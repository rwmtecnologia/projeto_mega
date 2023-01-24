# Generated by Django 3.2.6 on 2022-02-16 16:52

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('titulo_dica', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descricao_dica', models.TextField(max_length=800, verbose_name='Descrição')),
                ('Autor_dica', models.CharField(max_length=100, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Dica',
                'verbose_name_plural': 'Dicas',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cont_descricao', models.TextField(max_length=400, verbose_name='Descrição')),
                ('cont_endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('cont_email', models.EmailField(max_length=150, verbose_name='E-mail')),
                ('cont_telefone', models.CharField(max_length=30, verbose_name='Telefone')),
                ('cont_localizacao', models.TextField(max_length=400, verbose_name='Localização')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contato',
            },
        ),
        migrations.CreateModel(
            name='Galeria_Portifolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Galeria Portifolio',
                'verbose_name_plural': 'Galeria Portifolio',
            },
        ),
        migrations.CreateModel(
            name='Galeria_Promocoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('titulo_promo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('imagem_promo', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem')),
                ('descricao_promo', models.TextField(max_length=400, verbose_name='Descrição')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Preço')),
            ],
            options={
                'verbose_name': 'Galeria Promoções',
                'verbose_name_plural': 'Galeria Promoções',
            },
        ),
        migrations.CreateModel(
            name='Parceiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descricao', models.TextField(max_length=400, verbose_name='Descrição')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem')),
                ('website', models.CharField(max_length=200, verbose_name='Website')),
                ('contato', models.CharField(max_length=15, verbose_name='Contato')),
                ('email', models.CharField(max_length=100, verbose_name='E-mail')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Parceiro',
                'verbose_name_plural': 'Parceiros',
            },
        ),
        migrations.CreateModel(
            name='Portifolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Portifolio',
                'verbose_name_plural': 'Portifolio',
            },
        ),
        migrations.CreateModel(
            name='Promocoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Promoções',
                'verbose_name_plural': 'Promoções',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('servico_titulo', models.CharField(max_length=100, verbose_name='Serviço')),
                ('servico_descricao', models.TextField(max_length=200, verbose_name='Descrição')),
                ('servico_icone', models.CharField(choices=[('bi-briefcase', 'Maleta'), ('bi-card-checklist', 'Lista'), ('bi-bar-chart', 'Grafico'), ('bi-binoculars', 'Binoculo'), ('bi-brightness-high', 'Luz'), ('bi-calendar4-week', 'Calendário')], max_length=30, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.CreateModel(
            name='Topo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titlulo')),
                ('logo', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Logo')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('skype', models.CharField(default='#', max_length=100, verbose_name='Skype')),
                ('linkedin', models.CharField(default='#', max_length=100, verbose_name='Linkedin')),
                ('titulo_banner', models.CharField(max_length=100, verbose_name='Titulo Banner')),
                ('descricao_banner', models.CharField(max_length=200, verbose_name='Descrição Banner')),
                ('fundo_banner', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Fundo Banner')),
            ],
            options={
                'verbose_name': 'Topo',
                'verbose_name_plural': 'Topo',
            },
        ),
    ]