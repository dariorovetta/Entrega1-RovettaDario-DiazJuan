from django.db import models
from django.contrib.auth.models import User

# Create your models here.
   
class ExtensionUsuario(models.Model):
  # Subcaperta avatares de media :) 
  avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
  # Vinculo con el usuario
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  def __str__ (self):
    return f"Imagen de: {self.user.username}"