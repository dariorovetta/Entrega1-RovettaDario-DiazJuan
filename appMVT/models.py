from asyncio.windows_events import NULL
from django.db import models
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
        return f"Titulo: {self.titulo} - Subtitulo: {self.subtitulo} - Autor: {self.autor} - Fecha de creacion: {self.fechaCreacion}"

    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    fechaCreacion = models.DateField(null=True)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    descripcion = RichTextField(null=True, blank=True)
