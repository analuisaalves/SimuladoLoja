# Generated by Django 5.0.6 on 2024-06-13 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lojinha', '0004_promocao_novo_preco_promocao_produto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='endereco',
            new_name='mensagem',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='razaosocial',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='contato',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='contato',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='contato',
            name='telefone',
        ),
    ]