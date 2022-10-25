# Importar lo necesario
from django.http import HttpResponse
from django.shortcuts import redirect, render
from appMVT.forms import FamiliarFormulario
from appMVT.models import Familiar

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from django.views.generic.detail import DetailView

# Vista de Inicio
@login_required
def inicio(request):

      return render(request, "appMVT/inicio.html")

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

# ListView --> Nos permite ver todos los familiares
# Al tener "LoginRequiredMixin", se necesita iniciar secion para que funcione
class FamiliarList(ListView):
      
      model = Familiar
      template_name = "appMVT/familiares_list.html"
      
# DetailView --> Para ver el detalle
class FamiliarDetalle(DetailView):
      
      model = Familiar
      template_name = "appMVT/familiar_detalle.html"
      
# CreateView --> Para crear
class FamiliarCreacion(LoginRequiredMixin, CreateView):
      
      model = Familiar
      success_url = "/familiares/list"
      template_name = "appMVT/familiar_form.html"
      fields = ['nombre', 'apellido', 'edad', 'fechaNacimiento']
      
# UpdateView --> Para editar
class FamiliarUpdate(UpdateView):
      
      model = Familiar
      success_url = "/familiares/list"
      template_name = "appMVT/familiar_form.html"
      fields = ['nombre', 'apellido', 'edad', 'fechaNacimiento']
      
# DeleteView --> Para eliminar
class FamiliarDelete(DeleteView):
      
      model = Familiar
      template_name = "appMVT/familiar_confirm_delete.html"
      success_url = "/familiares/list"

