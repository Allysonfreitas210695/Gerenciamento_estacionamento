# Generated by Django 4.2.3 on 2024-02-08 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento_estacionamento', '0007_remove_veiculo_data_cadastro_veiculo_atualizado_em_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='estacionamento',
            options={'verbose_name': 'Estacionamento', 'verbose_name_plural': 'Estacionamentos'},
        ),
        migrations.AlterModelOptions(
            name='tarifa',
            options={'verbose_name': 'Tarifa', 'verbose_name_plural': 'Tarifas'},
        ),
        migrations.AlterModelOptions(
            name='veiculo',
            options={'verbose_name': 'Veiculo', 'verbose_name_plural': 'Veiculos'},
        ),
    ]
