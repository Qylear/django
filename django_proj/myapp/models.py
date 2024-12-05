from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class Commentaire(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        post = self.cleaned_data.get('post')
        return post