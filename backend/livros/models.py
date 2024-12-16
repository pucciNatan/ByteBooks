from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Livro(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    autor = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    estoque = models.IntegerField(default=0)
    img = models.ImageField(upload_to='imgsLivros/')
    qtdVendas = models.IntegerField(default=0)
    dataLancamento = models.DateField(default=timezone.now)
    dataLancamentoLoja = models.DateField(default=timezone.now)
    avaliacaoGeral = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    qtdAvaliacoes = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

class Combo(models.Model):
    tituloCombo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2) 
    descricao = models.TextField()
    livros = models.ManyToManyField(Livro)
    dataLancamentoLoja = models.DateField(default=timezone.now)
    qtdVendas = models.IntegerField(default=0)

    def __str__(self):
        return self.tituloCombo
