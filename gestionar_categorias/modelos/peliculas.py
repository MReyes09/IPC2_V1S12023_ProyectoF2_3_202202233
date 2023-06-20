
class Pelicula:
    def __init__(self, titulo:str, director:str, anio:int, fecha:str, hora:str, imagen:str, precio:int):
        self._titulo = titulo
        self._director = director
        self._anio = anio
        self._fecha = fecha
        self._hora = hora
        self._imagen = imagen
        self._precio = precio


    def get_titulo(self) -> str:
        return self._titulo

    def set_titulo(self, titulo: str):
        self._titulo = titulo

    def get_director(self) -> str:
        return self._director

    def set_director(self, director: str):
        self._director = director

    def get_anio(self) -> int:
        return self._anio

    def set_anio(self, anio: int):
        self._anio = anio

    def get_fecha(self) -> str:
        return self._fecha

    def set_fecha(self, fecha: str):
        self._fecha = fecha

    def get_hora(self) -> str:
        return self._hora

    def set_hora(self, hora: str):
        self._hora = hora

    def get_imagen(self) -> str:
        return self._imagen

    def set_imagen(self, imagen: str):
        self._imagen = imagen

    def get_precio(self) -> int:
        return self._precio

    def set_precio(self, precio: int):
        self._precio = precio

    def __str__(self) -> str:
        return self._titulo