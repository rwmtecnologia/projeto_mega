# Generated by Django 3.2.6 on 2023-01-23 14:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220725_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicacao',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AddField(
            model_name='comunicacao',
            name='criados',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comunicacao',
            name='modificado',
            field=models.DateField(auto_now=True, verbose_name='Atualização'),
        ),
    ]
