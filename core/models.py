import uuid
from django.db import models
from django.db.models import Model

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):


    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)


    class Meta:
        abstract = True


class Topo(Base):
    titulo = models.CharField('Titlulo', max_length=100)
    logo = StdImageField('Logo', upload_to=get_file_path, variations={'thumb': {'width': 600, 'height': 600, 'crop': True}})
    twitter = models.CharField('Twitter', max_length=100, default='#')
    facebook = models.CharField('Facebook', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    skype = models.CharField('Skype', max_length=100, default='#')
    linkedin = models.CharField('Linkedin', max_length=100, default='#')

    # Banner
    titulo_banner = models.CharField('Titulo Banner', max_length=100)
    descricao_banner = models.CharField('Descrição Banner', max_length=200)
    fundo_banner = StdImageField('Fundo Banner', upload_to=get_file_path, variations={'thumb': {'width': 1874, 'height': 1229, 'crop': True}})

    class Meta:
        verbose_name = 'Topo'
        verbose_name_plural = 'Topo'

    def __str__(self):
        return self.titulo


class Portifolio(Base):
    nome = models.CharField('Titulo', max_length=100)
    descricao = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Portifolio'
        verbose_name_plural = 'Portifolio'

    def __str__(self):
        return self.nome


class Galeria_Portifolio(Base):
    descricao = models.CharField('Descrição', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 800, 'height': 600, 'crop': True}})

    class Meta:
        verbose_name = 'Galeria Portifolio'
        verbose_name_plural = 'Galeria Portifolio'

    def __str__(self):
        return self.descricao


class Parceiro(Base):
    titulo = models.CharField('Titulo', max_length=100)
    descricao = models.TextField('Descrição', max_length=400)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 800, 'height': 600, 'crop': True}})
    website = models.CharField('Website', max_length=200)
    contato = models.CharField('Contato', max_length=15)
    email = models.CharField('E-mail', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)

    class Meta:
        verbose_name = 'Parceiro'
        verbose_name_plural = 'Parceiros'

    def __str__(self):
        return self.titulo


class Promocoes(Base):
    nome = models.CharField('Titulo', max_length=100)
    descricao = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Promoções'
        verbose_name_plural = 'Promoções'

    def __str__(self):
        return self.nome

class Galeria_Promocoes(Base):
    titulo_promo = models.CharField('Titulo', max_length=100)
    imagem_promo = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 300, 'height': 300, 'crop': True}})
    descricao_promo = models.TextField('Descrição', max_length=400)
    preco = models.DecimalField('Preço', max_digits=15, decimal_places=2)

    class Meta:
        verbose_name = 'Galeria Promoções'
        verbose_name_plural = 'Galeria Promoções'

    def __str__(self):
        return self.titulo_promo

class Servico(Base):
    ICONE_CHOICES = (
        ('bi-briefcase', 'Maleta'),
        ('bi-card-checklist', 'Lista'),
        ('bi-bar-chart', 'Grafico'),
        ('bi-binoculars', 'Binoculo'),
        ('bi-brightness-high', 'Luz'),
        ('bi-calendar4-week', 'Calendário'),
    )
    servico_titulo = models.CharField('Serviço', max_length=100)
    servico_descricao = models.TextField('Descrição', max_length=200)
    servico_icone = models.CharField('Icone', max_length=30, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico_titulo

class Dicas(Base):
    titulo_dica = models.CharField('Titulo', max_length=100)
    descricao_dica = models.TextField('Descrição', max_length=800)
    Autor_dica = models.CharField('Autor', max_length=100)


    class Meta:
        verbose_name = 'Dica'
        verbose_name_plural = 'Dicas'

    def __str__(self):
        return self.titulo_dica


class Footer(Base):
    cont_descricao = models.TextField('Descrição', max_length=400)
    cont_endereco = models.CharField('Endereço', max_length=200)
    cont_email = models.EmailField('E-mail', max_length=150)
    cont_telefone = models.CharField('Telefone', max_length=30)
    cont_localizacao = models.TextField('Localização', max_length=400)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contato'

    def __str__(self):
        return self.cont_descricao


class Comunicacao(Base):
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('E-mail', max_length=255)
    assunto = models.CharField('Assunto', max_length=255)
    descricao = models.TextField('Mensagem')

    class Meta:
        verbose_name = 'Comunicações'
        verbose_name_plural = 'Comunicações'

    def __str__(self):
        return self.nome