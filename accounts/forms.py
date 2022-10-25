from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    
class UserRegisterForm(UserCreationForm):
     
     first_name = forms.CharField(label='Nombre')
     last_name = forms.CharField(label='Apellido')
     username = forms.CharField(label='Usuario')
     email = forms.EmailField()
     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
     password2 = forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput)
     avatar = forms.ImageField(required=False)
     
     class Meta:
         model = User
         fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'avatar'] 
         #Saca los mensajes de ayuda
         help_texts = {k:"" for k in fields}
        

class UserEditForm(forms.Form):
    #Especificar los campos
    email = forms.EmailField(label="Modificar E-mail")
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)