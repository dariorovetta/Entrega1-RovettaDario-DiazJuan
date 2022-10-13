# Importar lo necesario
from django.shortcuts import render
from appMVT.forms import *
from .models import *
from django.http import HttpResponse

# Vista de Inicio
def inicio(request):

      return render(request, "appMVT/inicio.html")

# Vista de About
def about(request):

      return render(request, "appMVT/about.html")
  
# Vista de los Familiares
def familiares(request):
      
      if request.method == 'POST':
            
            miFormulario = FamiliarFormulario(request.POST)  # Aqui me llega toda la informacion del html
            
            print(miFormulario)
            
            if miFormulario.is_valid:  # Si paso la validacion de Django
            
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
            
            # Respuesta respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }"
            apellido = request.GET['apellido']
            familiares = Familiar.objects.filter(apellido__icontains=apellido)
            
            return render(request, "appMVT/busquedaApellido.html", {"familiares":familiares, "apellido":apellido})
      
      else:
            
            respuesta = "No enviaste datos"
      
      # return HttpResponse(respuesta)
      return render(request, "appMVT/busquedaApellido.html", {"respuesta":respuesta})
