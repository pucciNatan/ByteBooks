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
        