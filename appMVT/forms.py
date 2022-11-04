from django import forms
from ckeditor.fields import RichTextFormField
from django.contrib.auth.models import User

class FamiliarFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fechaNacimiento = forms.DateField()


class FormBlogFamiliar(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=30)
    autor = forms.CharField(max_length=30)
    fechaCreacion = forms.DateField()
    descripcion = RichTextFormField(required=False)


class BusquedaBlogFamilar(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)


class BusquedaFamilar(forms.Form):
    apellido = forms.CharField(max_length=30, required=False)
