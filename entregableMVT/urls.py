from django.contrib import admin
from django.urls import path, include

# Para las imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name="Admin"),
    path('', include('appMVT.urls')),
    path('', include('accounts.urls')),
    path('', include("appChats.urls")),
]

# Para las imagenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
