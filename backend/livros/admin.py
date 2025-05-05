from django.contrib import admin
from .models import Livro, Combo

class LivroAdmin(admin.ModelAdmin):
    fields = ['titulo', 'autor', 'preco', 'descricao', 'categoria', 'img', 'dataLancamento', 
              'estoque', 'idioma', 'editora', 'qtdPaginas', 'dataLancamentoLoja', 'chamadaDesc', 
              'qtdAvaliacoes', 'avaliacaoGeral']
    

class ComboAdmin(admin.ModelAdmin):
    fields = ['tituloCombo', 'livros', 'preco', 'descricao', 'chamadaDesc', 'descricaoDetalhada', 'dataLancamentoLoja']

admin.site.register(Livro, LivroAdmin)
admin.site.register(Combo, ComboAdmin)
