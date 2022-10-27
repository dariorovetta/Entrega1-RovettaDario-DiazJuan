from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.


class Familiar(models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Fecha de Nacimiento: {self.fechaNacimiento}"

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fechaNacimiento = models.DateField(null=True)


class BlogFamiliar(models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Fecha de Nacimiento: {self.fechaNacimiento}"

    titulo = models.CharField(max_length=30)
    sub_titulo = models.CharField(max_length=30)
    descripcion = RichTextField()
    autor = models.CharField(max_length=30)
    fechaCreacion = models.DateField(null=True)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
