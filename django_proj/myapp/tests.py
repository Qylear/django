from django.test import TestCase
from django.urls import reverse
from .models import BlogPost, Comment

# Create your tests here.

class BlogTests(TestCase):
    def test_create_post(self):
        response = self.client.post(reverse('create_post'), {'title': 'Django Basics', 'content': 'Introduction to Django.'})
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(BlogPost.objects.count(), 1)

    def test_create_comment(self):
        post = BlogPost.objects.create(title='Test Post', content='Test Content')
        response = self.client.post(reverse('add_comment', args=[post.id]), {'author': 'John', 'text': 'Great post!'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 1)

    def test_delete_post(self):
        post = BlogPost.objects.create(title='Test Post', content='Test Content')
        response = self.client.post(reverse('delete_post', args=[post.id]))
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(BlogPost.objects.count(), 0)

    def test_delete_comment(self):
        post = BlogPost.objects.create(title='Test Post', content='Test Content')
        comment = Comment.objects.create(post=post, author='John', text='Great post!')
        response = self.client.post(reverse('delete_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Comment.objects.count(), 0)