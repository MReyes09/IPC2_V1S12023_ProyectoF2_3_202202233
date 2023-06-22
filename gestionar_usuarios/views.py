from django.shortcuts import render

from gestionar_usuarios.estructura_lista.listaUsuario import ListaUser
from gestionar_usuarios.modelos.usuario import Usuario
from gestionar_categorias.views import getListaCategoria
from gestionar_categorias.estructura_lista.lista_Pelicula import ListaPelicula
from gestionar_categorias.modelos.peliculas import Pelicula

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
    mi_Fav:ListaPelicula = userLoged.get_peliFav()

    if request.method == 'GET' and 'categoria' in request.GET:
        
        categoria_seleccionada:str = request.GET.get('categoria')
        return render(request, 'menuUser.html', {'Mi_Fav': mi_Fav, 'lista_Categorias': listaCategorias, 'userLoged': userLoged, 'categoria_Seleccionada': categoria_seleccionada,})
    
    elif request.method == "POST" :

        titulo = request.POST.get('titulo')
        nomCategoria = request.POST.get('categoria')

        if userLoged.get_peliFav():
            
            for categoria in listaCategorias:

                if categoria.get_NombreCa() == nomCategoria:
                    lista_Peliculas:ListaPelicula = categoria.get_Peliculas()
                    findedPelicula:Pelicula = lista_Peliculas.buscar_Pelicula(lista_Peliculas, titulo)
                    my_List:ListaPelicula = userLoged.get_peliFav()
                    my_List.add_Pelicula(findedPelicula)
                    userLoged.set_peliFav(my_List)
                    lista.actualizar_Usuario(userLoged)
                    categoria_seleccionada = "General"

                    return render(request, 'menuUser.html', {'Mi_Fav': mi_Fav, 'lista_Categorias': listaCategorias, 'userLoged': userLoged, 'categoria_Seleccionada': categoria_seleccionada,})

        else: 

            lista_Nueva: ListaPelicula = ListaPelicula()

            for categoria in listaCategorias:

                if categoria.get_NombreCa() == nomCategoria:

                    lista_Peliculas:ListaPelicula = categoria.get_Peliculas()
                    findedPelicula:Pelicula = lista_Peliculas.buscar_Pelicula(lista_Peliculas, titulo)
                    lista_Nueva.add_Pelicula(findedPelicula)                    
                    userLoged.set_peliFav(lista_Nueva)
                    lista.actualizar_Usuario(userLoged)
                    categoria_seleccionada = "General"

                    return render(request, 'menuUser.html', {'Mi_Fav': mi_Fav, 'lista_Categorias': listaCategorias, 'userLoged': userLoged, 'categoria_Seleccionada': categoria_seleccionada,})
                
    categoria_seleccionada = "General"
    return render(request, 'menuUser.html', {'Mi_Fav': mi_Fav, 'lista_Categorias': listaCategorias, 'userLoged': userLoged, 'categoria_Seleccionada': categoria_seleccionada,})