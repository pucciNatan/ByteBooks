# Generated by Django 5.1.3 on 2025-04-06 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0002_rename_tempocriacaocarrinho_carrinho_ultimamovimentacaocarrinho'),
        ('livros', '0013_alter_combo_descricao_alter_combo_descricaodetalhada_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='listaLivros',
        ),
        migrations.CreateModel(
            name='ItemCarrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='carrinho.carrinho')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.livro')),
            ],
        ),
    ]
