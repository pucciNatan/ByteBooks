from ninja import Router
from .models import Carrinho
from livros.models import Livro
from django.http import JsonResponse
from .schemas import CarrinhoSchema
from core.auth import JWTAuth

carrinho_router = Router()

@carrinho_router.post('adicionarLivroAoCarrinho/{idLivro}', auth = JWTAuth())
def adicionarAoCarrinho(request, idLivro:int):
    try:
        idUsuario = request.auth['userId']

        livroEncontrado = Livro.objects.filter(id = idLivro).first()

        if livroEncontrado is None:
            return JsonResponse({'msg':'Livro não encontrado.'}, status = 401)
        
        carrinhoEncontrado = Carrinho.objects.filter(idUsuario = idUsuario).first()

        if carrinhoEncontrado is None:
            return JsonResponse({'msg':'Carrinho não encontrado.'}, status = 401)

        carrinhoEncontrado.listaLivros.add(livroEncontrado)

        return JsonResponse({'msg': 'Livro adicionado com sucesso!'}, status=201)
    
    except Exception as e:
        return JsonResponse({'msg': f'Erro inesperado: {str(e)}'}, status=500)
    
@carrinho_router.delete('removerDoCarrinho/{id}', auth=JWTAuth())
def removerDoCarrinho(request, id: int):
    try:
        idUsuario = request.auth['userId']

        livroEncontrado = Livro.objects.filter(id=id).first()
        if livroEncontrado is None:
            return JsonResponse({'msg': 'Livro não encontrado.'}, status=404)
        
        carrinhoEncontrado = Carrinho.objects.filter(idUsuario=idUsuario).first()
        if carrinhoEncontrado is None:
            return JsonResponse({'msg': 'Carrinho não encontrado.'}, status=404)

        carrinhoEncontrado.listaLivros.remove(livroEncontrado)

        return JsonResponse({'msg': 'Livro removido com sucesso!'}, status=200)
    
    except Exception as e:
        return JsonResponse({'msg': f'Erro inesperado: {str(e)}'}, status=500)
    
@carrinho_router.get('retornaCarrinho/', response = CarrinhoSchema, auth = JWTAuth())
def retornaCarrinho(request):
    try:
        idUsuario = request.auth['userId']

        carrinhoEncontrado = Carrinho.objects.filter(idUsuario = idUsuario).first()

        if carrinhoEncontrado is None:
            return JsonResponse({'msg':'Carrinho não encontrado.'}, status = 401)
        
        return carrinhoEncontrado
    
    except Exception as e:
        return JsonResponse({'msg': f'Erro inesperado: {str(e)}'}, status=500)
    
@carrinho_router.get('retornaQtdCarrinho/', auth = JWTAuth())
def retornaCarrinho(request):
    try:
        idUsuario = request.auth['userId']

        carrinhoEncontrado = Carrinho.objects.filter(idUsuario = idUsuario).first()
        
        return carrinhoEncontrado.listaLivros.count()
    
    except Exception as e:
        return JsonResponse({'msg': f'Erro inesperado: {str(e)}'}, status=500)