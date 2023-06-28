from gestionar_categorias.modelos.Sala import Sala


class NodoSala:
    
    def __init__(self, sala: Sala):

        self.sala:Sala = sala
        self.anterior = None
        self.siguiente = None