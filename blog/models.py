from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name        

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() 
    date_posted = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)
    def __str__(self):
         return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments') 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

