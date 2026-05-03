import json
import os
#importamos clases que heredan del Contenido:
from clases.Contenido.canciones import Cancion
from clases.Contenido.album import Album
from clases.Contenido.contenido import Contenido
from clases.Contenido.playlist import ListaReproduccion
from datetime import date

#importamos clases que heredan del Artista:
from clases.Artistas.cantantes import Cantantes
from clases.Artistas.grupo import Grupos
from clases.Artistas.orquesta import Orquestas
from clases.Artistas.productor_musical import ProductorMusical

# ------------------------------------------------------------
# funciones auxiliares del main.

def menu_canciones():
    print("\n========== MENU CANCIONES ==========")
    print("(1) Añadir cancion")
    print("(2) Eliminar cancion")
    print("(3) Mostrar todas las canciones")
    print("(4) Filtrar canciones")
    print("(5) Buscar cancion")
    print("(0) Volver al menu general")
    print("===================================")


def menu_elegir_playlist():
    print("\n========== PLAYLISTS DISPONIBLES ==========\n")

    ruta_base = "archivos/playlists"
    playlists_disponibles = []
    contador = 1

    for archivo in os.listdir(ruta_base):
        if archivo.endswith(".json"):
            print(f"({contador}) {archivo.replace('.json','').replace('_',' ').title()}")
            playlists_disponibles.append(archivo)
            contador += 1

    print("\n------------------------------------------")
    print(f"({contador}) Crear nueva playlist")
    print("(0) Salir al menu general")
    print("==========================================")

    return playlists_disponibles, contador


def menu_playlists():
    print("\n========== MENU PLAYLIST ==========")
    print("(1) Mostrar informacion")
    print("(2) Añadir cancion a la playlist")
    print("(3) Eliminar cancion de la playlist")
    print("(4) Eliminar playlist")
    print("(0) Volver")
    print("==================================")


def menu_artista():
    print("\n========== MENU ARTISTA ==========")
    print("(1) Añadir artista")
    print("(2) Eliminar artista")
    print("(3) Buscar artista")
    print("(4) Mostrar todos los artistas")
    print("(0) Volver al menu general")
    print("=================================")


def menu_elegir_album():
    print("\n========== ALBUMES POR ARTISTA ==========\n")

    ruta_base = "archivos/albumes"
    artistas = [
        artista for artista in os.listdir(ruta_base)
        if os.path.isdir(f"{ruta_base}/{artista}")
    ]

    albumes_disponibles = []
    contador = 1

    for artista in artistas:
        print(artista.replace("_", " ").title())
        print("----------------------------------------")

        ruta_artista = f"{ruta_base}/{artista}"
        for archivo in os.listdir(ruta_artista):
            if archivo.endswith(".json"):
                print(f"({contador}) {archivo.replace('.json','').replace('_',' ').title()}")
                albumes_disponibles.append(f"{artista}/{archivo}")
                contador += 1

        print()

    print("----------------------------------------")
    print(f"({contador}) Crear nuevo album")
    print("(0) Salir al menu general")
    print("========================================")

    return albumes_disponibles, contador


def menu_album():
    print("\n========== MENU ALBUM ==========")
    print("(1) Mostrar informacion")
    print("(2) Mostrar canciones del album")
    print("(3) Eliminar album")
    print("(4) Añadir cancion al album")
    print("(5) Eliminar cancion del album")
    print("(0) Volver")
    print("================================")


def menu_productor_musical():
    print("\n========== MENU PRODUCTOR ==========")
    print("(1) Añadir nuevo productor")
    print("(2) Eliminar productor")
    print("(3) Buscar productor")
    print("(4) Mostrar todos los productores")
    print("(0) Volver al menu general")
    print("==================================")


def menu():
    print("\n========== BIBLIOTECA MUSICAL ==========")
    print("(1) Menu canciones")
    print("(2) Menu playlists")
    print("(3) Menu albumes")
    print("(4) Menu artistas")
    print("(5) Menu productor musical")
    print("(0) Salir")
    print("=======================================")


def pedir_opcion():
    return input("Elige una opcion: ").strip()



# ------------------------------------------------------------
#funcion principal del programa.

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


        # ------------------------------------------------------------
        #flujo del programa.

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
                while opcion_canciones not in ('0', '1', '2', '3', '4','5'):
                    print("Opcion no valida.")
                    opcion_canciones = pedir_opcion()

                # ------------------------------------------------------------

                if opcion_canciones == '0':
                    print('Saliendo al menu general...')
                    start1 = False

                # ------------------------------------------------------------

                elif opcion_canciones == '1':
                    print()
                    print('==== ANADIR CANCION ====')
                    titulo = input('Introduce el titulo de la cancion: ').strip()
                    artista = input('Introduce el autor de la cancion: ').strip()
                    feat_input = input("Introduce los artistas invitados (feat.), Enter si no hay: ").strip()
                    feat = [a.strip() for a in feat_input.split(",")] if feat_input else []
                    fecha_lanzamiento = input('Introduce el año de lanzamiento de la cancion: ').strip()
                    duracion = input('Introduce la duracion de la cancion: ').strip()
                    genero = [g.strip() for g in input('Introduce el genero(s) de la cancion: ').split(',')]
                    discografia = input('Introduce la discografia de la cancion: ').strip()

                    #creamos un objeto de la clase cancion para agregarlo a la base de datos.
                    cancion = Cancion(
                        titulo=titulo,
                        artista=artista,
                        fecha_lanzamiento=fecha_lanzamiento,
                        duracion=duracion,
                        genero=genero,
                        discografia=discografia,
                        feat=feat
                    )

                    Cancion.anadir_cancion(cancion, 'archivos/canciones_guardadas.json')
                    print(f"La cancion '{titulo}' de {artista} se ha guardado correctamente.")

                # ------------------------------------------------------------

                #eliminamos canciones de la base de datos.
                elif opcion_canciones == '2':
                    # pedimos datos para eliminar
                    titulo = input("Introduce el titulo de la cancion a borrar: ").strip()
                    artista = input("Introduce el autor de la cancion: ").strip()

                    print()
                    print("Buscando la cancion...")

                    #buscamos la cancion en la base de datos de las canciones segun el titulo y el artista.
                    cancion_encontrada = Cancion.buscar_cancion(titulo, artista)

                    #si no la encontramos:
                    if cancion_encontrada is None:
                        print(f"La cancion '{titulo.title()}' de {artista.title()} no existe en la base de datos.")

                    #si la encontramos:
                    else:
                        # nos aseguramos de que no ha sido missclisk
                        opcion_eliminar_cancion = input(f"Eliminar la cancion '{titulo.title()}' de {artista.title()}? (s/n): ").strip().lower()

                        # validamos la peticion
                        while opcion_eliminar_cancion not in ("s", "n"):
                            print("Opcion no valida. Solo puedes poner (s/n).")
                            opcion_eliminar_cancion = input(f"Eliminar la cancion '{titulo.title()}' de {artista.title()}? (s/n): ").strip().lower()

                        #si decimos que si:
                        if opcion_eliminar_cancion == "s":
                            print(f"Eliminando la cancion {titulo.title()}...")
                            Cancion.eliminar_cancion(titulo, artista)
                            print(f"Cancion '{titulo.title()}' eliminada correctamente.")
                        #si ha sido un missclick
                        else:
                            print("La eliminacion se ha canceldado.")

                # ------------------------------------------------------------

                #mostramos todas las canciones disponibles.
                elif opcion_canciones =='3':
                    print('Mostrando todas las canciones...')
                    print()
                    print(f'== LISTADO DE CANCIONES DISPONIBLES ==')
                    #mostramos el listado de todas las canciones en la base de datos.
                    Cancion.mostrar_canciones()

                # ------------------------------------------------------------

                #filtramos las canciones segun gustos.
                elif opcion_canciones =='4':
                    print('Filtrando las canciones...')
                    #codigo: buscar artista en la base de datos.
                    Cancion.filtrar_canciones()

                # ------------------------------------------------------------

                #en esta opcion vamos a busar solo una cancion concreta
                elif opcion_canciones =='5':

                    #pedimos los datos de la cancion al usuario.
                    titulo= input('Introduce el titulo de la cancion: ')
                    artista= input('Introduce el artista: ')

                    print()
                    print('Buscando la cancion...')
                    print(f'== CANCION ENCONTRADA ==')

                    #busacmos la cancion encontrada en la base de datos.
                    cancion_encontrada = Cancion.buscar_cancion(titulo,artista)
                    #mostramos info de la cancion encontarada.
                    Cancion.mostrar_cancion(cancion_encontrada)

        #AQUI ACABA LA PRIMERA OPCION (CANCIONES) ------------------------------------------------------------


        # cuando elegimos la opcion 2- la gestion de las playlists
        elif opcion_general =='2':
            start2 = True
            while start2:

                #llamamos la funcion que muestra el menu de las playlists
                playlists_disponibles, contador_playlist = menu_elegir_playlist()

                opcion_elegir_playlist = pedir_opcion()
                # nos aseguramos de que la opcion es valida dentro de las posibles.
                while not (opcion_elegir_playlist.isdigit() and 0 <= int(opcion_elegir_playlist) <= contador_playlist):
                    print("Opcion no valida.")
                    opcion_elegir_playlist = pedir_opcion()

                # la convertimos a entero para poder trabajar con los indices dinamicos (cambian en funcion de la cantidad de albumes)
                opcion_elegir_playlist = int(opcion_elegir_playlist)

                # ------------------------------------------------------------

                if opcion_elegir_playlist == 0:
                    print('Saliendo al menu de las playlists...')
                    start2 = False

                # ------------------------------------------------------------

                elif opcion_elegir_playlist == contador_playlist:
                    #codigo: crear playlist vacia (crear un archivo .json)
                    titulo = input('Introduce el nombre de la playlist: ')
                    fecha_lanzamiento = date.today().year
                    #duracion y genero por defecto vienen vacios.
                    playlist = ListaReproduccion(titulo,fecha_lanzamiento,duracion='0:00', genero=[])
                    playlist.guardar_playlist()

                    playlist.ruta_archivo = f"archivos/playlists/{titulo.lower().replace(' ', '_')}.json"

                # ------------------------------------------------------------

                #buscador de playlists.
                elif opcion_elegir_playlist == contador_playlist+1:
                    print('Buscando la playlist...')

                # ------------------------------------------------------------

                else:
                    # calculamos el indice del album (restamos 1 porque en python empieza en 0)
                    indice_playlist = opcion_elegir_playlist - 1
                    # del archivo con las rutas sacado de la funcion de elegir menu y elegimos el que nos muestra la eleccion del usuario.
                    ruta_playlist = playlists_disponibles[indice_playlist]
                    # usamos el metodo de seleccionar album pasandole la ruta del album que queremos cargar.
                    playlist_cargada = ListaReproduccion.seleccionar_playlist(ruta_playlist)

                    if playlist_cargada:
                        start_playlist = True
                        while start_playlist:

                            #muestramos el menu de album
                            menu_playlists()

                            #pedimos al usuaior una eleccion.
                            opcion_playlist = pedir_opcion()

                            #validamos la eleccion del usuario.
                            while opcion_playlist not in ('0', '1', '2', '3','4'):
                                print("Opcion no valida.")
                                #volvemos a pedir la opcion hasta que sea valida.
                                opcion_playlist = pedir_opcion()

                            # ------------------------------------------------------------

                            #opcion de salir al menu de las playlists.
                            if opcion_playlist == '0':
                                print('Saliendo al menu de las playlists...')
                                start_playlist = False

                            # ------------------------------------------------------------

                            #opcion de mostrar informacion de la playlist.
                            elif opcion_playlist == '1':
                                #codigo: mostrar informacion de la playlist elegida.
                                print('Mostrando informacion de la playlist...')
                                playlist_cargada.mostrar_info()

                            # ------------------------------------------------------------

                            #opcion de anadir cancion a la playlist elegida.
                            elif opcion_playlist == '2':
                                #codigo: anadir cancion a la playlist.
                                print(f'Anadiendo cancion a la playlist...')

                                print("\n=== ANADIR CANCION A LA PLAYLIST ===")

                                # pedimos al usuario los datos de la cancion que quiere anadir.
                                titulo_playlist = input("Introduce el titulo de la cancion: ").strip().lower()
                                artista_playlist = input("Introduce el artista de la cancion: ").strip().lower()

                                # buscamos la cancion que queremos anadir al album en la base de datos de las canciones.
                                cancion_playlist = Cancion.buscar_cancion(titulo_playlist,artista_playlist)

                                # si no encontramos ninguna cancion ofrecemos la opcion de crearla y anadirla directamente al album:
                                if cancion_playlist is None:
                                    print(f"La cancion '{titulo_playlist.title()}' - {artista_playlist.title()} no existe.")
                                    opcion_crear_cancion = input(
                                        f"Quieres crear la cancion '{titulo_playlist.title()}' a la base de datos? (s/n): ").strip().lower()

                                    # validamos la opcion del usuario
                                    while opcion_crear_cancion not in ('s', 'n'):
                                        print("Opcion no valida.")
                                        opcion_crear_cancion = input(
                                            f"Quieres crear la cancion '{titulo_playlist.title()}' a la base de datos? (s/n): ").strip().lower()

                                    # si el usuario quiere crear la cancion a la base de datos, la creamos.
                                    if opcion_crear_cancion == 's':
                                        print()
                                        print(f'Artista de la cancion: {artista_playlist}')
                                        print(f'Introduce el titulo de la cancion: {titulo_playlist}')
                                        feat_input = input(
                                            "Introduce los artistas invitados (feat.), Enter si no hay: ").strip()

                                        nueva_playlist = Cancion(
                                            titulo=titulo_playlist,
                                            fecha_lanzamiento=input("Introduce el año de lanzamiento: "),
                                            duracion=input("Introduce la duracion de la cancion: "),
                                            genero=[g.strip() for g in
                                                    input("Introduce los generos de la cancion (separado por comas): ").split(
                                                        ",")],
                                            artista=artista_playlist,
                                            discografia=input("Introduce la discografia: "),
                                            feat=[a.strip() for a in feat_input.split(",")] if feat_input else []
                                        )
                                        # con el metodo de la clase cancion, anaidmos la cancion creada a la base de datos.
                                        Cancion.anadir_cancion(nueva_playlist)
                                        print()
                                        print(f"La cancion '{titulo_playlist}' de {artista_playlist} se ha guardado correctamente.")
                                        # volvemos a buscar la cancion que queremos anadir en la base de datos.
                                        cancion_playlist = Cancion.buscar_cancion(nueva_playlist.titulo, nueva_playlist.artista)

                                        # si la encontramos, la anadimos.
                                        if cancion_playlist:
                                            playlist_cargada.anadir_cancion_existente(cancion_playlist)

                                        # si no la encontramos no pasa nada.
                                    # si el usuario no quiere crear la cancion a la base de datos.
                                    else:
                                        print(
                                            f"La cancion '{titulo_playlist.title()}' no se ha anadido al album '{playlist_cargada.titulo.title()}'.")
                                # si la cancion exisita antes en la base de datos, la anadimos directamente.

                                else:
                                    # convertimos dict a objeto Cancion
                                    cancion_obj = Cancion(
                                        cancion_playlist["Titulo"],
                                        cancion_playlist["Fecha de lanzamiento"],
                                        cancion_playlist["Duracion"],
                                        cancion_playlist["Genero"],
                                        cancion_playlist["Artista"],
                                        cancion_playlist["Discografia"]
                                    )

                                    playlist_cargada.anadir_cancion_existente(cancion_obj)



                            # ------------------------------------------------------------

                            #funcion de eliminar cancion de la playlist.
                            elif opcion_playlist == '3':
                                #codigo: eliminar cancion de la playlist.

                                #pedimos los datos de la cancion al usuario.
                                titulo_cancion = input('Introduce el titulo de la cancion a eliminar: ')
                                artista_cancion = input('Introduce el artista de la cancion a eliminar: ')

                                opcion_eliminar_cancion_playlist = input(
                                    f"Eliminar la cancion '{titulo_cancion.title()}' de {artista_cancion.title()}? (s/n): ").strip().lower()

                                # validamos la peticion
                                while opcion_eliminar_cancion_playlist not in ("s", "n"):
                                    print("Opcion no valida. Solo puedes poner (s/n).")
                                    opcion_eliminar_cancion_playlist = input(
                                        f"Eliminar la cancion '{titulo_cancion.title()}' de {artista_cancion.title()}? (s/n): ").strip().lower()

                                # si decimos que si:
                                if opcion_eliminar_cancion_playlist == "s":
                                    print(f"Eliminando la cancion {titulo_cancion.title()}...")
                                    playlist_cargada.eliminar_cancion_playlist(titulo_cancion, artista_cancion)
                                # si ha sido un missclick
                                else:
                                    print("La eliminacion se ha canceldado.")

                                print(f'Eliminando la cancion de la playlist...')

                            # ------------------------------------------------------------

                            #opcion de eliminar la playlist de la lista.
                            elif opcion_playlist == '4':
                                #codigo: eliminar la playlist.
                                # nos aseguramos de que el usuario de verdad quiere eliminar album.
                                opcion_eliminar_playlist = input(f"Eliminar playlist '{playlist_cargada.titulo.title()}'? (s/n): ").strip().lower()

                                # validamos la opcion del usuaior.
                                while opcion_eliminar_playlist not in ('s', 'n'):
                                    print("Opcian no valida. Solo puedes poner (s/n).")
                                    opcion_eliminar_playlist = input(
                                        f"Eliminar playlist '{playlist_cargada.titulo.title()}'? (s/n): ").strip().lower()

                                # el caso de que el usuario quiere eliminar el album.
                                if opcion_eliminar_playlist == 's':
                                    # eliminamos el album.
                                    ListaReproduccion.eliminar_playlist(playlist_cargada.titulo)
                                    # volvemos al menu de los albumes
                                    print('Saliendo al menu de las playlists...')
                                    start_playlist = False
                                print(f'Eliminando la playlist...')


        #AQUI ACABA LA SEGUNDA OPCION (PLAYLISTS) ------------------------------------------------------------


        #cuando elegimos en el menu principal 3- entramos en el gestor de albumes.
        elif opcion_general == '3':
            start3 = True
            while start3:

                #cargamos la lista de albumes disponibles calculadoes en el menu, devovlemos el contador para ver cuantas opciones de eleccion hay para validar.
                albumes_disponibles, crear_album = menu_elegir_album()

                #pedimos al usuario una opcion para elegir el album de los disponibles.
                opcion_elegir_album = pedir_opcion()

                #validamos las opciones
                while not (opcion_elegir_album.isdigit() and 0 <= int(opcion_elegir_album) <= crear_album):
                    print("Opcion no valida.")
                    opcion_elegir_album = pedir_opcion()

                #la convertimos a entero para poder trabajar con los indices dinamicos (cambian en funcion de la cantidad de albumes)
                opcion_elegir_album = int(opcion_elegir_album)

                # ------------------------------------------------------------

                #salimos al menu general con 0.
                if opcion_elegir_album == 0:
                    print("Saliendo al menu general...")
                    start3 = False

                # ------------------------------------------------------------

                #permitimos crear un album nuevo (creando asi tambien la carpeta para el artista si no existe todavia)
                elif opcion_elegir_album == crear_album:
                    print("\n==== CREAR ALBUM ====")

                    #pedimos los datos al usuario sobre el album a crear.
                    titulo = input("Introduce el titulo del album: ").strip().lower()
                    artista = input("Introduce el artista: ").strip().lower()

                    #creamos el album mediante el metodo creado en la clase album.
                    Album.crear_album(titulo, artista)

                # ------------------------------------------------------------

                #si el album ya existe
                else:
                    #calculamos el indice del album (restamos 1 porque en python empieza en 0)
                    indice = opcion_elegir_album - 1
                    #del archivo con las rutas sacado de la funcion de elegir menu y elegimos el que nos muestra la eleccion del usuario.
                    ruta_relativa = albumes_disponibles[indice]
                    #usamos el metodo de seleccionar album pasandole la ruta del album que queremos cargar.
                    album_cargado = Album.seleccionar_album(ruta_relativa)

                    #si se ha cargado el album correctamente:
                    if album_cargado:
                        start_album = True
                        while start_album:

                            #muestramos el menu de album
                            menu_album()

                            #pedimos al usuaior una eleccion.
                            opcion_album = pedir_opcion()

                            #validamos la eleccion del usuario.
                            while opcion_album not in ('0', '1', '2', '3', '4','5'):
                                print("Opcion no valida.")
                                #volvemos a pedir la opcion hasta que sea valida.
                                opcion_album = pedir_opcion()

                            # ------------------------------------------------------------

                            #salimos al menu de los albumes
                            if opcion_album == '0':
                                start_album = False
                                print('Saliendo al menu de los albumes...')

                            # ------------------------------------------------------------

                            #mostramos info del album seleccionado.
                            elif opcion_album == '1':
                                album_cargado.mostrar_info_album()

                            # ------------------------------------------------------------

                            #mostramos el listado de las canciones del album seleccionado.
                            elif opcion_album == '2':
                                album_cargado.mostrar_canciones_album()

                            # ------------------------------------------------------------

                            #permitimos opcion de eliminar album
                            elif opcion_album == '3':
                                #nos aseguramos de que el usuario de verdad quiere eliminar album.
                                opcion_eliminar_album = input(f"Eliminar album '{album_cargado.titulo.title()}'? (s/n): ").strip().lower()

                                #validamos la opcion del usuaior.
                                while opcion_eliminar_album not in ('s', 'n'):
                                    print("Opcian no valida. Solo puedes poner (s/n).")
                                    opcion_eliminar_album = input(f"Eliminar album '{album_cargado.titulo.title()}'? (s/n): ").strip().lower()

                                #el caso de que el usuario quiere eliminar el album.
                                if opcion_eliminar_album == 's':
                                    #eliminamos el album.
                                    album_cargado.eliminar_album()
                                    #volvemos al menu de los albumes
                                    print('Saliendo al menu de los albumes...')
                                    start_album = False

                                #si el usuario elige no, salimos al menu de los albumes.

                            # ------------------------------------------------------------

                            #opcion de canadir canion al album.
                            elif opcion_album == '4':
                                print("\n=== ANADIR CANCION AL ALBUM ===")

                                # pedimos al usuario los datos de la cancion que quiere anadir.
                                # El artista ya se concoe porque vamos a guardar en su carpeta, con lo cual no hace falta introducir el artista de nuevo.
                                artista = album_cargado.artista
                                print(f'Artista: {artista}')
                                titulo = input("Introduce el titulo de la cancion: ").strip()

                                # buscamos la cancion que queremos anadir al album en la base de datos de las canciones.
                                cancion_album = Cancion.buscar_cancion(titulo, artista)

                                # si no encontramos ninguna cancion ofrecemos la opcion de crearla y anadirla directamente al album:
                                if cancion_album is None:
                                    print(f"La cancion '{titulo.title()}' - {artista.title()} no existe.")
                                    opcion_crear_cancion = input(
                                        f"Quieres crear la cancion '{titulo.title()}' a la base de datos? (s/n): ").strip().lower()

                                    # validamos la opcion del usuario
                                    while opcion_crear_cancion not in ('s', 'n'):
                                        print("Opcion no valida.")
                                        opcion_crear_cancion = input(
                                            f"Quieres crear la cancion '{titulo.title()}' a la base de datos? (s/n): ").strip().lower()

                                    # si el usuario quiere crear la cancion a la base de datos, la creamos.
                                    if opcion_crear_cancion == 's':
                                        print()
                                        print(f'Artista de la cancion: {artista}')
                                        print(f'Introduce el titulo de la cancion: {titulo}')
                                        feat_input = input(
                                            "Introduce los artistas invitados (feat.), Enter si no hay: ").strip()

                                        nueva = Cancion(
                                            titulo=titulo,
                                            fecha_lanzamiento=input("Introduce el año de lanzamiento: "),
                                            duracion=input("Introduce la duracion de la cancion: "),
                                            genero=[g.strip() for g in
                                                    input("Introduce los generos de la cancion (separado por comas): ").split(",")],
                                            artista=artista,
                                            discografia=album_cargado.titulo,
                                            feat=[a.strip() for a in feat_input.split(",")] if feat_input else []
                                        )
                                        # con el metodo de la clase cancion, anaidmos la cancion creada a la base de datos.
                                        Cancion.anadir_cancion(nueva)
                                        print()
                                        print(f"La cancion '{titulo}' de {artista} se ha guardado correctamente.")
                                        # volvemos a buscar la cancion que queremos anadir en la base de datos.
                                        cancion_album = Cancion.buscar_cancion(nueva.titulo, nueva.artista)

                                        # si la encontramos, la anadimos.
                                        if cancion_album:
                                            album_cargado.anadir_cancion_existente(cancion_album)

                                        # si no la encontramos no pasa nada.
                                    # si el usuario no quiere crear la cancion a la base de datos.
                                    else:
                                        print( f"La cancion '{titulo.title()}' no se ha anadido al album '{album_cargado.titulo.title()}'.")
                                # si la cancion exisita antes en la base de datos, la anadimos directamente.
                                else:
                                    album_cargado.anadir_cancion_existente(cancion_album)

                            # ------------------------------------------------------------

                            #elegimos la opcion de eliminar una cancion del album.
                            elif opcion_album == '5':

                                #pedimos al usuario los datos para eliminar la cancion del album.
                                titulo = input("Introduce el titulo de la cancion a borrar: ").strip()
                                artista = album_cargado.artista

                                # nos aseguramos de que no ha sido missclisk
                                opcion_eliminar_cancion_album = input(f"Eliminar la cancion '{titulo.title()}' de {artista.title()}? (s/n): ").strip().lower()

                                # validamos la peticion
                                while opcion_eliminar_cancion_album not in ("s", "n"):
                                    print("Opcion no valida. Solo puedes poner (s/n).")
                                    opcion_eliminar_cancion_album = input(f"Eliminar la cancion '{titulo.title()}' de {artista.title()}? (s/n): ").strip().lower()

                                # si decimos que si:
                                if opcion_eliminar_cancion_album == "s":
                                    print(f"Eliminando la cancion {titulo.title()}...")
                                    album_cargado.eliminar_cancion_album(titulo,artista)
                                # si ha sido un missclick
                                else:
                                    print("La eliminacion se ha canceldado.")




        # AQUI ACABA LA TERCERA OPCION (ALBUMES) ------------------------------------------------------------


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

                # ------------------------------------------------------------

                #salimos al menu general
                if opcion_artista == '0':
                    print('Saliendo al menu general...')
                    start4 = False

                # ------------------------------------------------------------

                elif opcion_artista == '1':
                    #codigo: anadir artista a la base de datos
                    print(f'Añadiendo artista a la base de datos...')

                # ------------------------------------------------------------

                elif opcion_artista == '2':
                    #codigo: eliminar artista de la base de datos
                    print(f'Eliminando artista de la base de datos...')

                # ------------------------------------------------------------

                elif opcion_artista == '3':
                    print('Buscando artista...')
                    #codigo: buscar artista en la base de datos

                # ------------------------------------------------------------

                elif opcion_artista == '4':
                    print('Mostrando los artistas registrados...')
                    print(f'== ARTISTAS REGISTRADOS ==')
                    #codigo: mostrar todos los artistas de la base de datos.

                # ------------------------------------------------------------

        # AQUI ACABA LA CUARTA OPCION (ARTISTAS) ------------------------------------------------------------


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

                # ------------------------------------------------------------

                #analizamos las opciones:
                #salimos del programa.
                if opcion_productor == '0':
                    print('Saliendo al menu general...')
                    start5 = False

                # ------------------------------------------------------------

                #anadimos nuevo productor a la base de datos.
                elif opcion_productor == '1':
                    #codigo: anadir nuevo productor.
                    print('Añadiendo productor musical a la base de datos...')

                # ------------------------------------------------------------

                #eliminamos productor de la base de datos.
                elif opcion_productor == '2':
                    #codigo: eliminar productor
                    print('Eliminando productor de la base de datos...')

                # ------------------------------------------------------------

                #opcion de buscar productor.
                elif opcion_productor == '3':
                    print('Buscando el productor en la base de datos...')
                    #codigo: buscar productor

                # ------------------------------------------------------------

                #mostramos productor.
                elif opcion_productor == '4':
                    print('Mostrando todos los productores...')
                    #codigo: mostrar productor

                # ------------------------------------------------------------

        #AQUI ACABA LA OPCION 5 (PRODUCTOR MUSICAL) ------------------------------------------------------------
    # AQUI ACABA LA OPCION ZERO (BUCLE GENERAL)-------------------------------------------------------------------------------------------------

# ------------------------------------------------------------
#ejecucion del programa.
main()