# Generated by Django 3.2.6 on 2022-07-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunicacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.CharField(max_length=255, verbose_name='E-mail')),
                ('assunto', models.CharField(max_length=255, verbose_name='Assunto')),
                ('descricao', models.TextField(verbose_name='Mensagem')),
            ],
            options={
                'verbose_name': 'Promoções',
                'verbose_name_plural': 'Promoções',
            },
        ),
    ]