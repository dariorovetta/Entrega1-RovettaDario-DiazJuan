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
         