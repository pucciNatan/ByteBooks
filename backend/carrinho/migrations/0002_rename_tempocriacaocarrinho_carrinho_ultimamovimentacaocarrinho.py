# Generated by Django 5.1.3 on 2025-04-01 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrinho',
            old_name='tempoCriacaoCarrinho',
            new_name='ultimaMovimentacaoCarrinho',
        ),
    ]
