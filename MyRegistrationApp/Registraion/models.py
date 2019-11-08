from django.db import models

# Create your models here.
from django import forms

class Person(models.Model):
    username=models.CharField(max_length=120)
    email=models.EmailField(max_length=150)
    phone=models.CharField(max_length=12)
    pwd=models.CharField(max_length=150)
    def __str__(self):
        return self.username