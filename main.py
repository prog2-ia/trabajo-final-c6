#importamos clases que heredan del Contenido:
from clases.Contenido.canciones import Cancion
from clases.Contenido.album import Album
from clases.Contenido.lista_reproduccion import ListaReproduccion

#importamos clases que heredan del Artista:
from clases.Artistas.cantantes import Cantantes
from clases.Artistas.grupo import Grupos
from clases.Artistas.orquesta import Orquestas


def submenu_canciones():
    print('=== SUBMENU CANCIONES ===')
    print(f'1- Añadir cancion')
    print(f'2- Eliminar cancion')
    print(f'3- Mostrar canciones')
    print(f'0- Salir al menu general')
    print('=========================')

def submenu_playlists():
    print('=== SUBMENU PLAYLISTS ===')
    print(f'1- Crear playlist')
    print(f'2- Eliminar playlist')
    print(f'3- Anadir cancion a la playlist')
    print(f'4- Eliminar cancion de la  playlist')
    print(f'5- Eliminar playlist')
    print(f'0- Salir al menu general')
    print('=========================')

def main():
    start = True
    while start:
        print(f'=========== BIBLIOTECA MUSICAL ===========')
        print(f'1- Menu canciones')
        print(f'2- Menu playlists')
        print(f'0- Salir')
        print('==========================================')
        print()

        #pedimos una opcion al usuario.
        opcion1 = (input('Elige una opcion:'))

        #FLUJO DEL PROGRAMA:

        if opcion1 == '0':
            print('Saliendo del programa...')
            start = False

        elif opcion1 == '1':
            start2 = True
            while start2:
                submenu_canciones()
                print()
                opcion2 = input('Elige una opcion: ')

                if opcion2 == '0':
                    print('Saliendo al menu general...')
                    start2 = False

                elif opcion2 =='1':
                    pass #Anadimos canciones

                elif opcion2 =='2':
                    pass #eliminar cancion

                elif opcion2 =='3':
                    pass #mostrar canciones

                else:
                    opcion2 = input('Elige una opcion: ')


        elif opcion1 =='2':
            start3 = True
            while start3:
                submenu_playlists()
                opcion3 = input('Elige una opcion: ')

                if opcion3 == '0':
                    print('Saliendo al menu general...')
                    start3 = False





        else:
            opcion = (input('Elige una opcion:'))

#----------------------------------------------
main()
