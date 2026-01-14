from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

""" 
Post model (title, content, author, date)
Create, list, detail, update, delete posts 
"""
# Create your models here.
class Category(models.Model):
        name = models.CharField(max_length=100, unique=True) 
        created_at = models.DateTimeField(auto_now_add=True) 
         
        class Meta:
            verbose_name_plural = "Categories" 
             
        def __str__(self): 
                return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f'{self.name} - {self.subject}'
    




