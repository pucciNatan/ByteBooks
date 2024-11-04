from django.contrib import admin
from .models import Livro

class LivroAdmin(admin.ModelAdmin):
    fields = ['titulo', 'autor', 'preco', 'descricao', 'categoria', 'img', 'estoque']

admin.site.register(Livro, LivroAdmin)
