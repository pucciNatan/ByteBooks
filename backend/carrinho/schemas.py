from typing import List
from ninja import ModelSchema, Schema
from livros.schemas import LivroSchema
from .models import Carrinho, ItemCarrinho

class ItemCarrinhoSchema(ModelSchema):
    livro: LivroSchema  

    class Config:
        model = ItemCarrinho
        model_fields = ['id', 'livro', 'quantidade']

class CarrinhoSchema(ModelSchema):
    itens: List[ItemCarrinhoSchema] 

    class Config:
        model = Carrinho
        model_fields = ['id', 'idUsuario', 'ultimaMovimentacaoCarrinho']

class AtualizarQuantidadeSchema(Schema):
    adicionar: bool
