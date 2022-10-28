from email.policy import default
from random import choices
from turtle import title
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models


class Category(models.Model):
    title =models.CharField(max_length=255)
    slug =models.SlugField()

    class Meta:
        ordering=('title',)
        verbose_name_plural= 'Categories'

    def __str__(self):
        return self.title    

class Post(models.Model):
    ACTIVE ='active'
    DRAFT ='draft'

    CHOICES_STATUS =(
        (ACTIVE,'Active'),
        (DRAFT,'Draft')
    )
    category =models.ForeignKey(Category, related_name='posts',on_delete =models.CASCADE)
    title =models.CharField(max_length=255)
    slug =models.SlugField()
    intro =models.TextField()
    body =models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    status =models.CharField(max_length=10, choices=CHOICES_STATUS ,default=ACTIVE)
    

    class Meta:
        ordering =('-created_at',)

    def __str__(self):
        return self.title     




class Comments(models.Model):
    post =models.ForeignKey(Post, related_name='comments',on_delete =models.CASCADE)    
    name=models.CharField(max_length=255)
    email=models.EmailField()
    body =models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
