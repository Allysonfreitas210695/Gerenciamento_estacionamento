# Generated by Django 4.2.3 on 2024-02-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AddField(
            model_name='profile',
            name='perfil',
            field=models.CharField(choices=[('admin', 'Admin'), ('outro_perfil', 'Outro Perfil')], default='admin', max_length=20),
        ),
    ]
