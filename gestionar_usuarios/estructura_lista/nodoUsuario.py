
from ..modelos.usuario import Usuario


class NodoUser:
    def __init__(self, user: Usuario): #se solicita un usuario como parametro
        self.dato = user
        self.siguiente = None