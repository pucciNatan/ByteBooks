from django.conf import settings
from django.http import JsonResponse
from ninja.security import HttpBearer
import jwt

class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            decoded = jwt.decode(token, settings.MY_SECRET, algorithms=["HS256"])
            return decoded
        
        except jwt.ExpiredSignatureError:
            return JsonResponse({'msg': 'Token expirado.'}, status=401)
        except jwt.DecodeError:
            return JsonResponse({'msg': 'Token inválido.'}, status=401)
        except Exception as e:
            return JsonResponse({'msg': f'Erro: {str(e)}'}, status=401)