# Generated by Django 4.2.3 on 2024-02-08 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento_estacionamento', '0005_tarifa_estacionamento_tarifas'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='atualizado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='estacionamento',
            name='atualizado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='estacionamento',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tarifa',
            name='atualizado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='tarifa',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]