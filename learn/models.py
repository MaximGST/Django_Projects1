from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=10, unique=True)
    text = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.name}, {self.text}'