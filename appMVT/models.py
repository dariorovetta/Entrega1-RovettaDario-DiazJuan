from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fechaCreacion = models.DateField(null=True)