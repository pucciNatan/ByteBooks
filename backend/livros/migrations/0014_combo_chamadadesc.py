# Generated by Django 5.1.3 on 2024-12-27 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0013_livro_chamadadesc_alter_livro_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='combo',
            name='chamadaDesc',
            field=models.CharField(default='', max_length=500),
        ),
    ]