from django.contrib import admin

from .models import Topo, Portifolio, Galeria_Portifolio, Parceiro, Promocoes, \
    Galeria_Promocoes, Servico, Dicas, Footer

@admin.register(Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagem', 'ativo', 'modificado')

@admin.register(Topo)
class TopoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo', 'modificado')

@admin.register(Portifolio)
class TopoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'modificado')

@admin.register(Galeria_Portifolio)
class Galeria_PortifolioAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'imagem', 'ativo', 'modificado')

@admin.register(Promocoes)
class TopoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'modificado')

@admin.register(Galeria_Promocoes)
class Galeria_PortifolioAdmin(admin.ModelAdmin):
    list_display = ('titulo_promo', 'imagem_promo', 'ativo', 'modificado')

@admin.register(Servico)
class Galeria_PortifolioAdmin(admin.ModelAdmin):
    list_display = ('servico_titulo', 'ativo', 'modificado')

@admin.register(Dicas)
class DicasAdmin(admin.ModelAdmin):
    list_display = ('titulo_dica', 'ativo', 'modificado')

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('cont_descricao', 'ativo', 'modificado')



