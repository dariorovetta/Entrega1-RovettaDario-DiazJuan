Pasos para crear el MVT
1.-  Creamos una carpeta (para el proyecto)
2.-  Entramos a la carpeta desde la terminal (para indicar la ruta: cd nombre del proyecto)   o desde el menú 
3.-  Aplicamos desde la terminal $ "code -r .  para que abra la nueva carpeta
4.-  Creamos un entorno virtual con $  "python -m venv <nombre entorno virtual>"
5.-  Activamos el entorno virtual con: $. <nombre entorno virtual>/Scripts/activate
6.-  Inicializar GIT con $ git init
7.- Conectar mi repositorio con la nube de GitHub 
a.- Verificar el estado con $ git status
b.- Agregar los archivos con $ git add .
c.- Agregar un commit a los archivos con $ git commit -m <mensaje>
d.- Verificar si se hizo el commit con $ git log --oneline
e.- Copiar los comandos de la pagina GitHub (Copiar comandos de la nube)
$ git remote add origin  xxxxxx   / $ git branch -M main  / $ git push -u origin main
8.-  Instalar Django con $ pip install Django
9. Cargamos en entorno virtual ($ . <nombre entorno virtual>/Scripts/actívate
10.- Iniciar el proyecto Django con $ django-admin startproject <nombredeproyecto>
11. Sacamos el archivo manage.py del directorio actual y lo movemos a la raíz a la altura de donde esta la carpeta de venv
12. renombramos la carpeta creada en el paso 10, sacamos la otra carpeta que esta adentro a la raíz y borramos la carpeta renombrada. 
13.- Probamos si Django se instalo y creamos un archivo con el nombre: requirements.txt ejecutando:  $ pip freeze > requirements.txt (colocamos el símbolo >), corroboramos que se haya creado el archivo en el directorio.
<PROYECTO>
| -> <proyectoxxxx>
| -> manage.py
| -> .gitignore
| -> requirements.txt
	11.- Probar si nuestro proyecto funciona con  $ python manage.py runserver
	12 .- Agregamos al archivo .girignore (venv, __pycache__, db.sqlite3)
	12.- Generar la base de datos con la configuración de django con $ python manage.py migrate
	
	13.- Crear una vista con el nombre "views.py" en la carpeta de nuestro proyecto
	a.- Dentro de la vista crear las funciones que necesitamos
	b.- Como las vistas se ejecutan con cargadores hay que agregar la ruta de las plantillas en "settings.py"
	14.- En el archivo "urls.py" tenemos que agregar las vistas que queremos ver
	15.- Crear una app dentro del proyecto con "python manage.py startapp <nombreapp>"
	a.- Dentro de la app en el archivo "models.py" crear la clase "Familiar"
	b.- Agregarnos nuestra app en el archivo "settings.py"
	c.- Verificar si esta todo bien con "python manage.py check appMVT"
	d.- Convertimos nuestros modelos en BD con "python manage.py makemigrations"
	e.- Migrar los datos con "python manage.py migrate"
	16.- Crear los familiares pedidos por la URL y verlos por la otra URL.
	17.- Aplicar cambio en GIT con "git add ."
	18.- Hacer un commit en GitHub con "git commit -m <comentario>"
	19.- Aplicamos los cambios en el repertorio web con "git push origin main"

Para crear una aplicación
Python manage.py startapp (nombre de la aplicación) home
Se crea una carpeta con varios archivos (indicando que se va a estar trabajando como con paquetes)
El modelo es el esqueto que determina como va a estar trabajando la información/ viene relacionado directamente con la relación de la base de datos

El archivo models es como una clase pero tiene la relación con la base de datos

Para crear un modelo:

class Perrsona(models.Model):
nombre = models.CharField(max_length=30)
apellido= models.CharField(max_length=30)
edad = models.IntegerField()

Ahora tengo que decirle a mi base de datos sepa que cree este modelo:
Primero debo ir al archivo de settings.py en la carpeta proyecto, e incorporar en:
INSTALLED_APPS = [
agregar: home
]
Luego seguimos:
$ python manage.py makemigrations
Es recomendable tener instalada la extensión: SQLite Viewer de Florian Klampfer
$ python manage.py migrate (se crea la BD y chicleando encima podemos ver el contenido)
 Si realizo alguna modificación a la BD por ejemplo le agrego:
fecha_nacimiento = models.DateField()
tenemos que volver a actualizar con:
$ python manage.py makemigrations
Si me genera un mensaje de advertencia seleccionamos modificar manualmente el archivo models.py y le agregamos:
fecha_nacimiento = models.DateField(null=True)
y volvemos a ejecutar el comando
$ python manage.py makemigrations
Luego:
$ python manage.py migrate


{% for persona in personas%}
<li> {{persona}}</li>
{% endfor %}

Para traer personas de la BD tenemos que ver que lo importe:
from home.models import Persona (en la parte superior del archivo)
después creamos la vista
def crear_persona(request, nombre, apellido):
	persona = DatosPersonales(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    	template = loader.get_template('ver_persona.html')
    	template_renderizado = template.render({‘personas’: personas})
	return HttpResponse(´´)

def ver_persona(request):
	persona = Persona.objects.all()		#Persona es la BD, trae todos los objetos de la BD
    	template = loader.get_template('ver_persona.html')
    	template_renderizado = template.render({‘personas’: personas})
	return HttpResponse(template_renderizado)



Clase 19 19-A
Agregamos RENDER a la vista (al inicio)
from django.shortcuts import render

Luego modificamos en este caso la vista:
def crear_persona(request, nombre, apellido):
    persona = DatosPersonales(
        nombre=nombre, apellido=apellido, edad=random.randrange(1, 99))  # , fecha_nacimiento=datetime.now())
    persona.save()
    return render(request, 'crear_persona.html', {'persona': persona})

# def crear_persona(request, nombre, apellido):
#     persona = DatosPersonales(
#         nombre=nombre, apellido=apellido, edad=random.randrange(1, 99))  # , fecha_nacimiento=datetime.now())
#     persona.save()
#     template = loader.get_template('crear_persona.html')
#     template_renderizado = template.render({'persona': persona})
#     return HttpResponse(template_renderizado)

Ahora modificamos la URLS
Creamos en la aplicacion el archivo urls.py
Copiamos el contenido y lo modificamos así:
from django.contrib import admin
from django.urls import path
# from .views import hola  # *hace lo mismo que lalinea de abajo*

# from ..home import views *se puede borrar ya que lo modifique por la linea anterior*


urlpatterns = [
    path('admin/', admin.site.urls),
]
Y el URLS nuevo de la aplicación queda así:
from django.urls import path

from home import views

urlpatterns = [
    path('hola/', views.hola),
    path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento),
    path('mi-index/', views.mi_index),
    path('tu-template/<str:nombre>/', views.tu_template),
    path('prueba-template/', views.prueba_template),
    path('crear-persona/<str:nombre>/<str:apellido>/', views.crear_persona),
    path('crear-persona1/', views.crear_persona),
    path('ver-personas/', views.ver_personas),
]

Ahora para que mi nueva urls pueda ver su contenido, debemos colocar un include y quedaria así:

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
]

HERENCIA DE TEMPLATE


PASOS PARA CREAR UN USUARIO

$ python manage.py createsuperuser
Al ejecutar el comando pide que coloquemos el nombre del usuario (admin) y el password

Ahora hay que decirle a la parte de django que reconozca el modelo de persona como lo hacemos:
En el directorio de home, buscamos el archivo de admin.py y le agregamos:
from home.models import DatosPersonas (el nombre de la BD) 

admin.site.register(DatosPersonales)

después podemos entrar a la dirección y colocar el nombre admin, la contraseña.

Para que los datos se vean bien y no:
DatosPersonales object(3)
DatosPersonales object(2)
DatosPersonales object(1)

Vamos al archivo models.py y colocamos:
def __str__(self):
return f´{self.nombre} {self.apellido}´
y listo, actualizamos la pagina y nos debe aparecer:
Juan Diaz
Juan Diaz
Juan Diaz
En este caso así porque son los datos que están en la BD, pero solo es visualización, no genera cambios en la BD

Si realizamos cambios a los campos de la BD y al nombre de la class, es recomendable hacer primero un cambio, ejecutar makemigrations, realizar el cambio de la class y realizar otra vez makemigrations, y por ultimo migrate:
$ python manage.py makemigrations
$ python manage.py migrate
NOTA: cualquier cambio que se haga en class, hay que hacer un makemigratios y luego migrate
Para salir de la vista de admin, clicleamos en logout (parte superior derecha)

TRABAJANDO CON LA PAGINA DE BOOSTRAP

Primero ubicamos los anclas, agregamos los títulos que queremos incorporar a la pagina: 
<nav class="navbar navbar-light bg-light static-top">
            <div class="container">
                <a class="navbar-brand" href="#!">Home</a>
                <a class="navbar-brand" href="#!">Hola</a>
                <a class="navbar-brand" href="#!">Fecha</a>
                <a class="navbar-brand" href="#!">Ver personas</a>
                <a class="navbar-brand" href="#!">Mi template</a>
             <!--   <a class="btn btn-primary" href="#signup">Sign Up</a> -->
            </div>
        </nav>

Luego vamos a URLS.PY
Y le agregamos a urlpatterns = [
	path('', views.index), /// agregamos  path('', views.index, name=index´),
]

Y a cada uno lo cambiamos
urlpatterns = [
    path('', views.index),
    path('hola/', views.hola),
    path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento),
    path('mi-index/', views.mi_index),
    path('tu-template/<str:nombre>/', views.tu_template),
    path('prueba-template/', views.prueba_template),
    path('crear-persona/<str:nombre>/<str:apellido>/', views.crear_persona),
    path('crear-persona1/', views.crear_persona),
    path('ver-personas/', views.ver_personas),
]

Y queda asi:

urlpatterns = [
    path('', views.index, name='index'),
    path('hola/', views.hola, name='hola'),
    path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento,
         name='calcular_fecha_nacimiento'),
    path('mi-index/', views.mi_index, name='mi_index'),
    path('tu-template/<str:nombre>/', views.tu_template, name='tu_template'),
    path('prueba-template/', views.prueba_template, name='prueba_template'),
    path('crear-persona/<str:nombre>/<str:apellido>/',
         views.crear_persona, name='crear_persona'),
    path('crear-persona1/', views.crear_persona, name='crear_persona'),
    path('ver-personas/', views.ver_personas, name='ver_personas'),
]

Ahora transformamos el ancla para que tenga el formato adecuado de Python



HERENCIA

1ero Creamos un archivo base.html en home
2do colocamos lo que vamos a repetir en los demás tempates y lo llevamos al base.html, tomando en cuenta la etiqueta de cierre del </html> 


