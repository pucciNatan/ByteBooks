from ninja import Router
from django.http import JsonResponse
from django.db import IntegrityError
from django.conf import settings
from datetime import datetime, timedelta
from .schemas import ClienteModel, ClienteSchemaRegister, ClienteSchemaLogin
from django.db.models import Q
from core.auth import JWTAuth
from carrinho.models import Carrinho
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

            tempoExpiracao = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE)

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


