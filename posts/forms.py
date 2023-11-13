from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'title': 'Título',
            'text': 'Conteúdo',
        }