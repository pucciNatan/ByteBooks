from django.db import models
from livros.models import Livro 

class Carrinho(models.Model):
    idUsuario = models.IntegerField() 
    listaLivros = models.ManyToManyField(Livro)
    ultimaMovimentacaoCarrinho  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrinho de {self.idUsuario}'