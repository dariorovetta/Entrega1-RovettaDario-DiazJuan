# Importar lo necesario
from appMVT.forms import FamiliarFormulario, BusquedaBlogFamilar, BusquedaFamilar
from appMVT.models import Familiar, BlogFamiliar
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Vista de Inicio
def inicio(request):

    return render(request, "appMVT/inicio.html")

# Vista de About
def about(request):

    return render(request, "appMVT/about.html")

# Vista de los Familiares
def crearFamiliares(request):

    if request.method == 'POST':

        # Aqui me llega toda la informacion del html
        miFormulario = FamiliarFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():  # Si paso la validacion de Django

            informacion = miFormulario.cleaned_data

            familiar = Familiar(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                edad=informacion['edad'], fechaNacimiento=informacion['fechaNacimiento'])

            familiar.save()

            # Vuelvo al inicio o a donde quiera
            return render(request, "appMVT/inicio.html")

    else:
        miFormulario = FamiliarFormulario()  # Formulario vacio para construir el html

    return render(request, "appMVT/familiares.html", {"miFormulario": miFormulario})


# Leer Familiares
def leerFamiliares(request):

    familiares = Familiar.objects.all()  # Trae todos los familiares

    contexto = {"familiares": familiares}

    return render(request, "appMVT/leerFamiliares.html", contexto)


# Eliminar un familiar
def eliminarFamiliar(request, id):

    familiar = Familiar.objects.get(id=id)
    familiar.delete()

    # Vuelvo al menu
    familiares = Familiar.objects.all()  # Trae todos los familiares

    contexto = {"familiares": familiares}

    return render(request, "appMVT/leerFamiliares.html", contexto)


# Editar Familiar
def editarFamiliar(request, id):

    # Recibe el nombre del familiar que vamos a modificar
    familiar = Familiar.objects.get(id=id)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # Aqui me llega toda la informacion del html
        miFormulario = FamiliarFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():  # Si paso la validacion de Django

            informacion = miFormulario.cleaned_data

            familiar.nombre = informacion['nombre']
            familiar.apellido = informacion['apellido']
            familiar.edad = informacion['edad']
            familiar.fechaNacimiento = informacion['fechaNacimiento']

            familiar.save()

            # Vuelvo al inicio o a donde quiera
            return render(request, "appMVT/inicio.html")

    # En caso de que no sea POST
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = FamiliarFormulario(initial={'nombre': familiar.nombre, 'apellido': familiar.apellido,
                                                   'edad': familiar.edad, 'fechaNacimiento': familiar.fechaNacimiento})

    # Voy al html que me permite editar
    return render(request, "appMVT/editarFamiliar.html", {"miFormulario": miFormulario, "id": id})


# Clases basadas en vistas

# ListView --> Nos permite ver todos los familiares
class VerFamiliar(ListView):

    model = Familiar
    template_name = "appMVT/ver_familiares.html"

    def get_queryset(self):
        apellido = self.request.GET.get('apellido', '')
        if apellido:
            object_list = self.model.objects.filter(
                apellido__icontains=apellido)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaFamilar()
        return context


# DetailView --> Para ver el detalle
class DetalleFamiliar(DetailView):

    model = Familiar
    template_name = "appMVT/detalle_familiar.html"

# CreateView --> Para crear
# Al tener "LoginRequiredMixin", se necesita iniciar secion para que funcione
class FamiliarCreacion(LoginRequiredMixin, CreateView):

    model = Familiar
    success_url = "/familiares/ver"
    template_name = "appMVT/crear_familiar.html"
    fields = ['nombre', 'apellido', 'edad', 'fechaNacimiento']

# UpdateView --> Para editar
class EditarFamiliar(LoginRequiredMixin, UpdateView):

    model = Familiar
    success_url = "/familiares/ver"
    template_name = "appMVT/crear_familiar.html"
    fields = ['nombre', 'apellido', 'edad', 'fechaNacimiento']

# DeleteView --> Para eliminar
class EliminarFamiliar(LoginRequiredMixin, DeleteView):

    model = Familiar
    template_name = "appMVT/eliminar_familiar.html"
    success_url = "/familiares/ver"

# CreateView --> Para crear blog Familiar
class VerBlogFamiliar(ListView):

    model = BlogFamiliar
    template_name = "appMVT/ver_blogfamiliar.html"

    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            object_list = self.model.objects.filter(titulo__icontains=titulo)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaBlogFamilar()
        return context

# Crear blog familiar
class CrearBlogFamiliar(LoginRequiredMixin, CreateView):

    model = BlogFamiliar
    success_url = "/blogfamiliar/ver"
    template_name = "appMVT/crear_blogfamiliar.html"
    fields = ['titulo', 'subtitulo', 'autor',
              'fechaCreacion', 'imagen', 'descripcion']

# Editar blog familiar
class EditarBlogFamiliar(LoginRequiredMixin, UpdateView):

    model = BlogFamiliar
    success_url = "/blogfamiliar/ver"
    template_name = "appMVT/editar_blogfamiliar.html"
    fields = ['titulo', 'subtitulo', 'descripcion',
              'autor', 'fechaCreacion', 'imagen']

# Eliminar blog familiar
class EliminarBlogFamiliar(LoginRequiredMixin, DeleteView):

    model = BlogFamiliar
    success_url = "/blogfamiliar/ver"
    template_name = "appMVT/eliminar_blogfamiliar.html"

# Detallar blog familiar
class DetalleBlogFamiliar(DetailView):

    model = BlogFamiliar
    template_name = "appMVT/detalle_blogfamiliar.html"
    
    
@login_required
def video(request):

    return render(request, "appMVT/video.html")