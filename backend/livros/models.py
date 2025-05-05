from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Livro(models.Model):
    CATEGORIA_DADOS     = 'dados'
    CATEGORIA_BACKEND   = 'backend'
    CATEGORIA_SOFTWARE  = 'software'

    CATEGORIA_CHOICES = [
        (CATEGORIA_DADOS,    'Dados'),
        (CATEGORIA_BACKEND,  'Backend'),
        (CATEGORIA_SOFTWARE, 'Software'),
    ]

    titulo = models.CharField(max_length=100, unique=True)
    autor = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    chamadaDesc = models.CharField(max_length=500, default="")
    descricao = models.TextField(max_length=5000, default="")
    categoria = models.CharField(
        max_length=10,
        choices=CATEGORIA_CHOICES,
        default=CATEGORIA_SOFTWARE,
    )
    estoque = models.IntegerField(default=0)
    img = models.ImageField(upload_to='imgsLivros/')
    qtdVendas = models.IntegerField(default=0)
    dataLancamento = models.DateField(default=timezone.now)
    dataLancamentoLoja = models.DateField(default=timezone.now)
    avaliacaoGeral = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    qtdAvaliacoes = models.IntegerField(default=0)
    qtdPaginas = models.IntegerField(default=0)
    editora = models.CharField(max_length=100, default="")
    idioma = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.titulo

class Combo(models.Model):
    tituloCombo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2) 
    chamadaDesc = models.CharField(max_length=500, default="")
    descricao = models.TextField(max_length=5000, default="")
    descricaoDetalhada = models.TextField(max_length=5000, default="")
    livros = models.ManyToManyField(Livro)
    dataLancamentoLoja = models.DateField(default=timezone.now)
    qtdVendas = models.IntegerField(default=0)

    def __str__(self):
        return self.tituloCombo
