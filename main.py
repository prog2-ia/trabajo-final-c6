import json
#importamos clases que heredan del Contenido:
from clases.Contenido.canciones import Cancion
from clases.Contenido.album import Album
from clases.Contenido.playlist import ListaReproduccion

#importamos clases que heredan del Artista:
from clases.Artistas.cantantes import Cantantes
from clases.Artistas.grupo import Grupos
from clases.Artistas.orquesta import Orquestas
from clases.Artistas.productor_musical import ProductorMusical

# funciones auxiliares -----------------------------------------

def menu_canciones():
    print()
    print('===== MENU CANCIONES =====')
    print(f'1- Añadir cancion')
    print(f'2- Eliminar cancion')
    print(f'3- Mostrar todas canciones disponibles')
    print(f'4- filtrar canciones')
    print(f'0- Salir al menu general')
    print('======================')

def menu_playlists():
    print()
    print('===== MENU PLAYLISTS =====')
    print(f'1- Crear playlist')
    print(f'2- Eliminar playlist')
    print(f'3- Anadir cancion a la playlist')
    print(f'4- Eliminar cancion de la  playlist')
    print(f'5- Mostrar todas playlists disponibles')
    print(f'6- Buscar playlist')
    print(f'0- Salir al menu general')
    print('======================')

def menu_artista():
    print()
    print('===== MENU ARTISTA =====')
    print(f'1- Añadir artista')
    print(f'2- Eliminar artista')
    print(f'3- Buscar artista')
    print(f'4- Mostrar todos artistas registrados')
    print(f'0- Salir al menu general')
    print('======================')

def menu_elegir_album():
    print()
    print('===== ALBUMES DISPONIBLES =====')
    archivos = Album.listar_albumes("archivos/albumes")
    print('---------------------------')
    print(f'{len(archivos)+1}- Crear nuevo album')
    print('0- Salir al menu general')
    print('======================')
    return archivos

def menu_album():
    print('===== MENU ALBUM =====')
    print(f'1- Mostrar informacion')
    print(f'2- Mostrar el listado de canciones')
    print(f'3- Eliminar album')
    print(f'0- salir la listado de albumes')
    print('======================')

def menu_productor_musical():
    print()
    print('===== MENU PRODUCTOR =====')
    print(f'1- Añadir nuevo productor')
    print(f'2- Eliminar productor ')
    print(f'3- Buscar productor')
    print(f'4- Mostrar todos productores guardados')
    print(f'0- Salir al menu general')
    print('======================')

def menu():
    print()
    print(f'=========== BIBLIOTECA MUSICAL ===========')
    print(f'1- Menu canciones')
    print(f'2- Menu playlists')
    print(f'3- Menu album')
    print(f'4- Menu artistas')
    print(f'5- Menu productor musical')
    print(f'0- Salir')
    print('==========================================')


def pedir_opcion():
    print()
    opcion = input('Elige una opcion: ').strip()
    return opcion



# funcion principal ----------------------------------------------

#el bucle principal del programa:
def main():
    start_general = True
    while start_general:

        # llamamos la funcion que muestra el menu de la biblioteca musical:
        menu()

        #pedimos una opcion al usuario.
        opcion_general = pedir_opcion()
        #nos aseguramos de que la opcion es valida dentro de las posibles.
        while opcion_general not in ('0', '1', '2', '3', '4','5'):
            print("Opcion no valida.")
            opcion_general = pedir_opcion()


        #FLUJO DEL PROGRAMA-----------------------------------------:

        #la opcion en el bucle grande es 0- salimos del programa.
        if opcion_general == '0':
            print('Saliendo del programa...')
            start_general = False

        #cuando elegimos la opcion 1- es decir la gestion de las canciones.
        elif opcion_general == '1':
            start1 = True
            while start1:

                #mostramos el menu de las canciones:
                menu_canciones()

                #pedimos al usuario una opcion dentro del submenu de canciones
                opcion_canciones = pedir_opcion()
                # nos aseguramos de que la opcion es valida dentro de las posibles.
                while opcion_canciones not in ('0', '1', '2', '3', '4'):
                    print("Opcion no valida.")
                    opcion_canciones = pedir_opcion()

                if opcion_canciones == '0':
                    print('Saliendo al menu general...')
                    start1 = False

                elif opcion_canciones =='1':
                    # codigo: Anadir cancion a la base de datos
                    print()
                    print('==== ANADIENDO CANCION ====')
                    cancion = Cancion(
                        titulo =  input('Introduce el titulo de la cancion: '),
                        artista = input('Introduce el autor de la cancion: '),
                        fecha_lanzamiento = input('Introduce el año de lanzamiento de la cancion: '),
                        duracion = input('Introduce la duracion de la cancion: '),
                        genero=[g.strip() for g in input('Introduce el genero(s) de la cancion: ').split(',')],
                        discografia= input('Introduce la discografia de la cancion: ')
                    )
                    #utilizamos el metodo de guardar canciones de la clase cancion.
                    Cancion.anadir_cancion(cancion,'archivos/canciones_guardadas.json')

                #eliminamos canciones de la base de datos.
                elif opcion_canciones =='2':
                    # codigo: Eliminar cancion a la base de datos
                    print()
                    print('==== ELIMINANDO CANCION ====')
                    titulo = input('Introduce el titulo de la cancion a borrar: ')
                    artista = input('Introduce el autor de la cancion: ')
                    Cancion.eliminar_cancion(titulo,artista)

                #mostramos todas las canciones disponibles.
                elif opcion_canciones =='3':
                    print('Mostrando todas las canciones...')
                    print()
                    print(f'== LISTADO DE CANCIONES DISPONIBLES ==')
                    #codigo: mostrar el listado de todas las canciones en la base de datos.
                    Cancion.mostrar_canciones()

                #filtramos las canciones segun gustos.
                elif opcion_canciones =='4':
                    #codigo: buscar artista en la base de datos.
                    Cancion.filtrar_canciones()

        #AQUI ACABA LA PRIMERA OPCION (CANCIONES)

        # cuando elegimos la opcion 2- la gestion de las playlists
        elif opcion_general =='2':
            start2 = True
            while start2:

                #llamamos la funcion que muestra el menu de las playlists
                menu_playlists()

                opcion_playlist = pedir_opcion()
                # nos aseguramos de que la opcion es valida dentro de las posibles.
                while opcion_playlist not in ('0', '1', '2', '3', '4','5','6'):
                    print("Opcion no valida.")
                    opcion_playlist = pedir_opcion()

                if opcion_playlist == '0':
                    print('Saliendo al menu general...')
                    start2 = False

                elif opcion_playlist == '1':
                    #codigo: crear playlist vacia (crear un archivo .json)
                    print(f'Creando una playlist...')

                elif opcion_playlist =='2':
                    #codigo: Eliminar playlist entera (eliminar el archivo .json)
                    print(f'Eliminando la playlist...')

                elif opcion_playlist == '3':
                    # codigo: Anadir cancion a la playlist
                    print(f'Añadiendo la cancion a la playlist...')

                elif opcion_playlist == '4':
                    #codigo: eliminar cancion de la playlist
                    print(f'Eliminando la cancion de la playlist...')

                elif opcion_playlist == '5':
                    print(f'Mostrando las playlists disponibles...')
                    print()
                    print(f'== PLAYLISTS DISPONIBLES ==')
                    #codigo: mostrar el listado de las playlists (por su nombre)

                elif opcion_playlist == '6':
                    print(f'Buscando playlists...')
                    #codigo: buscar la playlist en la base de datos.

        #AQUI ACABA LA SEGUNDA OPCION (PLAYLISTS)


        #cuando elegimos en el menu principal 3- entramos en el gestor de albumes.

        elif opcion_general == '3':
            start3 = True
            while start3:

                #muestramos los albumes dispobibles.
                albumes_disponibles = menu_elegir_album()
                #pedimos al usuario que eliga una opcion.
                opcion_elegir_album = pedir_opcion()

                #validamos la opcion.
                while not (opcion_elegir_album.isdigit() and 0 <= int(opcion_elegir_album) <= len(albumes_disponibles) + 1):
                    print("Opcion no valida.")

                    #volvemos a pedir la opcion
                    opcion_elegir_album = pedir_opcion()

                #si elegimos 0, salimos al menu general.
                if opcion_elegir_album == '0':
                    print('Saliendo al menu general...')
                    start3 = False

                #opcion de crear nuevo album desde el menu.
                elif opcion_elegir_album == str(len(albumes_disponibles)+1):
                    print('Creando nuevo album...')

                #cuando obtenemos un numero valido (distinto de 0), cargamos el archivo con el album.
                else:
                    indice = int(opcion_elegir_album) - 1
                    #seleccionamos el album.
                    nombre_archivo = albumes_disponibles[indice]
                    album_cargado = Album.seleccionar_album(nombre_archivo)

                    #si el album se ha cargado, empezamos un bucle.
                    if album_cargado is not None:
                        start_album = True
                        while start_album:

                            #mostramos el menu.
                            menu_album()
                            #pedimos una opcion.
                            opcion_album = pedir_opcion()

                            #validamos la opcion.
                            while opcion_album not in ('0', '1', '2', '3'):
                                print("Opcion no valida.")
                                opcion_album = pedir_opcion()

                            #si elegimos 0, salimos al listado de los albumes.
                            if opcion_album == '0':
                                print('Saliendo al listado de albumes disponibles...')
                                start_album = False

                            #mostramos la info del album.
                            elif opcion_album == '1':
                                album_cargado.mostrar_info_album()

                            #mostramos el listado de las canciones del album.
                            elif opcion_album == '2':
                                album_cargado.mostrar_canciones_album()

                            #eliminamos el album
                            elif opcion_album == '3':
                                album_cargado.eliminar_album()
                                #volvemos al listado de los albumes.
                                start_album = False

        # AQUI ACABA LA TERCERA OPCION (ALBUMES)

        #en el menu principal elegimos 4- el gestor de artistas.
        elif opcion_general == '4':
            start4 = True
            while start4:

                #mostramos la informacion del menu de artistas:
                menu_artista()

                opcion_artista = pedir_opcion()
                # nos aseguramos de que la opcion es valida dentro de las posibles.
                while opcion_artista not in ('0', '1', '2', '3', '4'):
                    print("Opcion no valida.")
                    opcion_artista = pedir_opcion()

                #salimos al menu general
                if opcion_artista == '0':
                    print('Saliendo al menu general...')
                    start4 = False

                elif opcion_artista == '1':
                    #codigo: anadir artista a la base de datos
                    print(f'Añadiendo artista a la base de datos...')

                elif opcion_artista == '2':
                    #codigo: eliminar artista de la base de datos
                    print(f'Eliminando artista de la base de datos...')

                elif opcion_artista == '3':
                    print('Buscando artista...')
                    #codigo: buscar artista en la base de datos

                elif opcion_artista == '4':
                    print('Mostrando los artistas registrados...')
                    print(f'== ARTISTAS REGISTRADOS ==')
                    #codigo: mostrar todos los artistas de la base de datos.

        # AQUI ACABA LA CUARTA OPCION (ARTISTAS)

        #si elegimos 4, entramos en el menu de productor musical.
        elif opcion_general == '5':
            start5 = True
            while start5:

                #mostramos el menu
                menu_productor_musical()

                #pedimos una opcion
                opcion_productor = pedir_opcion()
                # nos aseguramos de que la opcion es valida dentro de las posibles.
                while opcion_productor not in ('0', '1', '2', '3', '4', '5', '6'):
                    print("Opcion no valida.")
                    opcion_productor = pedir_opcion()

                #analizamos las opciones:
                #salimos del programa.
                if opcion_productor == '0':
                    print('Saliendo al menu general...')
                    start5 = False

                #anadimos nuevo productor a la base de datos.
                elif opcion_productor == '1':
                    #codigo: anadir nuevo productor.
                    print('Añadiendo productor musical a la base de datos...')

                #eliminamos productor de la base de datos.
                elif opcion_productor == '2':
                    #codigo: eliminar productor
                    print('Eliminando productor de la base de datos...')

                #opcion de buscar productor.
                elif opcion_productor == '3':
                    print('Buscando el productor en la base de datos...')
                    #codigo: buscar productor

                #mostramos productor.
                elif opcion_productor == '4':
                    print('Mostrando todos los productores...')
                    #codigo: mostrar productor

        #AQUI ACABA LA OPCION 5 (PRODUCTOR MUSICAL)
    # AQUI ACABA LA OPCION ZERO (BUCLE GENERAL)

#----------------------------------------------
main()