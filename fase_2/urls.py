
from django.contrib import admin
from django.urls import path

from home.views import Home
from gestionar_usuarios.views import menuUserCliente, compraBoletos, menuAdminCliente, actualizar_Usuario, actualizar_Ta
from gestionar_categorias.views import actualizar_Ca, actualizar_Cine

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home, name = "Home"),
    path('home/userHome/', menuUserCliente, name = "userHome"),
    path('home/userHome/compra_boleto/<str:titulo>/<str:categoria>/', compraBoletos, name="compra"),
    path('home/adminHome/', menuAdminCliente, name = "userAdmin"),
    path('home/adminHome/<str:correo>/', actualizar_Usuario, name="actualizar_U"),
    path('home/adminHome/<str:categoria>/<str:titulo>/', actualizar_Ca, name = "actualizar_C"),
    path('home/adminHome/<str:nombre>/<str:numero>/actualizar', actualizar_Cine, name="actualizar_Cine"),
    path('home/actualizar_Tarjeta/<int:numero>/', actualizar_Ta, name="actualizar_Tarjeta"),
]