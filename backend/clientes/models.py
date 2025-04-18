from django.db import models
from django.contrib.auth.models import AbstractUser
from livros.models import Livro

class Cliente(AbstractUser):
    email = models.EmailField(unique=True, max_length=100)
    dataNascimento = models.DateField(null=True, blank=True)
    livrosComprados = models.ManyToManyField(
        Livro,
        through='Compra',
        related_name='compradores'
    )
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.email

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    dataCompra = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.cliente} comprou {self.livro} em {self.dataCompra}'