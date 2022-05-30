from django.db import models
from django.forms import CharField, DateField, EmailField, ImageField


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)
    nick = models.CharField(max_length=20)


class Blog(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)


class Comment(models.Model): 
    date = models.DateField()
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)