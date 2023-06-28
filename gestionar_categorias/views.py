from django.shortcuts import render, redirect
from django.contrib import messages

from gestionar_categorias.estructura_lista.categoriaCotroller import categoriaController
from gestionar_categorias.estructura_lista.CineController import CineController
from gestionar_categorias.modelos.categoria import Categoria
from gestionar_categorias.modelos.peliculas import Pelicula
from gestionar_categorias.modelos.Cine import Cine
from gestionar_categorias.modelos.Sala import Sala
from gestionar_categorias.estructura_lista.lista_Pelicula import ListaPelicula
from gestionar_categorias.estructura_lista.ListsaSala import ListaSala

# Create your views here.

categoriaControl = categoriaController()
cineControl = CineController()

lista_Categorias = []
lista_Cines = []

def getListaCategoria():
    global lista_Categorias
    return lista_Categorias
    
def setListaCategoria(lista):

    global lista_Categorias
    lista_Categorias = lista

def setListaCine(lista):
    global lista_Cines

    lista_Cines = lista

def getListaCine():
    global lista_Cines
    return lista_Cines

def actualizar_Ca(request, categoria:str, titulo:str):

    global lista_Categorias
    global categoriaControl

    categoria_HTML:Categoria = None
    pelicula_HTML:Pelicula = None

    for categorias in lista_Categorias:

        if categorias.nombreCa == categoria:

            categoria_HTML = categorias

            if titulo != "Nada":
                
                lista_Buscar:ListaPelicula = ListaPelicula()
                pelicula_HTML = lista_Buscar.buscar_Pelicula(categorias.peliculas, titulo)

    if request.method == "POST":

        if pelicula_HTML:

            nombreCa:str = categoria_HTML.get_NombreCa()
            titulo_Pel:str = request.POST.get('titulo')
            director:str = request.POST.get('director')
            anio:int = int(request.POST.get('anio'))
            fecha:str = request.POST.get('fecha')
            hora:str = request.POST.get('hora')
            imagen:str = request.POST.get('imagen')
            precio:int = request.POST.get('precio')

            titulo_B:str = pelicula_HTML.get_titulo()

            pelicula_Ac:Pelicula = Pelicula(titulo_Pel, director, anio, fecha, hora, imagen, precio)

            lista = categoriaControl.actualizar_Categoria(nombreCa, None, titulo_B, pelicula_Ac, 2)
            setListaCategoria(lista)
            messages.success(request, 'Se ha actualizado la pelicula con éxito')
            return redirect('userAdmin')
        
        else: 

            nombreCa:str = categoria_HTML.get_NombreCa()
            nombreCa_new:str = request.POST.get('nombreCa_New')

            lista = categoriaControl.actualizar_Categoria(nombreCa, nombreCa_new, None, None, 1)
            setListaCategoria(lista)
            messages.success(request, 'Se ha actualizado la categoria con éxito')
            return redirect('userAdmin')


    return render(request, 'actualizar_Cat.html', {'categoria': categoria_HTML, 'pelicula': pelicula_HTML})

def actualizar_Cine(request, nombre:str, numero:str):
    global lista_Cines
    global cineControl

    cine_HTML:Cine = None
    sala_HTML:Sala = None
    
    for cine in lista_Cines:

        if cine.get_nombre() == nombre:

            cine_HTML = cine

            if numero == "Nada":

                sala_HTML = None

            else:
                lista_Salas:ListaSala = cine_HTML.get_salas()
                sala_HTML = lista_Salas.buscar_Sala(numero, None, 1)  

    if request.method == "POST":

        if sala_HTML:

            nombre:str = request.POST.get('nombre')
            numero:str = request.POST.get('numero')
            asientos:int = int(request.POST.get('asientos'))

            sala_nueva:Sala = Sala(numero,asientos)

            lista = cineControl.modificar_Cine(nombre, None, sala_nueva, sala_HTML.get_numero(), 3)
            setListaCine(lista)
            messages.success(request, 'Se ha actualizado la Sala con éxito')
            return redirect('userAdmin')
        
        else:

            nombre:str = request.POST.get('nombre')
            nombre_new:str = request.POST.get('nombre_New')

            lista = cineControl.modificar_Cine(nombre, nombre_new, None, None, 1)
            setListaCine(lista)
            messages.success(request, 'Se ha actualizado el cine con éxito')
            return redirect('userAdmin')


    return render(request, 'actualizar_Cine.html', {'cine': cine_HTML, 'sala': sala_HTML,})