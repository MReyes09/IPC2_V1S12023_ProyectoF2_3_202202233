from django.shortcuts import render

from gestionar_usuarios.estructura_lista.listaUsuario import ListaUser

# Create your views here.
lista: ListaUser = ListaUser()


def getListaUsers() -> ListaUser:

    if lista is None:
        lista.CargarXML()
        return lista
    return lista

def menuUserCliente(request):

    return render(request, 'menuUser.html')