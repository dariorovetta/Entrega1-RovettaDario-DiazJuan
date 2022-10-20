from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Familiar(models.Model):
    
    def __str__(self):
      return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Fecha de Nacimiento: {self.fechaNacimiento}"

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fechaNacimiento = models.DateField(null=True)
    
class Avatar(models.Model):
  # Vinculo con el usuario
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  # Subcaperta avatares de media :) 
  imagen = models.ImageField(upload_to='avatares', null=True, blank = True)