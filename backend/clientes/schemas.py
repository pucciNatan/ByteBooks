from ninja import ModelSchema, Schema
from .models import Cliente as ClienteModel

class ClienteSchemaRegister(Schema):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str

class ClienteSchemaLogin(Schema):
    emailOrUsername: str
    password: str

class ClienteSchema(ModelSchema):
    class Config:
        model = ClienteModel
        model_fields = ['username', 'email', 'first_name','last_name']