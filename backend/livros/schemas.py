from typing import List
from ninja import ModelSchema
from .models import Combo, Livro

class LivroSchema(ModelSchema):
    class Config:
        model = Livro
        model_fields = ['id', 'titulo', 'autor', 'preco', 'chamadaDesc', 'descricao', 'categoria', 'img', 'estoque', 'qtdVendas',
                        'dataLancamento', 'dataLancamentoLoja', 'avaliacaoGeral', 'qtdAvaliacoes', 'qtdPaginas', 'editora', 'idioma']

class ComboSchema(ModelSchema):
    livros: List[LivroSchema]

    class Config:
        model = Combo
        model_fields = ['id', 'preco', 'dataLancamentoLoja', 'qtdVendas', 'descricao', 'descricaoDetalhada', 'tituloCombo', 'chamadaDesc']
