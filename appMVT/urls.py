from django.urls import path
from appMVT import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),  # Esta es nuestra primer view
    path('crearFamiliares', views.crearFamiliares, name="crearFamiliares"),

    path('busquedaApellido', views.busquedaApellido, name="BusquedaApellido"),
    path('buscar/', views.buscar),
    
    path('about', views.about, name="About"),
    
    path('leerFamiliares', views.leerFamiliares, name="LeerFamiliares"),
    
    path('eliminarFamiliar/<id>/', views.eliminarFamiliar, name="EliminarFamiliar"),
    path('editarFamiliar/<id>/', views.editarFamiliar, name="EditarFamiliar"),
    
    path('familiares/list', views.FamiliarList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.FamiliarDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.FamiliarCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.FamiliarUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.FamiliarDelete.as_view(), name='Delete'),
    
    path('login/', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    
    path('logout', LogoutView.as_view(template_name='appMVT/logout.html'), name='Logout'),
    
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),
    

]

