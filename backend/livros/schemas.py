from typing import List
from ninja import ModelSchema
from .models import Combo, Livro

class LivroSchema(ModelSchema):
    class Config:
        model = Livro
        model_fields = ['id', 'titulo', 'autor', 'preco', 'descricao', 'categoria', 'img', 'estoque', 'qtdVendas',
                        'dataLancamento', 'dataLancamentoLoja', 'avaliacaoGeral', 'qtdAvaliacoes']

class ComboSchema(ModelSchema):
    id: int
    tituloCombo: str
    descricao: str
    livros: List[LivroSchema]

    class Config:
        model = Combo
        model_fields = ['preco', 'dataLancamentoLoja', 'qtdVendas']
