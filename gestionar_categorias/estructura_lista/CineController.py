import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

from gestionar_categorias.estructura_lista.ListsaSala import ListaSala
from gestionar_categorias.modelos.Cine import Cine
from gestionar_categorias.modelos.Sala import Sala
from gestionar_categorias.estructura_lista.NodoSala import NodoSala


class CineController:

    listaCines = []    

    def CargarXML_Cine(self):

        tree = ET.parse('dataXML/salas.xml')
        root = tree.getroot()

        self.listaCines.clear()

        for cine in root.findall('cine'):

            lista_Sala: ListaSala = ListaSala()
            nombre_Cine: str = cine.find('nombre').text

            for sala in cine.findall('salas/sala'):

                numero:str = sala.find('numero').text
                asientos:int = int(sala.find('asientos').text)
                cargar_Sala: Sala = Sala(numero, asientos)
                lista_Sala.add_Sala(cargar_Sala)

            cargar_Cine: Cine = Cine(nombre_Cine, lista_Sala)
            self.listaCines.append(cargar_Cine)
    
    def actualizar_XML(self, listaCines):

        root = ET.Element("cines")

        if len(listaCines) !=0:

            for cine in listaCines:

                nuevo_Cine = ET.SubElement(root, "cine")
                nombre = ET.SubElement(nuevo_Cine, "nombre")
                nombre.text = cine.get_nombre()

                salas = ET.SubElement(nuevo_Cine, "salas")

                if cine.get_salas() is not None:
                    lista_Salas:ListaSala = cine.get_salas()
                    nodo_actual: NodoSala = lista_Salas.cabeza

                    while nodo_actual is not None:

                        getSala = nodo_actual.sala
                        nueva_Sala = ET.SubElement(salas, "sala")

                        numero = ET.SubElement(nueva_Sala, "numero")
                        numero.text = getSala.get_numero()

                        asientos = ET.SubElement(nueva_Sala, "asientos")
                        asientos.text = str(getSala.get_asientos())

                        nodo_actual = nodo_actual.siguiente

            xml_str = ET.tostring(root, encoding="utf-8")
            dom = minidom.parseString(xml_str)
            with open("dataXML/salas.xml", "w") as archivo:
                archivo.write(dom.toprettyxml(indent="   "))

    def get_Lista_Cines(self):

        return self.listaCines
    
    def agregar_Cine(self, nombre:str) -> []:

        agregar_Cine: Cine = Cine(nombre)
        self.listaCines.append(agregar_Cine)

        return self.listaCines
    
    def eliminar_Cine(self, nombre:str) -> []:

        indice: int = 0

        for cine in self.listaCines:

            if cine.get_nombre() == nombre:

                del self.listaCines[indice]
                print(f"se elimino con exito el cine {nombre}\n")
                return self.listaCines

            else: indice += 1
        print(f"No se encontro ningun cine con nombre {nombre}\n")

    def modificar_Cine(self, nombre: str, nombre_nuevo:str, sala_nueva, numero, opcion:int) -> []:

        indice: int = 0
        for cine in self.listaCines:

            if cine.get_nombre() == nombre:

                if opcion == 1:
                    
                    if cine.get_salas() is not None:

                        up_Cine: Cine = Cine(nombre_nuevo, cine.get_salas())
                        self.listaCines[indice] = up_Cine
                        return self.listaCines

                    else:

                        up_Cine: Cine = Cine(nombre_nuevo)
                        self.listaCines[indice] = up_Cine
                        return self.listaCines

                elif opcion == 2:

                    
                    if cine.get_salas() is None:

                        lista_Nueva: ListaSala = ListaSala()
                        lista_Nueva.add_Sala(sala_nueva)
                        cine.set_salas(lista_Nueva)

                    else:

                        cine.get_salas().add_Sala(sala_nueva)

                    self.listaCines[indice] = cine
                    return self.listaCines

                elif opcion == 3:

                    cine.get_salas().buscar_Sala(numero, sala_nueva, 2)
                    self.listaCines[indice] = cine
                    return self.listaCines

                elif opcion == 4:

                    cine.get_salas().eliminar_Sala(numero)
                    self.listaCines[indice] = cine
                    return self.listaCines

            else: indice += 1

        print("No se encontro ninguna coincidencia con el nombre")