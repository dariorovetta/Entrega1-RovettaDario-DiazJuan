from django.urls import path
from appMVT import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),  # Esta es nuestra primer view
    path('crearFamiliares', views.crearFamiliares, name="crearFamiliares"),

    path('busquedaApellido', views.busquedaApellido, name="BusquedaApellido"),
    path('buscar/', views.buscar),
    
    path('about', views.about, name="About"),
    
    path('leerFamiliares', views.leerFamiliares, name="LeerFamiliares"),
    
    path('eliminarFamiliar/<id>/', views.eliminarFamiliar, name="EliminarFamiliar"),
    path('editarFamiliar/<id>/', views.editarFamiliar, name="EditarFamiliar"),

]

