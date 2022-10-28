from django.urls import path
from appMVT import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),  # Esta es nuestra primer view

    path('leerFamiliares', views.leerFamiliares, name="LeerFamiliares"),
    path('crearFamiliares', views.crearFamiliares, name="CrearFamiliares"),
    path('editarFamiliar/<id>/', views.editarFamiliar, name="EditarFamiliar"),
    path('eliminarFamiliar/<id>/', views.eliminarFamiliar, name="EliminarFamiliar"),

    path('busquedaApellido', views.busquedaApellido, name="BusquedaApellido"),
    path('buscar/', views.buscar),

    path('about', views.about, name="About"),


    # Clases basadas en Vistas (Familiares)
    path('familiares/list', views.FamiliarList.as_view(), name='Ver'),
    path('familiar/crear/', views.FamiliarCreacion.as_view(), name='Crear'),
    path('familiar/editar/<int:pk>', views.FamiliarUpdate.as_view(), name='Editar'),
    path('familiar/borrar/<int:pk>', views.FamiliarDelete.as_view(), name='Borrar'),
    path('familiar/detalle/<int:pk>',
         views.FamiliarDetalle.as_view(), name='Detallar'),

    # Clases basadas en Vistas (Blog Familiares)
    path('blogfamiliar/ver', views.FamiliarList.as_view(), name='Ver'),
    path('blogfamiliar/crear/', views.CrearBlogFamiliar.as_view(),
         name='CrearBlogFamiliar'),
    path('blogfamiliar/editar/<int:pk>',
         views.FamiliarUpdate.as_view(), name='Editar'),
    path('blogfamiliar/borrar/<int:pk>',
         views.FamiliarDelete.as_view(), name='Borrar'),
    path('blogfamiliar/detalle/<int:pk>',
         views.FamiliarDetalle.as_view(), name='Detallar'),


]
