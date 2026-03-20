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
    print('=== MENU CANCIONES ===')
    print(f'1- Añadir cancion')
    print(f'2- Eliminar cancion')
    print(f'3- Mostrar todas canciones disponibles')
    print(f'4- Buscar cancion')
    print(f'0- Salir al menu general')
    print('======================')

def menu_playlists():
    print()
    print('=== MENU PLAYLISTS ===')
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
    print('==== MENU ARTISTA ====')
    print(f'1- Añadir artista')
    print(f'2- Eliminar artista')
    print(f'3- Buscar artista')
    print(f'4- Mostrar todos artistas registrados')
    print(f'0- Salir al menu general')
    print('======================')

def menu_album():
    print()
    print('===== MENU ALBUM =====')
    print(f'1- Añadir nuevo album')
    print(f'2- Eliminar album')
    print(f'3- Buscar album')
    print(f'4- Mostrar todos albumes disponibles')
    print(f'0- Salir al menu general')
    print('======================')

def menu_productor_musical():
    print()
    print('===== MENU ALBUM =====')
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
        while opcion_general not in ('0', '1', '2', '3', '4'):
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
                    print('Añadiendo cancion a la base de datos...')

                elif opcion_canciones =='2':
                    # codigo: Eliminar cancion a la base de datos
                    print('Eliminando cancion de la base de datos...')

                elif opcion_canciones =='3':
                    print('Mostrando todas las canciones...')
                    print()
                    print(f'== LISTADO DE CANCIONES DISPONIBLES ==')
                    #codigo: mostrar el listado de todas las canciones en la base de datos

                elif opcion_canciones =='4':
                    print('Buscando canciones en la base de datos...')
                    #codigo: buscar artista en la base de datos.

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

                #llamamos la funcion que muestre el menu de albumes.
                menu_album()

                opcion_album = pedir_opcion()
                # nos aseguramos de que la opcion es valida dentro de las posibles.
                while opcion_album not in ('0', '1', '2', '3', '4'):
                    print("Opcion no valida.")
                    opcion_album = pedir_opcion()

                if opcion_album == '0':
                    print('Saliendo al menu general...')
                    start3 = False

                elif opcion_album == '1':
                    #codigo: anadir nuevo album a la base de datos.
                    print(f'Añadiendo nuevo album...')

                elif opcion_album == '2':
                    #codigo: eliminar album de la base de datos.
                    print(f'Eliminando album...')

                elif opcion_album == '3':
                    print('Buscando album en la base de datos...')
                    #codigo: buscar album en la base de datos.

                elif opcion_album == '4':
                    print('Mostrando todos los albumes disponibles...')
                    print()
                    print(f'== ALBUMES DISPONIBLES ==')
                    #codigo: recorrer la carpeta con albumes y mostrar los nombres.

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
    # AQUI ACABA LA OPCION ZERO (BUCLE GENERAL)

#----------------------------------------------
#main()
