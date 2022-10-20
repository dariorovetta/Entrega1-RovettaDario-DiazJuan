from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
    
class FamiliarFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fechaNacimiento = forms.DateField()
    

class UserRegisterForm(UserCreationForm):
     
     email = forms.EmailField()
     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
     
     class Meta:
         model = User
         fields = ['username', 'email', 'password1', 'password2'] 
         #Saca los mensajes de ayuda
         help_texts = {k:"" for k in fields}
         
        
class UserEditForm(UserCreationForm):
     
     # Aca se definen las opciones que queres modificar del usuario. Ponemos las basicas.
     email = forms.EmailField(label="Modificar E-mail")
     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
     password1 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
     
     last_name = forms.CharField(label='Apellido')
     first_name = forms.CharField(label='Nombre')
     
     class Meta:
         model = User
         fields = ['email', 'password1', 'password2', 'last_name', 'first_name'] 
         #Saca los mensajes de ayuda
         help_texts = {k:"" for k in fields}


class AvatarFormulario(forms.Form):

    #Especificar los campos
    
    imagen = forms.ImageField(required=True)