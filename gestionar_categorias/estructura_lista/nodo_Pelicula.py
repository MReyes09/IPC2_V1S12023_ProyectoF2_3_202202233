from ..modelos.peliculas import Pelicula

class NodoPelicula:

    def __init__(self, pelicula: Pelicula):

        self.pelicula:Pelicula = pelicula
        self.anterior = None
        self.siguiente = None