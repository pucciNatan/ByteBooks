from django.contrib import admin
from .models import Livro, Combo

class LivroAdmin(admin.ModelAdmin):
    fields = ['titulo', 'autor', 'preco', 'descricao', 'categoria', 'img', 'dataLancamento', 'estoque']

class ComboAdmin(admin.ModelAdmin):
    fields = ['tituloCombo', 'livros', 'preco', 'descricao']

admin.site.register(Livro, LivroAdmin)
admin.site.register(Combo, ComboAdmin)
