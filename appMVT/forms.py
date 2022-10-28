from django import forms
from ckeditor.fields import RichTextFormField


class FamiliarFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fechaNacimiento = forms.DateField()


class BlogFamiliar(forms.Form):

    titulo = forms.CharField(max_length=30)
    sub_titulo = forms.CharField(max_length=30)
    descripcion = RichTextFormField(required=False)
    autor = forms.CharField(max_length=30)
    fechaCreacion = forms.DateField()
    imagen = forms.ImageField(upload_to='imagenes', null=True, blank=True)
