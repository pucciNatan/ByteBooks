from ninja import Router
from django.http import JsonResponse
from django.db import IntegrityError
from django.conf import settings
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from typing import List
from .schemas import ClienteModel, ClienteSchemaRegister, ClienteSchemaLogin, ClienteSchema
from django.db.models import Q
from core.auth import JWTAuth
from carrinho.models import Carrinho
from livros.schemas import LivroSchema
from django.db.models import Prefetch
from .models import Compra 

import jwt

clientes_router = Router()

@clientes_router.get('protegida/', auth = JWTAuth())
def fui(request):
    return JsonResponse({"msg":"Logado com Sucesso!"})

@clientes_router.post('registro/')
def registraCliente(request, cliente: ClienteSchemaRegister):
    try:
        novoCliente = ClienteModel(
            username=cliente.username,
            email=cliente.email,
            first_name=cliente.first_name,
            last_name=cliente.last_name,
        )
        novoCliente.set_password(cliente.password)
        novoCliente.save()
        
        return JsonResponse({'msg': 'Cliente registrado com sucesso!'}, status=201)

    except IntegrityError:
        return JsonResponse({'msg': 'Email ou Username já cadastrado.'}, status=400)

    except Exception as e:
        return JsonResponse({'msg': f'Erro inesperado: {str(e)}'}, status=500)

@clientes_router.post('login/')
def logarUsuario(request, cliente: ClienteSchemaLogin):
    try:
        clienteEncontrado = ClienteModel.objects.filter(Q(username = cliente.emailUsername) | 
                                                        Q(email = cliente.emailUsername)).first()
                
        if clienteEncontrado is None:
            return JsonResponse({'msg':'Usuário não encontrado.'}, status = 401)
        
        if clienteEncontrado.check_password(cliente.password):

            tempoExpiracao = datetime.now() + timedelta(hours=settings.ACCESS_TOKEN_EXPIRE)

            payload = {
                'userId': clienteEncontrado.id,
                'exp': int(tempoExpiracao.timestamp())
            }

            token = jwt.encode(payload, settings.MY_SECRET, algorithm="HS256")
            
            carrinhoExistente = Carrinho.objects.filter(idUsuario = clienteEncontrado.id).first()

            if carrinhoExistente is None:
                novoCarrinho = Carrinho(
                    idUsuario = clienteEncontrado.id,
                )

                novoCarrinho.save()

            return JsonResponse({'token':token, 'nomeUsuario': clienteEncontrado.first_name, 'username':clienteEncontrado.username,}, status = 200)
        else:
            return JsonResponse({'msg':'Senha ou email incorretos.'}, status = 400)
        
    except ClienteModel.DoesNotExist:
        return JsonResponse({'msg':'Senha ou email incorretos.'}, status = 401)
    
@clientes_router.get("cliente/", response=ClienteSchema, auth=JWTAuth())
def get_cliente(request):
    usuario_id = request.auth["userId"]

    # Pré-carrega o cliente com o through model 'compra_set', trazendo os livros relacionados
    cliente = get_object_or_404(
        ClienteModel.objects.prefetch_related(
            Prefetch("compra_set", queryset=Compra.objects.select_related("livro"))
        ),
        id=usuario_id
    )
    
    # Cria uma lista de livros enriquecida com o campo dataCompra
    livros_comprados_com_data = []
    for compra in cliente.compra_set.all():
        livro = compra.livro
        # Converte o objeto livro para dicionário utilizando o schema
        livro_data = LivroSchema.from_orm(livro).dict()
        livro_data["dataCompra"] = compra.dataCompra
        livros_comprados_com_data.append(livro_data)
    
    # Monta o dicionário de resposta com os dados do cliente
    cliente_data = {
        "username": cliente.username,
        "first_name": cliente.first_name,
        "last_name": cliente.last_name,
        "email": cliente.email,
        "dataNascimento": cliente.dataNascimento,
        "livrosComprados": livros_comprados_com_data
    }
    
    return cliente_data

