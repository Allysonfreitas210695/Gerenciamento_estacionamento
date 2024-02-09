# Generated by Django 4.2.3 on 2024-02-08 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento_estacionamento', '0004_estacionamento_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=100)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_diaria', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='estacionamento',
            name='tarifas',
            field=models.ManyToManyField(to='gerenciamento_estacionamento.tarifa'),
        ),
    ]