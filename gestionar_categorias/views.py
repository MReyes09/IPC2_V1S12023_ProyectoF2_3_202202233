from django.shortcuts import render

from gestionar_categorias.estructura_lista.categoriaCotroller import categoriaController

# Create your views here.

categoriaControl = categoriaController()
lista_Categorias = []

def getListaCategoria() -> []:
    global lista_Categorias
    if len(lista_Categorias) > 0:
        return lista_Categorias
    else:
        lista_Categorias = categoriaControl.CargarXML_Category()

    return lista_Categorias