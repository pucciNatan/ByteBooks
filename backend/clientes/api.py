from ninja import Router
from django.http import JsonResponse
from django.db import IntegrityError
from django.conf import settings
from datetime import datetime, timedelta
from .schemas import ClienteSchema, ClienteModel, ClienteSchemaRegister, ClienteSchemaLogin
from django.db.models import Q
import jwt

clientes_router = Router()

@clientes_router.post('registro/')
def registraCliente(request, cliente: ClienteSchemaRegister):
    try:
        novoCliente = ClienteModel(
                            username =  cliente.username,
                            email =  cliente.email,
                            first_name = cliente.first_name,
                            last_name = cliente.last_name,
                        )
        novoCliente.set_password(cliente.password)
        novoCliente.save()

        return JsonResponse({'msg':'Cliente registrado com sucesso!'}, status = 201)
    except IntegrityError:
        return JsonResponse({'msg':'Esse email já está cadastrado.'}, status = 400)
    except Exception as e:
        return JsonResponse({'msg':f'Erro inesperado: {str(e)}'}, status = 500)

@clientes_router.post('login/')
def logarUsuario(request, cliente: ClienteSchemaLogin):
    try:
        clienteEncontrado = ClienteModel.objects.filter(Q(username = cliente.emailOrUsername) | 
                                                Q(email = cliente.emailOrUsername)).first()
        if clienteEncontrado is None:
            return JsonResponse({'msg':'Usuário não encontrado.'}, status = 401)
        
        if clienteEncontrado.check_password(cliente.password):

            tempoExpiracao = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE)

            payload = {
                'user': cliente.emailOrUsername,
                'exp': int(tempoExpiracao.timestamp())
            }

            token = jwt.encode(payload, settings.MY_SECRET, algorithm="HS256")

            return JsonResponse({'token':token}, status = 200)
        else:
            return JsonResponse({'msg':'Senha incorreta.'}, status = 400)
        
    except ClienteModel.DoesNotExist:
        return JsonResponse({'msg':'Email não encontrado'}, status = 401)


