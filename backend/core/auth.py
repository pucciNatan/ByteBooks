from django.conf import settings
from ninja.security import HttpBearer
from django.http import HttpRequest
import jwt

class JWTAuth(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str):
        try:
            data = jwt.decode(token, settings.MY_SECRET, algorithms=["HS256"])

        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return None
        
        if data:
            return data
        
        return None
        
'''from django.conf import settings
from django.http import HttpRequest
from ninja.security import HttpBearer
from django.db.models import Q
from clientes.models import Cliente
import jwt

class JWTAuth(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str):
        try:
            data = jwt.decode(token, settings.MY_SECRET, algorithms=["HS256"])
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return None
        
        user = Cliente.objects.filter(Q(username = data.get('user')) | 
                                      Q(email = data.get('user'))).first()
        if user:
            return user
        
        return None'''