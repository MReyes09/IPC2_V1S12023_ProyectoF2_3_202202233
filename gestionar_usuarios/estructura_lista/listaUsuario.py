from ..estructura_lista.nodoUsuario import NodoUser
from ..modelos.usuario import Usuario

import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class ListaUser:

    userLoged:Usuario = None

    def __init__(self):
        self.cabeza:NodoUser = None

    def CargarXML(self):
            
        with open('dataXML/usuarios.xml', 'r', encoding='utf-8') as archivo:
            tree = ET.parse(archivo)
            root = tree.getroot()

            self.cabeza = None

            for usuarios in root.findall('usuario'):
                rol: str = usuarios.find('rol').text
                nombre: str = usuarios.find('nombre').text
                apellido: str = usuarios.find('apellido').text
                telefono: int = int(usuarios.find('telefono').text)
                correo: str = usuarios.find('correo').text
                contrasena: str = usuarios.find('contrasena').text

                cargar_User = Usuario(rol, nombre, apellido, telefono, correo, contrasena)
                self.add_User(cargar_User)

    def add_User(self, user: Usuario):
        nuevo_User = NodoUser(user)

        if self.cabeza is None:
            self.cabeza = nuevo_User
        else:
            actual: NodoUser = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_User

    def Listar_Usuarios(self):
        actual: NodoUser = self.cabeza
        while actual is not None:
            usuario: Usuario = actual.dato
            print(f"Rol: {usuario.get_rol()} nombre: {usuario.get_nombre()} telefono: {usuario.get_telefono()} correo: {usuario.get_correo()} contraseña: {usuario.get_contrasena()}")
            actual = actual.siguiente

    def Iniciar_Sesion(self,  correo_Rec: str, contrasena_Rec: str) -> Usuario:
        actual: NodoUser = self.cabeza
        while actual is not None:
            usuario: Usuario = actual.dato
            if usuario.get_correo() == correo_Rec and usuario.get_contrasena() == contrasena_Rec:
                self.userLoged = usuario
                return self.userLoged
            actual = actual.siguiente
        return None
    
    def Registrarse(self, rol:str, nombre:str, apellido:str, telefono:int, correo:str, contrasena:str):

         #Guardar el usuario en la lista simple enlazada
         usuario_Nuevo_En_Lista:Usuario = Usuario(rol, nombre, apellido, telefono, correo, contrasena)

         self.add_User(usuario_Nuevo_En_Lista)

         print("El usuario se ha registrado exitosamente \n")

    def actualizar_Usuario(self, userLoged: Usuario):

        actual: NodoUser = self.cabeza

        while actual is not None:

            usuario: Usuario = actual.dato

            if usuario.get_correo() == userLoged.get_correo():

                actual.dato = userLoged
                self.userLoged = userLoged
                return userLoged

            actual = actual.siguiente

        print("No se encontro coincidencias")

    def get_UserLoged(self):

        return self.userLoged