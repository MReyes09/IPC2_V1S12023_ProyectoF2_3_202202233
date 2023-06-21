from django.shortcuts import render, redirect
from django.contrib import messages

from gestionar_usuarios.estructura_lista.listaUsuario import ListaUser
from gestionar_usuarios.views import getListaUsers
from gestionar_categorias.views import getListaCategoria
from gestionar_categorias.estructura_lista.categoriaCotroller import categoriaController

# Create your views here.
# https://mdbootstrap.com/docs/standard/forms/overview/ CSS CHILERo
# https://bootsnipp.com/forms
global listaCategorias
listaCategorias = getListaCategoria()
categoriaControl = categoriaController()

listaUsuarios: ListaUser = ListaUser()
listaUsuarios = getListaUsers()

def Home(request):
    if request.method == 'POST':

        nombre:str = request.POST.get('nombre')
        apellido: str = request.POST.get('apellido')
        telefono:int = request.POST.get('telefono')                
        correo:str = request.POST.get('correo')
        contrasena:str = request.POST.get('contrasena')

        if nombre == None:

            usuario = listaUsuarios.Iniciar_Sesion(correo, contrasena)
            if usuario:
                messages.success(request, 'Sesión iniciada correctamente!!!')
                return redirect('userHome')
            else:
                messages.warning(request, 'No se encontró ninguna coincidencia.')

        else:

            rol:str = "cliente"
            listaUsuarios.Registrarse(rol, nombre, apellido, telefono, correo, contrasena)
            listaUsuarios.Listar_Usuarios()
            messages.success(request, 'Se ha registrado el usuario con éxito')
    return render(request, "Home.html", {'lista_Categorias': listaCategorias})