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


        lista_categorias = []

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

    def actualiar_XML(self):

        global lista_categorias
        root = ET.Element("categorias")

        for categoria in lista_categorias:
            nueva_categoria = ET.SubElement(root, "categoria")

            nombre = ET.SubElement(nueva_categoria, "nombre")
            nombre.text = categoria.get_NombreCa()

            peliculas = ET.SubElement(nueva_categoria, "peliculas")

            if categoria.get_Peliculas() is not None:
                lista_peliculas = categoria.get_Peliculas()

                nodo_actual:NodoPelicula = lista_peliculas.cabeza

                while nodo_actual is not None:
                    pelicula = nodo_actual.pelicula
                    nueva_pelicula = ET.SubElement(peliculas, "pelicula")

                    titulo = ET.SubElement(nueva_pelicula, "titulo")
                    titulo.text = pelicula.get_titulo()

                    director = ET.SubElement(nueva_pelicula, "director")
                    director.text = pelicula.get_director()

                    anio = ET.SubElement(nueva_pelicula, "anio")
                    anio.text = str(pelicula.get_anio())

                    fecha = ET.SubElement(nueva_pelicula, "fecha")
                    fecha.text = pelicula.get_fecha()

                    hora = ET.SubElement(nueva_pelicula, "hora")
                    hora.text = pelicula.get_hora()

                    imagen = ET.SubElement(nueva_pelicula, "imagen")
                    imagen.text = pelicula.get_imagen()

                    precio = ET.SubElement(nueva_pelicula, "precio")
                    precio.text = str(pelicula.get_precio())

                    if nodo_actual.siguiente == lista_peliculas.cabeza:
                        break
                    else: nodo_actual = nodo_actual.siguiente

        xml_str = ET.tostring(root, encoding="utf-8")
        dom = minidom.parseString(xml_str)
        with open("dataXML/categorias.xml", "w") as archivo:
            archivo.write(dom.toprettyxml(indent="   "))

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

    def agregar_Categoria(self, nombre:str):

        global lista_categorias

        add_Cate:Categoria = Categoria(nombre)
        lista_categorias.append(add_Cate)

    def eliminar_Categoria(self, nombre:str):

        global lista_categorias

        index = 0
        for categoria in lista_categorias:

            if categoria.nombreCa == nombre:

                del lista_categorias[index]
            else:

                index += 1

    def agregar_Pelicula(self, nombreCa, peli_nueva:Pelicula):

        global lista_categorias

        index = 0

        for categoria in lista_categorias:

            if categoria.nombreCa == nombreCa:

                lista_Actualizada:ListaPelicula = categoria.peliculas

                if lista_Actualizada:
                    
                    lista_Actualizada.add_Pelicula(peli_nueva)
                    categoria.set_Peliculas(lista_Actualizada)

                    lista_categorias[index] = categoria
                    return
                
                else:

                    lista_Nueva:ListaPelicula = ListaPelicula()
                    lista_Nueva.add_Pelicula(peli_nueva)
                    categoria.set_Peliculas(lista_Nueva)

                    lista_categorias[index] = categoria
                    return
            
            index += 1

    def actualizar_Categoria(self, nombreCa:str, nombreCa_New:str, titulo:str, pelicula_ac, opcion:int):

        global lista_categorias

        index = 0
        for categoria in lista_categorias:

            if categoria.nombreCa == nombreCa:

                if opcion == 1:

                    categoria.set_NombreCa(nombreCa_New)
                    lista_categorias[index] = categoria
                    return lista_categorias
                
                elif opcion ==2:

                    categoria.peliculas.actualizar_Pelicula(titulo, pelicula_ac)
                    lista_categorias[index] = categoria
                    return lista_categorias

            else:

                index += 1 

    def eliminar_Pel(self, nombre:str, titulo:str):

        global lista_categorias

        index = 0
        for categoria in lista_categorias:

            if categoria.nombreCa == nombre:

                categoria.peliculas.eliminar_Pelicula(titulo)
                lista_categorias[index] = categoria                

            else:

                index += 1