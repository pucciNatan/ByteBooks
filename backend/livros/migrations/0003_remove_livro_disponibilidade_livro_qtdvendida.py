# Generated by Django 5.1.1 on 2024-10-31 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_livro_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='disponibilidade',
        ),
        migrations.AddField(
            model_name='livro',
            name='qtdVendida',
            field=models.IntegerField(default=0),
        ),
    ]
