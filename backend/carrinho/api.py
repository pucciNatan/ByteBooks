from ninja import Router
from .models import Carrinho
from livros.models import Livro
from django.http import JsonResponse
from .schemas import CarrinhoSchema
from core.auth import JWTAuth

carrinho_router = Router()

@carrinho_router.post('adicionarAoCarrinho/', auth = JWTAuth())
def adicionarAoCarrinho(request, idLivro):
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