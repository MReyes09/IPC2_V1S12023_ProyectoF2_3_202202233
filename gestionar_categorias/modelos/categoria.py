
class Categoria:

    def __init__(self, nombreCa: str, peliculas=None):
        self.nombreCa = nombreCa
        self.peliculas = peliculas if peliculas is not None else None

    def set_NombreCa(self, nombreCa: str):
        self.nombreCa = nombreCa

    def get_NombreCa(self) -> str:
        return self.nombreCa

    def set_Peliculas(self, peliculas):
        self.peliculas = peliculas

    def get_Peliculas(self):
        return self.peliculas