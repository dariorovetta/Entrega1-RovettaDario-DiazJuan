
from django.urls import path, include
from appChats import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("chat/", chat_views.chatPage, name="chat-page"),

    # login-section
    path("auth/login/", LoginView.as_view(template_name="appChats/LoginPage.html"),
         name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
