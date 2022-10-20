# Importar lo necesario
from typing import List
from django.shortcuts import redirect, render, HttpResponse
from appMVT.forms import *
from .models import *
from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Para el Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Decorador por defecto
from django.contrib.auth.decorators import login_required


# Vista de Inicio
@login_required
def inicio(request):
      
      avatares = Avatar.objects.filter(user=request.user.id)

      return render(request, "appMVT/inicio.html", {"url":avatares[3].imagen.url})

# Vista de About
def about(request):

      return render(request, "appMVT/about.html")
  
# Vista de los Familiares
def crearFamiliares(request):
      
      if request.method == 'POST':
            
            miFormulario = FamiliarFormulario(request.POST)  # Aqui me llega toda la informacion del html
            
            print(miFormulario)
            
            if miFormulario.is_valid():  # Si paso la validacion de Django
            
                  informacion = miFormulario.cleaned_data
      
                  familiar = Familiar(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                      edad=informacion['edad'], fechaNacimiento=informacion['fechaNacimiento'])
            
                  familiar.save()
            
                  return render(request, "appMVT/inicio.html")  # Vuelvo al inicio o a donde quiera
      
      else:
            miFormulario = FamiliarFormulario()  # Formulario vacio para construir el html
      
      return render(request, "appMVT/familiares.html", {"miFormulario":miFormulario})
      


# Crear vista de Buscar Camadas
def busquedaApellido(request):
      
      return render(request, "appMVT/busquedaApellido.html")

# Crear vista de Busqueda
def buscar(request):
      
      if request.GET["apellido"]:
            
            apellido = request.GET['apellido']
            familiares = Familiar.objects.filter(apellido__icontains=apellido)
            
            return render(request, "appMVT/busquedaApellido.html", {"familiares":familiares, "apellido":apellido})
      
      else:
            
            respuesta = "No enviaste datos"
      
      # return
      return render(request, "appMVT/busquedaApellido.html", {"respuesta":respuesta})


# Leer Familiares
def leerFamiliares(request):
      
      familiares = Familiar.objects.all()  # Trae todos los profesores
      
      contexto = {"familiares":familiares}
      
      return render(request, "appMVT/leerFamiliares.html", contexto)


# Eliminar un familiar

def eliminarFamiliar(request, id):
      
      familiar = Familiar.objects.get(id=id)
      familiar.delete()
      
      # Vuelvo al menu
      familiares = Familiar.objects.all()  # Trae todos los familiares
      
      contexto = {"familiares":familiares}
      
      return render(request, "appMVT/leerFamiliares.html",contexto)


# Editar Familiar

def editarFamiliar(request, id):
      
      # Recibe el nombre del familiar que vamos a modificar
      familiar = Familiar.objects.get(id=id)
      
      # Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            
            miFormulario = FamiliarFormulario(request.POST)  # Aqui me llega toda la informacion del html
            
            print(miFormulario)
            
            if miFormulario.is_valid():  # Si paso la validacion de Django
            
                  informacion = miFormulario.cleaned_data
      
                  familiar.nombre=informacion['nombre']
                  familiar.apellido=informacion['apellido']
                  familiar.edad=informacion['edad']
                  familiar.fechaNacimiento=informacion['fechaNacimiento']
            
                  familiar.save()
            
                  return render(request, "appMVT/inicio.html")  # Vuelvo al inicio o a donde quiera
      
      # En caso de que no sea POST
      else:
            # Creo el formulario con los datos que voy a modificar
            miFormulario = FamiliarFormulario(initial={'nombre': familiar.nombre, 'apellido': familiar.apellido,
                  'edad': familiar.edad, 'fechaNacimiento': familiar.fechaNacimiento})  
            
      # Voy al html que me permite editar
      return render(request, "appMVT/editarFamiliar.html", {"miFormulario":miFormulario, "id": id})
      
      
# Clases basadas en vistas

# ListView --> Nos permite ver todos los cursos
# Al tener "LoginRequiredMixin", se necesita iniciar secion para que funcione
class FamiliarList(LoginRequiredMixin, ListView):
      
      model = Familiar
      template_name = "appMVT/familiares_list.html"
      login_url = "/login/"
      redirect_field_name = ""
      
      
# DetailView --> Para ver el detalle
class FamiliarDetalle(DetailView):
      
      model = Familiar
      template_name = "appMVT/familiar_detalle.html"
      
# CreateView --> Para crear
class FamiliarCreacion(CreateView):
      
      model = Familiar
      success_url = "/familiares/list"
      fields = ['nombre', 'apellido', 'edad', 'fechaNacimiento']
      
# UpdateView --> Para editar
class FamiliarUpdate(UpdateView):
      
      model = Familiar
      success_url = "/familiares/list"
      fields = ['nombre', 'apellido', 'edad', 'fechaNacimiento']
      
# DeleteView --> Para eliminar
class FamiliarDelete(DeleteView):
      
      model = Familiar
      success_url = "/familiares/list"
      

# Vista del login
def login_request(request):
      
      if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST) 
            
            if form.is_valid(): 
            
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
                  
                  user = authenticate(username=usuario, password=contra)
                  
                  if user is not None:
                        login(request, user)
                        
                        return render(request, "appMVT/inicio.html", {"mensaje":f"¡Bienvenido! {usuario}"})
                  else:
                        return render(request, "appMVT/inicio.html", {"mensaje":"Error, datos incorrectos"})
      
            else:
                  return render(request, "appMVT/inicio.html", {"mensaje":"Error, formulario erroneo"})
      
      form = AuthenticationForm()
      
      return render(request, "appMVT/login.html", {'form':form})


# Vista para crear usuario
def register(request):
      if request.method == 'POST':
            
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():
                  
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request, "appMVT/inicio.html", {"mensaje":"Usuario Creado :)"})
            
      else:
            #form = UserCreationForm()
            form = UserRegisterForm()
            
      return render(request, "appMVT/registro.html", {"form":form})


@login_required
def editarPerfil(request):
      
      # Instancia del login
      usuario = request.user
      
      # Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            
            miFormulario = UserEditForm(request.POST)
            
            if miFormulario.is_valid():
                  
                  informacion = miFormulario.cleaned_data
                  
                  # Datos que se modificaran
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
                  
                  return render(request, "appMVT/inicio.html")  # Vuelvo al inicio
            
      # En caso de que no sea post
      else:
            # Creo el formulario con lo datos que voy a modificar
            miFormulario = UserEditForm(initial={'email':usuario.email})
            
      # Voy al html que me permite editar
      return render(request, "appMVT/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})


@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES)  # Aquí me llega toda la información del html

            if miFormulario.is_valid():  # Si pasó la validación de Django


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "appMVT/inicio.html")  # Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AvatarFormulario()  # Formulario vacio para construir el html

      return render(request, "appMVT/agregarAvatar.html", {"miFormulario":miFormulario})