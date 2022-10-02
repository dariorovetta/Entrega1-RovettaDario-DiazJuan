from django.http import HttpResponse
from django.template import loader

from appMVT.models import Familiar
import datetime


# Funcion para crear familiar
def crearFamiliar(request, nombre, apellido, edad):

    familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad, fechaCreacion=datetime.datetime.now())

    familiar.save()  # Para que la persona se guarde en la base de datos.

    plantilla = loader.get_template("crearFamiliar.html")
    renderizado = plantilla.render({"familiares": familiar})

    return HttpResponse(renderizado)

# Funcion para ver los familiares creados
def verFamiliares(request):

    familiares = Familiar.objects.all()

    plantilla = loader.get_template("verFamiliares.html")
    renderizado = plantilla.render({"familiares": familiares})

    return HttpResponse(renderizado)
    