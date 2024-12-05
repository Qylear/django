import django.forms 
from .models import Article
from .models import Commentaire

class Articleform(django.forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

class Commentaireform(django.forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['post', 'author', 'text']

