
from django.contrib import admin
from django.urls import path

from home.views import Home
from gestionar_usuarios.views import menuUserCliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home, name = "Home"),
    path('home/userHome/', menuUserCliente, name = "userHome"),
]