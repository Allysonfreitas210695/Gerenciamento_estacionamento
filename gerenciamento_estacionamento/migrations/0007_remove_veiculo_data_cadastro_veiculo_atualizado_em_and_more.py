# Generated by Django 4.2.3 on 2024-02-08 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento_estacionamento', '0006_cliente_atualizado_em_cliente_criado_em_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='data_cadastro',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='atualizado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]