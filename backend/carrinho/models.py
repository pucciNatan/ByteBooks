from django.db import models
from livros.models import Livro

class Carrinho(models.Model):
    idUsuario = models.IntegerField()
    ultimaMovimentacaoCarrinho = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrinho de {self.idUsuario}'

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name="itens")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.livro.titulo} (Quantidade: {self.quantidade})"
