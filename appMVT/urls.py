from django.urls import path
from appMVT import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),  # Esta es nuestra primer view
    path('familiares', views.familiares, name="Familiares"),

    path('busquedaApellido', views.busquedaApellido, name="BusquedaApellido"),
    path('buscar/', views.buscar),
    
    path('about', views.about, name="About"),

]

