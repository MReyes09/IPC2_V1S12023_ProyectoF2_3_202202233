from gestionar_categorias.modelos.Sala import Sala
from gestionar_categorias.estructura_lista.NodoSala import NodoSala


class ListaSala:

    def __init__(self):
        self.cabeza: NodoSala = None

    def add_Sala(self, sala: Sala):

        new_nodo = NodoSala(sala)

        if self.cabeza is None:

            self.cabeza = new_nodo

        else:

            actual: NodoSala = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = new_nodo

    def eliminar_Sala(self, numero_Sala: str):

        if self.cabeza is None:
            return

            # Caso 1: El nodo a eliminar es el primero
        if self.cabeza.sala.get_numero() == numero_Sala:
            siguiente_nodo = self.cabeza.siguiente
            if siguiente_nodo is not None:
                siguiente_nodo.anterior = None
            self.cabeza = siguiente_nodo
            return

        nodo_actual:NodoSala = self.cabeza
        # Caso 2: El nodo a eliminar está en medio
        while nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.sala.get_numero() == numero_Sala:
                nodo_siguiente = nodo_actual.siguiente.siguiente
                nodo_actual.siguiente = nodo_siguiente
                if nodo_siguiente is not None:
                    nodo_siguiente.anterior = nodo_actual
                return
            nodo_actual = nodo_actual.siguiente

        # Caso 3: El nodo a eliminar es el último
        if nodo_actual.sala.get_numero() == numero_Sala:
            nodo_anterior = nodo_actual.anterior
            if nodo_anterior is not None:
                nodo_anterior.siguiente = None
            return

        # Si el dato no se encuentra en la lista, se puede mostrar un mensaje o realizar otra acción
        print("El dato no existe en la lista.")

    def buscar_Sala(self, numero_Sala: str, sala_Ac, opcion:int):

        if self.cabeza is None:

            print("No tiene salas")
            return

        else:

            nodoSala: NodoSala = self.cabeza

            while nodoSala is not None:

                sala = nodoSala.sala

                if opcion == 1:
                    if sala.get_numero() == numero_Sala:

                        return sala

                    else:
                        nodoSala = nodoSala.siguiente

                elif opcion == 2: #Actualizar sala con coincidencia

                    if sala.get_numero() == numero_Sala:

                        nodoSala.sala = sala_Ac
                        return

                    else: nodoSala = nodoSala.siguiente

            return

    def loop(self):

        actual = self.cabeza

        while actual:
            yield actual.sala
            actual = actual.siguiente

            if actual == None:
                break

    def __iter__(self):
        return iter(self.loop())