from .nodo_Pelicula import NodoPelicula
from ..modelos.peliculas import Pelicula


class ListaPelicula:

    def __init__(self):

        self.cabeza: NodoPelicula = None
        self.cola: NodoPelicula = None

    def Listar_Peliculas(self, listaDePelis):

        actual: NodoPelicula = listaDePelis.cabeza

        if actual is None:
            print("No hay peliculas")
            return

        while True:

            print(f"Titulo: {actual.pelicula.get_titulo()} \n"
                  f"director: {actual.pelicula.get_director()}\n"
                  f"anio: {actual.pelicula.get_anio()}\n"
                  f"fecha: {actual.pelicula.get_fecha()}\n"
                  f"hora: {actual.pelicula.get_hora()}\n"
                  f"imagen: {actual.pelicula.get_imagen()}\n"
                  f"precio: {actual.pelicula.get_precio()}\n")

            if listaDePelis.cabeza == actual.siguiente:

                break

            else:
                actual = actual.siguiente

    def add_Pelicula(self, pelicula: Pelicula):

        nuevo_Nodo: NodoPelicula = NodoPelicula(pelicula)

        if self.cabeza is None:

            self.cabeza = nuevo_Nodo
            self.cola = nuevo_Nodo
            nuevo_Nodo.anterior = nuevo_Nodo
            nuevo_Nodo.siguiente = nuevo_Nodo

        else:

            nuevo_Nodo.anterior = self.cola
            nuevo_Nodo.siguiente = self.cabeza
            self.cola.siguiente = nuevo_Nodo
            self.cabeza.anterior = nuevo_Nodo
            self.cola = nuevo_Nodo