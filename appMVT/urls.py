from django.urls import path
from appMVT import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),  # Esta es nuestra primer view
    path('familiares', views.familiares, name="Familiares"),

    #path('busquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    #path('buscar/', views.buscar),

]

