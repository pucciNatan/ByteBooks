from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Livro(models.Model):
    CATEGORIA_DADOS = 'dados'
    CATEGORIA_BACKEND = 'backend'
    CATEGORIA_SOFTWARE = 'software'

    CATEGORIA_CHOICES = [
        (CATEGORIA_DADOS, 'Ciência de Dados'),
        (CATEGORIA_BACKEND, 'Desenvolvimento Back-End'),
        (CATEGORIA_SOFTWARE, 'Engenharia de Software'),
    ]

    titulo = models.CharField(max_length=100, unique=True, verbose_name='Título')
    autor = models.CharField(max_length=100, verbose_name='Autor')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço (R$)')
    chamadaDesc = models.CharField(max_length=500, default="", verbose_name='Descrição curta (Home)')
    descricao = models.TextField(max_length=5000, default="", verbose_name='Descrição completa')
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, default=CATEGORIA_SOFTWARE, verbose_name='Categoria')
    estoque = models.IntegerField(default=0, verbose_name='Estoque')
    img = models.ImageField(upload_to='imgsLivros/', verbose_name='Imagem da capa')
    qtdVendas = models.IntegerField(default=0, verbose_name='Quantidade de vendas')
    dataLancamento = models.DateField(default=timezone.now, verbose_name='Data de lançamento')
    dataLancamentoLoja = models.DateField(default=timezone.now, verbose_name='Disponível na loja em')
    avaliacaoGeral = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0, verbose_name='Avaliação média (0-5)')
    qtdAvaliacoes = models.IntegerField(default=0, verbose_name='Número de avaliações')
    qtdPaginas = models.IntegerField(default=0, verbose_name='Quantidade de páginas')
    editora = models.CharField(max_length=100, default="", verbose_name='Editora')
    idioma = models.CharField(max_length=100, default="", verbose_name='Idioma')

    def __str__(self):
        return self.titulo


class Combo(models.Model):
    tituloCombo = models.CharField(max_length=100, verbose_name='Título do combo')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço do combo (R$)')
    chamadaDesc = models.CharField(max_length=500, default="", verbose_name='Descrição curta (Home)')
    descricao = models.TextField(max_length=5000, default="", verbose_name='Descrição completa')
    descricaoDetalhada = models.TextField(max_length=5000, default="", verbose_name='O que o combo contém?')
    livros = models.ManyToManyField(Livro, verbose_name='Livros incluídos')
    dataLancamentoLoja = models.DateField(default=timezone.now, verbose_name='Disponível na loja em')
    qtdVendas = models.IntegerField(default=0, verbose_name='Quantidade de vendas')

    def __str__(self):
        return self.tituloCombo
