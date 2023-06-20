import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

from .lista_Pelicula import ListaPelicula
from ..modelos.categoria import Categoria
from ..modelos.peliculas import Pelicula
from .nodo_Pelicula import NodoPelicula


lista_categorias = []

class categoriaController():

    def CargarXML_Category(self):
        global lista_categorias


        if len(lista_categorias) > 0:
            lista_categorias.clear()

        with open('dataXML/categorias.xml', 'r', encoding='utf-8') as archivo:
            tree = ET.parse(archivo)
            root = tree.getroot()

            for categoria in root.findall('categoria'):

                lista_Pelicula: ListaPelicula = ListaPelicula()
                nombre: str = categoria.find('nombre').text

                for pelicula in categoria.findall("peliculas/pelicula"):

                    titulo: str = pelicula.find('titulo').text
                    director: str = pelicula.find('director').text
                    anio: int = int(pelicula.find('anio').text)
                    fecha: str = pelicula.find('fecha').text
                    hora: str = pelicula.find('hora').text
                    imagen: str = pelicula.find('imagen').text
                    precio: int = int(pelicula.find('precio').text)

                    cargar_Pelicula: Pelicula = Pelicula(
                        titulo, director, anio, fecha, hora,
                        imagen, precio
                    )

                    lista_Pelicula.add_Pelicula(cargar_Pelicula)

                cargar_Categoria: Categoria = Categoria(nombre, lista_Pelicula)                
                lista_categorias.append(cargar_Categoria)
        return lista_categorias

    def get_Lista_Categorias(self):

        global lista_categorias
        return lista_categorias
    
    def listar_Categorias(self):

        global lista_categorias

        if lista_categorias:

            for categoria in lista_categorias:

                print(f"Categoria: {categoria.get_NombreCa()}")

                if categoria.get_Peliculas():

                    categoria_Pelis: ListaPelicula = ListaPelicula()
                    categoria_Pelis.Listar_Peliculas(categoria.get_Peliculas())
                    print(" ")

                else: print("No tiene peliculas aun")

        else: print("lista vacia")

