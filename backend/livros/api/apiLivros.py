from ninja import Router
from django.http import JsonResponse
from django.db.models import Q
from typing import List
from ..models import Livro
from datetime import datetime, timedelta
from ..schemas import LivroSchema

livros_router = Router()

@livros_router.get('todosLivros/', response=List[LivroSchema])
def retornaTodosLivros(request):
    todosOsLivros = Livro.objects.all()

    if todosOsLivros.exists():
        return todosOsLivros
    else:
        return JsonResponse({'msg':'Livros não encontrados.'},status = 404)

@livros_router.get('livroPorPesquisa/{pesquisaTexto}', response=list[LivroSchema])
def livroPorId(request, pesquisaTexto: str):
    livroEncontrados = Livro.objects.filter(Q(titulo__icontains = pesquisaTexto) | 
                                            Q(descricao__icontains = pesquisaTexto) |
                                            Q(autor__icontains = pesquisaTexto))

    if livroEncontrados.exists():
        return livroEncontrados
    else:
        return JsonResponse({'msg':'Livros não encontrados.'},status = 404)

@livros_router.get('livroPorCategoria/{categoria}', response=List[LivroSchema])
def retornaLivroPorCategoria(request, categoria: str):
    livroEncontrado = Livro.objects.filter(categoria = categoria)
    if livroEncontrado.exists():
        return livroEncontrado
    else:
        return JsonResponse({'msg':'Livro não encontrado.'},status = 404)

@livros_router.get('todasCategorias/', response=List[str])
def retornaCategorias(request):
    categorias = Livro.objects.values_list('categoria', flat=True).distinct()

    if categorias.exists():
        return categorias
    else:
        return JsonResponse({'msg':'Categorias não encontradas.'},status = 404)


@livros_router.get('todosLivrosDisponiveis/', response=List[LivroSchema])
def retornaLivrosDisponiveis(request):
    livros_disponiveis = Livro.objects.filter(estoque__gt=0)

    if livros_disponiveis.exists():
        return livros_disponiveis
    else:
        return JsonResponse({'msg':'Livros não encontrado.'},status = 404)

@livros_router.get('ultimosLancamentos/', response=List[LivroSchema])
def retornaUltimosLancamentos(request):
    ultimosLancamentos = Livro.objects.all().order_by('-dataLancamento')

    if ultimosLancamentos.exists():
        return ultimosLancamentos
    return JsonResponse({'msg': 'Não há livros recentes.'})

@livros_router.get('ultimosLancamentosLoja/', response=List[LivroSchema])
def retornaUltimosLancamentos(request):
    ultimosLancamentos = Livro.objects.all().order_by('-dataLancamentoLoja')

    if ultimosLancamentos.exists():
        return ultimosLancamentos
    return JsonResponse({'msg': 'Não há livros recentes.'})

@livros_router.get('maisVendidos/', response=List[LivroSchema])
def retornaMaisVendidos(request):
    maisVendidos = Livro.objects.all().order_by('-qtdVendas')

    if maisVendidos.exists():
        return maisVendidos
    return JsonResponse({'msg': 'Não há livros recentes.'})


