from ninja import ModelSchema
from .models import Livro

class LivroSchema(ModelSchema):
    class Config:
        model = Livro
        model_fields = ['id','titulo','autor','preco','descricao','categoria', 'img', 'estoque', 'qtdVendas',
                        'dataLancamento', 'avaliacaoGeral', 'qtdAvaliacoes']