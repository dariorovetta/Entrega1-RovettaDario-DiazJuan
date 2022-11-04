from django.db import models
from django.contrib.auth.models import User

class ExtensionUsuario(models.Model):
    # Subcaperta avatares de media :)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=30, null=True)
    red_social = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"
