from typing import List
from ninja import ModelSchema
from livros.schemas import LivroSchema
from .models import Carrinho

class CarrinhoSchema(ModelSchema):
    listaLivros: List[LivroSchema]

    class Config:
        model = Carrinho
        model_fields = ['id', 'idUsuario', 'ultimaMovimentacaoCarrinho']
