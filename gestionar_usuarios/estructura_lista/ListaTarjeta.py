import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

from gestionar_usuarios.estructura_lista.NodoTarjeta import NodoTarjeta
from gestionar_usuarios.modelos.Tarjeta import Tarjeta

class ListaTarjeta:

    def __init__(self):
        self.cabeza: NodoTarjeta = None

    def add_Sala(self, tarjeta: Tarjeta):

        new_nodo = NodoTarjeta(tarjeta)

        if self.cabeza is None:

            self.cabeza = new_nodo

        else:

            actual: NodoTarjeta = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = new_nodo  
    
    def CargarXML_Tarjeta(self):

        tree = ET.parse('dataXML/tarjetas.xml')
        root = tree.getroot()

        self.cabeza = None

        for tarjeta in root.findall('tarjeta'):

            tipo:str = tarjeta.find('tipo').text
            numero:int = int(tarjeta.find('numero').text)
            titular:str = tarjeta.find('titular').text
            fecha_expiracion:str = tarjeta.find('fecha_expiracion').text
            
            cargar_tarjeta:Tarjeta = Tarjeta(tipo, numero, titular, fecha_expiracion)
            self.add_Sala(cargar_tarjeta)

    def actualizar_XML(self):

        root = ET.Element("tarjetas")

        if self.cabeza is not None:
            nodo_actual = self.cabeza

            while nodo_actual is not None:
                tarjeta = nodo_actual.tarjeta
                nueva_tarjeta = ET.SubElement(root, "tarjeta")

                tipo = ET.SubElement(nueva_tarjeta, "tipo")
                tipo.text = tarjeta.tipo

                numero = ET.SubElement(nueva_tarjeta, "numero")
                numero.text = str(tarjeta.numero)

                titular = ET.SubElement(nueva_tarjeta, "titular")
                titular.text = tarjeta.titular

                fecha_expiracion = ET.SubElement(nueva_tarjeta, "fecha_expiracion")
                fecha_expiracion.text = tarjeta.fecha_expiracion

                nodo_actual = nodo_actual.siguiente

        xml_str = ET.tostring(root, encoding="utf-8")
        dom = minidom.parseString(xml_str)
        with open("dataXML/tarjetas.xml", "w") as archivo:
            archivo.write(dom.toprettyxml(indent="   "))
            
    def eliminar_Tarjeta(self, numero: int):

        if self.cabeza is None:
            return

            # Caso 1: El nodo a eliminar es el primero
        if self.cabeza.tarjeta.numero == numero:
            siguiente_nodo = self.cabeza.siguiente
            if siguiente_nodo is not None:
                siguiente_nodo.anterior = None
            self.cabeza = siguiente_nodo
            return

        nodo_actual:NodoTarjeta = self.cabeza
        # Caso 2: El nodo a eliminar está en medio
        while nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.tarjeta.numero == numero:
                nodo_siguiente = nodo_actual.siguiente.siguiente
                nodo_actual.siguiente = nodo_siguiente
                if nodo_siguiente is not None:
                    nodo_siguiente.anterior = nodo_actual
                return
            nodo_actual = nodo_actual.siguiente

        # Caso 3: El nodo a eliminar es el último
        if nodo_actual.tarjeta.numero == numero:
            nodo_anterior = nodo_actual.anterior
            if nodo_anterior is not None:
                nodo_anterior.siguiente = None
            return

        # Si el dato no se encuentra en la lista, se puede mostrar un mensaje o realizar otra acción
        print("El dato no existe en la lista.")

    def buscar_Tarjeta(self, numero: str, Tarjeta_Ac):

        if self.cabeza is None:

            print("No tiene Tarjetas")
            return

        else:

            nodoTarjeta: NodoTarjeta = self.cabeza

            while nodoTarjeta is not None:

                tarjeta = nodoTarjeta.tarjeta

                if tarjeta.numero == numero:

                    nodoTarjeta.tarjeta = Tarjeta_Ac
                    return

                else: nodoTarjeta = nodoTarjeta.siguiente

            return

    def loop(self):

        actual = self.cabeza

        while actual:
            yield actual.tarjeta
            actual = actual.siguiente

            if actual == None:
                break

    def __iter__(self):
        return iter(self.loop())