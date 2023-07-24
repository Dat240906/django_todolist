from django.db import models
from django.forms import CharField

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.username
    
    
class Service(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    time = models.DateTimeField()
