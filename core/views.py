from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comunicacao
from .forms import PostForm

from .models import Topo, Portifolio, Galeria_Portifolio, Parceiro, Promocoes, Galeria_Promocoes, Servico, Dicas, Footer


class Post:
    def post_create(request):
        form = PostForm()
        if (request.method == 'POST'):
            form = PostForm(request.POST)
            if (form.is_valid()):
                post_nome = form.cleaned_data['nome']
                post_email = form.cleaned_data['email']
                post_assunto = form.cleaned_data['assunto']
                post_descricao = form.cleaned_data['descricao']
                new_post = Post(title=post_nome, slug=post_email, body=post_assunto, author=post_descricao,
                                status=post_status)
                new_post.save()
                # return redirect('blog:post_list')
        elif (request.method == 'GET'):
            return render(request, 'contact.html', {'form': form})


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['topos'] = Topo.objects.order_by('?').all()
        context['portifolio'] = Portifolio.objects.order_by('?').all()
        context['galeria_portifolio'] = Galeria_Portifolio.objects.order_by('?').all()
        context['parceiros'] = Parceiro.objects.order_by('?').all()
        context['promocoes'] = Promocoes.objects.order_by('?').all()
        context['galeria_promocoes'] = Galeria_Promocoes.objects.order_by('?').all()
        context['servico'] = Servico.objects.order_by('?').all()
        context['dicas'] = Dicas.objects.order_by('?').all()
        context['footer'] = Footer.objects.order_by('?').all()
        return context





