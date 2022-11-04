from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}


class UserEditForm(forms.Form):
    # Especificar los campos
    email = forms.EmailField(label="Modificar E-mail")
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)
    descripcion = forms.CharField(label='Descripción')
    red_social = forms.CharField(label='Red Social')


class MiCambioDePassword(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña vieja', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Contraseña nueva', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repetir Contraseña nueva', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {key: '' for key in fields}
