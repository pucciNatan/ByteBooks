from ninja import Router
from .models import Carrinho, ItemCarrinho
from livros.models import Livro
from django.http import JsonResponse
from .schemas import CarrinhoSchema, AtualizarQuantidadeSchema
from core.auth import JWTAuth

carrinho_router = Router()

@carrinho_router.post('adicionarItemAoCarrinho/{idLivro}', auth=JWTAuth())
def adicionarAoCarrinho(request, idLivro: int, quantidade: int = 1):
    try:
        idUsuario = request.auth['userId']

        # Verifica se o livro existe
        livroEncontrado = Livro.objects.filter(id=idLivro).first()
        if livroEncontrado is None:
            return JsonResponse({'msg': 'Livro não encontrado.'}, status=404)
        
        # Busca o carrinho do usuário
        carrinhoEncontrado = Carrinho.objects.filter(idUsuario=idUsuario).first()
        if carrinhoEncontrado is None:
            return JsonResponse({'msg': 'Carrinho não encontrado.'}, status=404)
        
        # Cria ou atualiza o item no carrinho
        item, created = ItemCarrinho.objects.get_or_create(
            carrinho=carrinhoEncontrado,
            livro=livroEncontrado,
            defaults={'quantidade': quantidade}
        )
        if not created:
            item.quantidade += quantidade
            item.save()

        return JsonResponse({'msg': 'Livro adicionado com sucesso!'}, status=201)
    
    except Exception as e:
        return JsonResponse({'msg': f'Erro inesperado: {str(e)}'}, status=500)
    
@carrinho_router.delete('removerDoCarrinho/{idLivro}', auth=JWTAuth())
def removerDoCarrinho(request, idLivro: int):
    try:
        idUsuario = request.auth['userId']

        # Verifica se o livro existe
        livroEncontrado = Livro.objects.filter(id=idLivro).first()
        if livroEncontrado is None:
            return JsonResponse({'msg': 'Livro não encontrado.'}, status=404)
        
        # Busca o carrinho do usuário
        carrinhoEncontrado = Carrinho.objects.filter(idUsuario=idUsuario).first()
        if carrinhoEncontrado is None:
            return JsonResponse({'msg': 'Carrinho não encontrado.'}, status=404)
        
        # Busca o item no carrinho para remover
        item = ItemCarrinho.objects.filter(carrinho=carrinhoEncontrado, livro=livroEncontrado).first()
        if item is None:
            return JsonResponse({'msg': 'Item não encontrado no carrinho.'}, status=404)
        
        item.delete()

        return JsonResponse({'msg': 'Livro removido com sucesso!'}, status=200)
    
    except Exception as e:
        return JsonResponse({'msg': f'Erro inesperado: {str(e)}'}, status=500)
    
@carrinho_router.get('retornaCarrinho/', response=CarrinhoSchema, auth=JWTAuth())
def retornaCarrinho(request):
    try:
        idUsuario = request.auth['userId']

        # Busca o carrinho do usuário
        carrinhoEncontrado = Carrinho.objects.filter(idUsuario=idUsuario).first()
        if carrinhoEncontrado is None:
            return JsonResponse({'msg': 'Carrinho não encontrado.'}, status=404)
        
        return carrinhoEncontrado
    
    except Exception as e:
        return JsonResponse({'msg': f'Erro inesperado: {str(e)}'}, status=500)
    
@carrinho_router.get('retornaQtdCarrinho/', auth=JWTAuth())
def retornaQtdCarrinho(request):
    try:
        idUsuario = request.auth['userId']

        # Busca o carrinho do usuário
        carrinhoEncontrado = Carrinho.objects.filter(idUsuario=idUsuario).first()
        if carrinhoEncontrado is None:
            return JsonResponse({'msg': 'Carrinho não encontrado.'}, status=404)
        
        # Retorna a quantidade de itens usando a relação reversa 'itens'
        return JsonResponse({'qtd': carrinhoEncontrado.itens.count()}, status=200)
    
    except Exception as e:
        return JsonResponse({'msg': f'Erro inesperado: {str(e)}'}, status=500)

@carrinho_router.patch('atualizarQuantidade/{idLivro}', auth=JWTAuth())
def atualizarQuantidade(request, idLivro: int, payload: AtualizarQuantidadeSchema):
    try:
        idUsuario = request.auth['userId']
        carrinhoEncontrado = Carrinho.objects.filter(idUsuario=idUsuario).first()
        if not carrinhoEncontrado:
            return JsonResponse({'msg': 'Carrinho não encontrado.'}, status=404)
        
        item = ItemCarrinho.objects.filter(carrinho=carrinhoEncontrado, livro__id=idLivro).first()
        if not item:
            return JsonResponse({'msg': 'Item não encontrado no carrinho.'}, status=404)
        if payload.adicionar:
            if item.livro.estoque > item.quantidade:
                item.quantidade += 1
        else:   
            if item.quantidade > 1:
                item.quantidade -= 1
            else:
                item.delete()
                return JsonResponse({'msg': 'Item removido do carrinho.'}, status=200)
        
        item.save()
        return JsonResponse({'msg': 'Quantidade atualizada com sucesso!', 'quantidade': item.quantidade}, status=200)
    except Exception as e:
        return JsonResponse({'msg': f'Erro inesperado: {str(e)}'}, status=500)


