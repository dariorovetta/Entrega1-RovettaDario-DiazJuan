from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('perfil/', views.perfil, name='Perfil'),
    path('perfil/editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('perfil/cambiarContrasenia', views.CambiarContrasenia.as_view(), name='CambiarContrasenia'),
]
