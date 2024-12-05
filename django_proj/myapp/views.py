from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import Articleform
from .models import Commentaire
from .forms import Commentaireform
from .forms import Commentaireform

# Create your views here.

def post_list(request):
    articles = Article.objects.all()
    return render(request, 'post_list.html', {'Articles': articles})

def post_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'post_detail.html', {'Article': article})

def create_post(request):
    if request.method == 'POST':
        form = Articleform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = Articleform()
    return render(request, 'create_post.html', {'form': form})

def edit_post(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = Articleform(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=article.id)
    else:
        form = Articleform(instance=article)
    return render(request, 'edit_post.html', {'form': form})

def add_comment(request, id):
    Article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = Commentaireform(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.Article = Article
            commentaire.save()
            return redirect('post_detail', id=Article.id)
    else:
        form = Commentaireform()
    return render(request, 'add_comment.html', {'form': form, 'Article': Article})

def edit_comment(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)  # Changer Commentaire en commentaire (minuscule)
    if request.method == 'POST':  # Changer la condition pour 'POST'
        form = Commentaireform(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=commentaire.article.id)  # Utiliser 'article' en minuscule
    else:
        form = Commentaireform(instance=commentaire)
    return render(request, 'edit_comment.html', {'form': form})

def delete_post(request, id):
    article = get_object_or_404(Article, id=id)  # Changer Article en article (minuscule)
    article.delete()
    return redirect('post_list')

def delete_comment(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)  # Changer Commentaire en commentaire (minuscule)
    article_id = commentaire.article.id  # Utiliser 'article' en minuscule
    commentaire.delete()
    return redirect('post_detail', id=article_id)