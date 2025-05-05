from ninja import Router
from django.http import JsonResponse
from django.db import IntegrityError
from django.conf import settings
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from typing import List
from .schemas import ClienteModel, ClienteSchemaRegister, ClienteSchemaLogin, ClienteSchema, ClienteSchemaUpdate
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

@clientes_router.post("registro/", response={201: dict, 400: dict, 500: dict})
def registra_cliente(request, cliente: ClienteSchemaRegister):
    try:
        data_nasc = datetime.strptime(cliente.dataNascimento, "%d/%m/%Y").date()
        
        novo_cliente = ClienteModel(
            username=cliente.username,
            email=cliente.email,
            first_name=cliente.first_name,
            last_name=cliente.last_name,
            dataNascimento=data_nasc,
        )
        novo_cliente.set_password(cliente.password)
        novo_cliente.save()

        return JsonResponse({"msg": "Cliente registrado com sucesso!"}, status=201)

    except IntegrityError:
        return JsonResponse({"msg": "Email ou Username já cadastrado."}, status=400)

    except Exception as e:
        return JsonResponse({"msg": f"Erro inesperado: {e}"}, status=500)

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

    # Pré‑carrega as compras já com o livro
    cliente = get_object_or_404(
        ClienteModel.objects.prefetch_related(
            Prefetch("compra_set", queryset=Compra.objects.select_related("livro"))
        ),
        id=usuario_id,
    )

    # Lista de livros enriquecida
    livros_comprados = []
    for compra in cliente.compra_set.all():
        livro_data = LivroSchema.from_orm(compra.livro).model_dump()
        livro_data["dataCompra"] = compra.dataCompra
        livro_data["quantidade"] = compra.quantidade        # ← campo exigido
        livros_comprados.append(livro_data)

    # Retorna no formato do schema
    return {
        "username": cliente.username,
        "first_name": cliente.first_name,
        "last_name": cliente.last_name,
        "email": cliente.email,
        "dataNascimento": cliente.dataNascimento,
        "livrosComprados": livros_comprados,
    }

@clientes_router.get('saldo/', auth=JWTAuth())
def getSaldoCliente(request):
    usuario_id = request.auth["userId"]

    cliente = get_object_or_404(
        ClienteModel.objects.prefetch_related(
            Prefetch("compra_set", queryset=Compra.objects.select_related("livro"))
        ),
        id=usuario_id
    )

    return cliente.saldo

@clientes_router.post('saldo/', auth=JWTAuth())
def postAtualizarSaldo50(request):
    usuario_id = request.auth["userId"]

    cliente = get_object_or_404(
        ClienteModel.objects.prefetch_related(
            Prefetch("compra_set", queryset=Compra.objects.select_related("livro"))
        ),
        id=usuario_id
    )

    cliente.saldo = cliente.saldo + 50
    
    cliente.save()
    return JsonResponse({'msg':'Saldo atualizado com sucesso!'})

@clientes_router.patch(
    "atualizarInfos/",
    response={200: dict, 400: dict, 401: dict, 500: dict},
    auth=JWTAuth(),
)
def atualizar_infos(request, dados: ClienteSchemaUpdate):
    usuario_id = request.auth["userId"]
    cli = get_object_or_404(ClienteModel, id=usuario_id)

    try:
        incoming = dados.dict(exclude_unset=True)

        novo_email    = incoming.get("email", cli.email)
        novo_username = incoming.get("username", cli.username)

        conflito = ClienteModel.objects.filter(~Q(id=usuario_id), Q(email=novo_email) | Q(username=novo_username)
        ).exists()
        if conflito:
            return JsonResponse(
                {"msg": "Email ou Username já utilizados por outro usuário."}, status=400
            )

        # ─────────── Atualiza somente o que veio ──────────
        if "email"       in incoming: cli.email       = incoming["email"]
        if "username"    in incoming: cli.username    = incoming["username"]
        if "first_name"  in incoming: cli.first_name  = incoming["first_name"]
        if "last_name"   in incoming: cli.last_name   = incoming["last_name"]

        if "dataNascimento" in incoming:
            cli.dataNascimento = datetime.strptime(
                incoming["dataNascimento"], "%d/%m/%Y"
            ).date()

        if incoming.get("password"):
            cli.set_password(incoming["password"])

        cli.save()
        return JsonResponse({"msg": "Dados atualizados com sucesso!"}, status=200)

    except IntegrityError:
        return JsonResponse(
            {"msg": "Erro de integridade (possível duplicidade)."}, status=400
        )
    except Exception as e:
        return JsonResponse({"msg": f"Erro inesperado: {e}"}, status=500)
