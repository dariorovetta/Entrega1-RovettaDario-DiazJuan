from django.contrib import admin
from django.urls import path, include

# Para las imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('appMVT.urls')),
    path('accounts/', include('accounts.urls')),
    path('appChats/', include("appChats.urls")),
    path('admin/', admin.site.urls, name="Admin"),
]

# Para las imagenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
