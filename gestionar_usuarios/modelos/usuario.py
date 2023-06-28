
class Usuario:
        def __init__(self, rol:str , nombre:str, apellido:str, telefono: int, correo:str, contrasena:str, historial=None, peliFav = None):
            self._rol = rol
            self._nombre = nombre
            self._apellido = apellido
            self._telefono = telefono
            self._correo = correo
            self._contrasena = contrasena
            self._historial = historial if historial is not None else []
            self._peliFav = peliFav if peliFav is not None else None

        def set_rol(self, rol):
            self._rol = rol

        def get_rol(self):
            return self._rol

        def set_nombre(self, nombre):
            self._nombre = nombre

        def get_nombre(self):
            return self._nombre

        def set_apellido(self, apellido):
            self._apellido = apellido

        def get_apellido(self):
            return self._apellido

        def set_telefono(self, telefono):
            self._telefono = telefono

        def get_telefono(self):
            return self._telefono

        def set_correo(self, correo):
            self._correo = correo

        def get_correo(self):
            return self._correo

        def set_contrasena(self, contrasena):
            self._contrasena = contrasena

        def get_contrasena(self):
            return self._contrasena

        def set_historial(self, historial):
            self._historial = historial

        def get_historial(self):
            return self._historial

        def set_peliFav(self, peliFav):
            self._peliFav = peliFav

        def get_peliFav(self):
            return self._peliFav