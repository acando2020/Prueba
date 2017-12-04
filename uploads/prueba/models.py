from django.db import models

# Create your models here.
class evento(models.Model):
    Nombre=models.CharField(max_length=10)