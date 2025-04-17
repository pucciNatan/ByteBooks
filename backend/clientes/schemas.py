from ninja import ModelSchema, Schema
from .models import Cliente as ClienteModel
from livros.schemas import LivroSchema
from datetime import datetime

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

class ClienteLivroSchema(LivroSchema):
    dataCompra: datetime 

class ClienteSchema(ModelSchema):
    livrosComprados: list[ClienteLivroSchema]

    class Config:
        model = ClienteModel
        model_fields = ["username", "first_name", "last_name",
                        "email", "dataNascimento", "livrosComprados"]