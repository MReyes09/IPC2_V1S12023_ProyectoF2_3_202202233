from django.shortcuts import render

from gestionar_usuarios.estructura_lista.listaUsuario import ListaUser
from gestionar_usuarios.modelos.usuario import Usuario
from gestionar_categorias.views import getListaCategoria

# Create your views here.
lista: ListaUser = ListaUser()
listaCategorias = getListaCategoria()
userLoged:Usuario = None

def getListaUsers() -> ListaUser:
    global lista
    if lista.cabeza is None:
        lista.CargarXML()
        return lista
    return lista

def setListaUsers(listaUsers):
    global lista

    lista = listaUsers

def menuUserCliente(request):

    global listaCategorias
    global userLoged

    userLoged = lista.get_UserLoged()

    if request.method == 'GET' and 'categoria' in request.GET:
        
        categoria_seleccionada:str = request.GET.get('categoria')
        return render(request, 'menuUser.html', {'lista_Categorias': listaCategorias, 'userLoged': userLoged, 'categoria_Seleccionada': categoria_seleccionada,})
    
    elif request.method == "POST" :

        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')

        print(f"\n titulo: {titulo}\n categoria: {categoria}\n")

        # return render(request, 'menuUser.html', {'lista_Categorias': listaCategorias, 'userLoged': userLoged, 'categoria_Seleccionada': categoria_seleccionada})

    categoria_seleccionada = "General"
    return render(request, 'menuUser.html', {'lista_Categorias': listaCategorias, 'userLoged': userLoged, 'categoria_Seleccionada': categoria_seleccionada,})