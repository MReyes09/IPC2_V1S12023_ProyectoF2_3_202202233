from django.shortcuts import render, redirect
from django.contrib import messages

from gestionar_usuarios.estructura_lista.listaUsuario import ListaUser
from gestionar_usuarios.modelos.usuario import Usuario
from gestionar_usuarios.modelos.Tarjeta import Tarjeta
from gestionar_categorias.views import getListaCategoria, setListaCategoria, setListaCine, getListaCine
from gestionar_categorias.estructura_lista.lista_Pelicula import ListaPelicula
from gestionar_categorias.modelos.peliculas import Pelicula
from gestionar_categorias.modelos.categoria import Categoria
from gestionar_categorias.modelos.Sala import Sala
from gestionar_categorias.estructura_lista.CineController import CineController
from gestionar_usuarios.estructura_lista.ListaTarjeta import ListaTarjeta
from gestionar_usuarios.estructura_lista.HistorialController import HistorialController
from gestionar_categorias.estructura_lista.categoriaCotroller import categoriaController

#CONTROLADORES
cineControl = CineController()
categoriaControl = categoriaController()

historialControl = HistorialController()
lista_Cines = []

lista_Tarjetas: ListaTarjeta = ListaTarjeta()

lista: ListaUser = ListaUser()
lista.add_Admin()
userLoged:Usuario = None

listaCategorias = []


def getListaUsers() -> ListaUser:
    global lista
    
    return lista

def setListaUsers(listaUsers):
    global lista

    lista = listaUsers

def menuUserCliente(request):

    global listaCategorias
    global userLoged

    userLoged = lista.get_UserLoged()
    mi_Fav:ListaPelicula = userLoged.get_peliFav()

    if request.method == 'GET' and 'categoria' in request.GET:
        
        categoria_seleccionada:str = request.GET.get('categoria')
        return render(request, 'menuUser.html', {'Mi_Fav': mi_Fav, 'lista_Categorias': listaCategorias, 'userLoged': userLoged, 'categoria_Seleccionada': categoria_seleccionada,})
    
    elif request.method == "POST" :

        titulo = request.POST.get('titulo')
        nomCategoria = request.POST.get('categoria')

        if userLoged.get_peliFav():
            
            for categoria in listaCategorias:

                if categoria.get_NombreCa() == nomCategoria:
                    lista_Peliculas:ListaPelicula = categoria.get_Peliculas()
                    findedPelicula:Pelicula = lista_Peliculas.buscar_Pelicula(lista_Peliculas, titulo)
                    my_List:ListaPelicula = userLoged.get_peliFav()
                    my_List.add_Pelicula(findedPelicula)
                    userLoged.set_peliFav(my_List)
                    lista.actualizar_Usuario(userLoged)
                    categoria_seleccionada = "General"

                    return render(request, 'menuUser.html', {'Mi_Fav': mi_Fav, 'lista_Categorias': listaCategorias, 'userLoged': userLoged, 'categoria_Seleccionada': categoria_seleccionada,})

        else: 

            lista_Nueva: ListaPelicula = ListaPelicula()

            for categoria in listaCategorias:

                if categoria.get_NombreCa() == nomCategoria:

                    lista_Peliculas:ListaPelicula = categoria.get_Peliculas()
                    findedPelicula:Pelicula = lista_Peliculas.buscar_Pelicula(lista_Peliculas, titulo)
                    lista_Nueva.add_Pelicula(findedPelicula)                    
                    userLoged.set_peliFav(lista_Nueva)
                    lista.actualizar_Usuario(userLoged)
                    categoria_seleccionada = "General"

                    return render(request, 'menuUser.html', {'Mi_Fav': mi_Fav, 'lista_Categorias': listaCategorias, 'userLoged': userLoged, 'categoria_Seleccionada': categoria_seleccionada,})
                
    categoria_seleccionada = "General"
    return render(request, 'menuUser.html', {'Mi_Fav': mi_Fav, 'lista_Categorias': listaCategorias, 'userLoged': userLoged, 'categoria_Seleccionada': categoria_seleccionada,})

def compraBoletos(request, titulo:str, categoria:str):
    global cineControl
    global lista_Cines
    global lista_Tarjetas
    global userLoged

    get_Pel:Pelicula = None
    for categorias in listaCategorias:

        if categorias.get_NombreCa() == categoria:

            buscar_Cat:Categoria = categorias
            lista_Buscar_Pelis: ListaPelicula = ListaPelicula()
            get_Pel = lista_Buscar_Pelis.buscar_Pelicula(buscar_Cat.get_Peliculas(),titulo)

    if request.method == "POST":

        titulo: str = get_Pel.get_titulo()
        fecha: str = get_Pel.get_fecha()
        hora: str = get_Pel.get_hora()
        num_Boletos:int = int(request.POST.get('boletos'))
        num_Asientos:int = int(request.POST.get('asientos'))
        monto_Tot:int = num_Boletos*get_Pel.get_precio()
        tipo_Pago:int = int(request.POST.get('selectTarjeta'))
        tipo:str = ''

        if tipo_Pago == 1:

            tipo = "EFECTIVO"
        
        else: tipo = str(tipo_Pago)

        act_List = historialControl.add_Historial(userLoged.get_historial(), titulo, fecha, hora, num_Boletos, num_Asientos, monto_Tot, tipo)
        userLoged.set_historial(act_List)
        userLoged = lista.actualizar_Usuario(userLoged)

        return redirect('userHome')
            

    return render(request, 'boletos.html', {'Pelicula':get_Pel, 'lista_Cines':lista_Cines, 'lista_Tarjetas':lista_Tarjetas, 'userLoged':userLoged, })

def actualizar_Usuario(request, correo):
    user_UP:Usuario = None

    for usuario in lista:
        if usuario.get_correo() == correo:
            user_UP = usuario

    if request.method == 'POST':

        nombre:str = request.POST.get('nombre')
        apellido: str = request.POST.get('apellido')
        telefono:int = request.POST.get('telefono')                
        correo:str = request.POST.get('correo')
        contrasena:str = request.POST.get('contrasena')
        rol:str = request.POST.get('rol')
        
        user_U:Usuario = Usuario(rol, nombre, apellido, telefono, correo, contrasena)
        lista.actualizar_Usuario(user_U)
        messages.success(request, 'Se actualizo con exito')
        return redirect('userAdmin')
    
    return render(request, 'actualizar_User.html', {'user': user_UP},)

def menuAdminCliente(request):
    global lista
    global listaCategorias
    global categoriaControl
    global lista_Cines
    global lista_Tarjetas

    lista_Cines = getListaCine()

    if request.method == 'POST':
        tipo_gestion = request.POST.get('tipo_gestion')
        if tipo_gestion == "g_Usuario":

            nombre:str = request.POST.get('nombre')
            cargar_XML_U:str = request.POST.get('cargar_XML_U')

            if nombre is not None:

                apellido: str = request.POST.get('apellido')
                telefono:int = request.POST.get('telefono')                
                correo:str = request.POST.get('correo')
                contrasena:str = request.POST.get('contrasena')
                rol:str = request.POST.get('rol')
                lista.Registrarse(rol, nombre, apellido, telefono, correo, contrasena)
                messages.success(request, 'Se ha agregado el usuario con éxito')

            elif cargar_XML_U == "1":
                
                lista.CargarXML()
                lista.add_Admin()
                messages.success(request, 'XML de usuarios cargado exitosamente!')
            
            elif cargar_XML_U == "2":

                lista.actualizar_XML()
                messages.success(request, 'XML de usuarios actualizado exitosamente')

            else:
                correo:str = request.POST.get('correo')
                lista.eliminar_Usuario(correo)
                messages.success(request, 'Se ha eliminado un usuario con exito')

        elif tipo_gestion == "g_Pe_Ca":

            cargar_XML_U = request.POST.get('cargar_XML_U')
            nombreCa:str = request.POST.get('nombreCa')
            titulo_Pel:str = request.POST.get('titulo')
            operacion:str = request.POST.get('operacion')

            if cargar_XML_U == "1":
                listaCategorias = []
                setListaCategoria(listaCategorias)
                listaCategorias = categoriaControl.CargarXML_Category()
                setListaCategoria(listaCategorias)
                print(f"lista: {getListaCategoria()}")
                messages.success(request, 'XML de categorias y peliculas cargado exitosamente')

            elif cargar_XML_U == "2":

                categoriaControl.actualiar_XML()
                messages.success(request, 'XML de categorias y peliculas actualizado exitosamente')

            elif nombreCa and operacion == "agregar_C":

                categoriaControl.agregar_Categoria(nombreCa)
                messages.success(request, 'Se ha agregado la categoria con éxito')
            
            elif nombreCa and titulo_Pel == None:

                categoriaControl.eliminar_Categoria(nombreCa)
                messages.success(request, 'Se elimino la categoria con exito')

            elif operacion == "agregar_P":

                director:str = request.POST.get('director')
                anio:int = int(request.POST.get('anio'))
                fecha:str = request.POST.get('fecha')
                hora:str = request.POST.get('hora')
                imagen:str = request.POST.get('imagen')
                precio:int = request.POST.get('precio')

                peli_Nueva:Pelicula = Pelicula(titulo_Pel, director, anio, fecha, hora, imagen, precio)
                categoriaControl.agregar_Pelicula(nombreCa, peli_Nueva)
                messages.success(request, 'Se ha agregado la pelicula con éxito')

            elif titulo_Pel and operacion == None:
                
                categoriaControl.eliminar_Pel(nombreCa, titulo_Pel)
                messages.success(request, 'Se elimino la pelicula con exito')

        elif tipo_gestion == "g_Salas":

            cargar_XML_U = request.POST.get('cargar_XML_U')
            operacion:str = request.POST.get('operacion')
            nombre = request.POST.get('nombre')

            if cargar_XML_U == "1":

                cineControl.CargarXML_Cine()
                lista_Cines = cineControl.get_Lista_Cines()
                setListaCine(lista_Cines)

                messages.success(request, 'XML de cines y salas cargado exitosamente')

            elif cargar_XML_U == "2":

                cineControl.actualizar_XML(lista_Cines)
                messages.success(request, 'XML de cines y salas actualizado exitosamente')

            elif operacion == "agregar_S":

                cineControl.agregar_Cine(nombre)
                messages.success(request, 'Cine agregado exitosamente')

            elif operacion == "eliminar_C":

                cineControl.eliminar_Cine(nombre)
                print(f"cine: {nombre}")
                messages.success(request, 'Cine eliminado exitosamente')

            elif operacion == "agregar_Sala":

                numero = request.POST.get('numero')
                asientos = request.POST.get('asientos')

                sala_Nueva:Sala = Sala(numero, asientos)
                cineControl.modificar_Cine(nombre,None, sala_Nueva, None, 2)
                messages.success(request, 'Sala agregada exitosamente')

            elif operacion == "eliminar_S":

                numero = request.POST.get('numero')
                cineControl.modificar_Cine(nombre, None, None, numero, 4)
                messages.success(request, 'Sala eliminada exitosamente')

        elif tipo_gestion == "g_Tarjeta":

            cargar_XML_U = request.POST.get('cargar_XML_U')
            operacion:str = request.POST.get('operacion')

            if cargar_XML_U == "1":

                lista_Tarjetas.CargarXML_Tarjeta()
                messages.success(request, 'XML de las tarjetas se han cargado exitosamente!')

            if cargar_XML_U == "2":

                lista_Tarjetas.actualizar_XML()
                messages.success(request, 'XML de las tarjetas se ha actualizado exitosamente!')

            elif operacion == "agregar_T":

                tipo:str = request.POST.get('tipo')
                numero:int = int(request.POST.get('numero'))
                titular:str = request.POST.get("titular")
                fecha:str = request.POST.get('fecha')

                new_Tarjeta:Tarjeta = Tarjeta(tipo, numero, titular, fecha)
                lista_Tarjetas.add_Sala(new_Tarjeta)
                messages.success(request, 'Tarjeta agregada exitosamente!')

            elif operacion == "elimiminar_T":

                numero:int = int(request.POST.get('numero'))
                lista_Tarjetas.eliminar_Tarjeta(numero)
                messages.success(request, 'Tarjeta eliminada exitosamente!')


    setListaCategoria(listaCategorias)
    setListaCine(lista_Cines)
    return render(request, 'menuAdmin.html', {'lista_Usuarios': lista, 'lista_Categorias': listaCategorias, 'lista_Cines': lista_Cines, 'lista_Tarjetas': lista_Tarjetas})

def actualizar_Ta(request, numero):
    
    global lista_Tarjetas
    tarjeta_HTML:Tarjeta = None

    for tarjeta in lista_Tarjetas:

        if tarjeta.numero == numero:
            tarjeta_HTML = tarjeta

    if request.method == 'POST':

        tipo:str = request.POST.get('tipo')
        numero:int = int(request.POST.get('numero'))
        titular:str = request.POST.get("titular")
        fecha:str = request.POST.get('fecha')

        new_Tarjeta:Tarjeta = Tarjeta(tipo, numero, titular, fecha)
        lista_Tarjetas.buscar_Tarjeta(tarjeta_HTML.numero, new_Tarjeta)
        messages.success(request, 'Tarjeta actualizada exitosamente!')
        return redirect('userAdmin')

    return render(request, 'actualizar_Tarjeta.html', {'tarjeta': tarjeta_HTML})