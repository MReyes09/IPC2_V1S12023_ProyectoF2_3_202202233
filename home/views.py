from django.shortcuts import render, redirect
from django.contrib import messages

from gestionar_usuarios.estructura_lista.listaUsuario import ListaUser
from gestionar_usuarios.views import getListaUsers, setListaUsers
from gestionar_categorias.views import getListaCategoria
from gestionar_categorias.estructura_lista.categoriaCotroller import categoriaController

# Create your views here.
# https://mdbootstrap.com/docs/standard/forms/overview/ CSS CHILERo
# https://bootsnipp.com/forms
categoriaControl = categoriaController()

listaUsuarios: ListaUser = ListaUser()
listaUsuarios = getListaUsers()

def Home(request):
    
    listaCategorias = getListaCategoria()
    global listaUsuarios
    
    if request.method == 'POST':

        nombre:str = request.POST.get('nombre')
        apellido: str = request.POST.get('apellido')
        telefono:int = request.POST.get('telefono')                
        correo:str = request.POST.get('correo')
        contrasena:str = request.POST.get('contrasena')

        if nombre == None:
            usuario = listaUsuarios.Iniciar_Sesion(correo, contrasena)
            if usuario:
                if usuario.get_rol() == "cliente":
                    messages.success(request, 'Sesión iniciada correctamente!!!')
                    setListaUsers(listaUsuarios)
                    return redirect('userHome')
                elif usuario.get_rol() == "administrador":
                    messages.success(request, 'Sesión iniciada correctamente!!!')
                    setListaUsers(listaUsuarios)
                    return redirect('userAdmin')
            else:
                messages.warning(request, 'No se encontró ninguna coincidencia.')

        else:

            rol:str = "cliente"
            listaUsuarios.Registrarse(rol, nombre, apellido, telefono, correo, contrasena)
            setListaUsers(listaUsuarios)
            listaUsuarios.Listar_Usuarios()
            messages.success(request, 'Se ha registrado el usuario con éxito')

    elif request.method == 'GET' and 'categoria' in request.GET:

        categoria_seleccionada:str = request.GET.get('categoria')
        return render(request, "Home.html", {'lista_Categorias': listaCategorias, 'categoria_Seleccionada': categoria_seleccionada})
    
    categoria_seleccionada = "General"
    return render(request, "Home.html", {'lista_Categorias': listaCategorias, 'categoria_Seleccionada': categoria_seleccionada})