from gestionar_usuarios.modelos.Tarjeta import Tarjeta

class NodoTarjeta:

    def __init__(self, tarjeta:Tarjeta):
        
        self.tarjeta:Tarjeta = tarjeta
        self.anterior = None
        self.siguiente = None