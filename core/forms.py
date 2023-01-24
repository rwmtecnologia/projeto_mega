from django.forms import ModelForm
from .models import Comunicacao



class PostForm(ModelForm):
    class Meta:
        model = Comunicacao
        fields = ['nome', 'email', 'assunto', 'descricao']