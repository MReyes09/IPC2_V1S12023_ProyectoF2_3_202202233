
class Cine:

    def __init__(self, nombre:str, salas = None):
        self._nombre = nombre
        self._salas = salas if salas is not None else None

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def get_salas(self):
        return self._salas

    def set_salas(self, salas):
        self._salas = salas