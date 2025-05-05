from ninja import ModelSchema, Schema
from .models import Cliente as ClienteModel
from livros.schemas import LivroSchema
from datetime import datetime
from typing import Optional
from pydantic import EmailStr

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
    quantidade: int
    dataCompra: datetime

class ClienteSchema(ModelSchema):
    livrosComprados: list[ClienteLivroSchema]

    class Config:
        model = ClienteModel
        model_fields = ["username", "first_name", "last_name",
                        "email", "dataNascimento", "livrosComprados"]
        
class ComprarLivroIn(Schema):
    quantidade: int = 1

class ClienteSchemaUpdate(Schema):
    username:       Optional[str]      = None
    email:          Optional[EmailStr] = None
    first_name:     Optional[str]      = None
    last_name:      Optional[str]      = None
    dataNascimento: Optional[str]      = None
    password:       Optional[str]      = None