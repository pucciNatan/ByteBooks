from ninja import ModelSchema, Schema
from .models import Cliente as ClienteModel

class ClienteSchemaRegister(Schema):
    username: str
    first_name: str
    last_name: str
    dataNascimento: str
    email: str
    password: str

class ClienteSchemaLogin(Schema):
    emailUsername: str
    password: str
