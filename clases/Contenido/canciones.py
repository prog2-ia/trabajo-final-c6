import json
from clases.Contenido.contenido import Contenido

# Clase Cancion
class Cancion(Contenido):
    # Clase Canción: hereda de Contenido.
    def __init__(self, titulo, fecha_lanzamiento, duracion, genero, artista, discografia):
        super().__init__(titulo, fecha_lanzamiento, duracion, genero, artista)
        self.discografia = discografia


    # ------------------------------------------------------------


    # Comprueba que discografia sea de tipo str
    @property
    def discografia(self):
        return self._discografia

    @discografia.setter
    def discografia(self, valor):
        if not isinstance(valor, str):
            print("La discografía debe ser texto.")
            self._discografia = "desconocida"
        else:
            self._discografia = valor


    # ------------------------------------------------------------


    #Metodo estatico para añadir cancion nueva al archivo json.
    @staticmethod
    def anadir_cancion(nueva_cancion, ruta_json="archivos/canciones_guardadas.json"):

        #cargamos el archivo json para poder buscar si no hay duplicato.
        with open(ruta_json, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        #normalizamos el titulo y el artista para poder buscar.
        titulo_nuevo = nueva_cancion.titulo.lower().strip()
        artista_nuevo = nueva_cancion.artista.lower().strip()

        #buscamos si la cancion ya existe en la base de datos.
        for cancion in canciones:
            if cancion["Titulo"].lower().strip() == titulo_nuevo and cancion["Artista"].lower().strip() == artista_nuevo:
                print(
                    f"La cancion '{nueva_cancion.titulo.title()}' de {nueva_cancion.artista.title()} ya existe en la base de datos.")
                #salimos al menu sin anaidr nada para no tener duplicatos.
                return None

        #Si no hay cancion en la base de datos, podemos anadirla.
            #pedimos datos al usuario.
        canciones.append({
            "Titulo": nueva_cancion.titulo.title(),
            "Artista": nueva_cancion.artista.title(),
            "Fecha de lanzamiento": nueva_cancion.fecha_lanzamiento,
            "Duracion": nueva_cancion.formatear_duracion(),
            "Genero": nueva_cancion.genero.title(),
            "Discografia": nueva_cancion.discografia.title()
        })

        #abrimos el archivo json en modo escritura para guardar la cancion.
        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(canciones, f, ensure_ascii=False, indent=4)

        print(f"Cancion '{nueva_cancion.titulo.title()}' anadida correctamente a la base de datos.")


    # ------------------------------------------------------------


    #metodo para eliminar canciones de la base de datos.
    @staticmethod
    def eliminar_cancion(titulo,artista,ruta_json="archivos/canciones_guardadas.json"):

        # Archivo json donde estan las canciones
        with open(ruta_json, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        #recorremos el archivo json buscando el titulo y artista para borrar.
        canciones_antes = len(canciones)
        canciones = [cancion for cancion in canciones if not (cancion["Titulo"].lower() == titulo.lower() and cancion["Artista"].lower() == artista.lower())]

        #abrimos el archivo json en modo escritura para eliminar la cancion de la base de datos.
        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(canciones, f, ensure_ascii=False, indent=4)

        #calculamos cuantas canciones hay y cuandas habia para mostrar info de que se ha eliminado correctamente.
        if len(canciones) == canciones_antes:
            print(f"La cancion '{titulo}' no existe en la base de datos.")
        else:
            print(f"Cancion '{titulo}' de {artista} eliminada correctamente.")


    #------------------------------------------------------------


    #metodo para mostrar TODAS las canciones disponibles de la base de datos.
    @staticmethod
    def mostrar_canciones(ruta_json="archivos/canciones_guardadas.json"):

        # Archivo json donde estan las canciones
        with open(ruta_json, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        #recorremos el archivo json y vamos imprimiendo todas las canciones una por una.
        for cancion in canciones:
            print(f"\t -  {cancion['Titulo']} -  {cancion['Artista']} - ({cancion['Duracion']})")


    # ------------------------------------------------------------


    #metodo para mostrar UNA SOLA cancion.
    @staticmethod
    def mostrar_cancion(cancion):
        print(f"Titulo: {cancion['Titulo']}")
        print(f"Artista: {cancion['Artista']}")
        print(f"Fecha de lanzamiento: {cancion['Fecha de lanzamiento']}")
        print(f"Duracion: {cancion['Duracion']}")
        print(f"Genero(s): {', '.join(cancion['Genero'])}")
        print(f"Discografia: {cancion['Discografia']}")
        print("========================\n")


    # ------------------------------------------------------------


    #metodo que sirve para filtrar cancioens.
    @staticmethod
    def filtrar_canciones(ruta_json="archivos/canciones_guardadas.json"):

        #abrimos el archivo json de la ruta en modo lectura.
        with open(ruta_json, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        #empezamos pedir informaicon para la busqueda de la cancion.
        print("\n==== FILTRAR CANCIONES ====")
        titulo = input("Filtrar por título (enter para omitir): ").strip().lower()
        artistas_busqueda = input("Filtrar por artista(s) separados por coma (enter para omitir): ").strip().lower()
        artistas = [artista.strip() for artista in artistas_busqueda.split(",")] if artistas_busqueda else []
        generos_busqueda = input("Filtrar por genero(s) separados por coma (enter para omitir): ").strip().lower()
        generos = [genero.strip() for genero in generos_busqueda.split(",")] if generos_busqueda else []
        discografia = input("Filtrar por discografía (enter para omitir): ").strip().lower()

        #si no intrduciomos ningun filtro, es decir metemos _todo enter.
        if not titulo and not artistas and not generos and not discografia:
            print("\n==== RESULTADOS DEL FILTRADO ====")
            print("No se ha introducido ningun filtro.")
            return None

        #preparamos una lista donde vamos a guardar los resultados encontrados.
        resultados = []

        #recorremos archivo json en busqueda de las canciones caracteristca una por una.
        for cancion in canciones:
            coincide = True

            #en caso de que titulo coincida
            if titulo and titulo not in cancion['Titulo'].lower():
                coincide = False

            #podemos introducir varios artistas (la misma logica que con genero)
            if artistas:
                coincide_artista = False
                artista_cancion = cancion['Artista'].lower()

                for artista_introducido in artistas:
                    if artista_introducido in artista_cancion:
                        coincide_artista = True

                if not coincide_artista:
                    coincide = False

            # podemos introdcir varios generos.
            if generos:
                generos_normalizados = [gen.lower() for gen in cancion["Genero"]]
                coincide_genero = False

                for genero_introducido in generos:

                    for genero_de_cancion in generos_normalizados:
                        if genero_introducido in genero_de_cancion:
                            coincide_genero = True

                if not coincide_genero:
                    coincide = False

            #comprobamos la discografia
            if discografia and discografia not in cancion['Discografia'].lower():
                coincide = False

            #si alguna cancion coincide con los filtros, anadimos a la lista de resultados.
            if coincide:
                resultados.append(cancion)

        #mostramos los resultados.
        print("\n==== RESULTADOS DEL FILTRADO ====\n")

        #si no encontramos ningun resultado.
        if not resultados:
            print("No se encontraron canciones que coincidan con los filtros aplicados.")

        #si encontramos algun resultado, lo mostramos.
        else:
            for cancion_encontrada in resultados:
                print(f"{cancion_encontrada['Titulo']} — {cancion_encontrada['Artista']} - ({cancion_encontrada['Duracion']})")
                print(f"Generos: {', '.join(cancion_encontrada['Genero'])}")
                print(f"Discografia: {cancion_encontrada['Discografia']}")
                print("-------------------------------------------")


    # ------------------------------------------------------------


    #metodo nos permite buscar canciones (para agragar al album)
    @staticmethod
    def buscar_cancion(titulo, artista, ruta_json="archivos/canciones_guardadas.json"):

        #abrimos el archivo json en modo lectura para buscar cancion.
        with open(ruta_json, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        #guardamos el titulo y el artista de la cancion que ha introducido el usuario.
        titulo = titulo.lower().strip()
        artista = artista.lower().strip()

        #recorremos el archivo json en busqueda de la cancion con los parametros indicados.
        for cancion in canciones:
            if cancion["Titulo"].lower() == titulo and cancion["Artista"].lower() == artista:
                #si la encontramos, la devolvemos.
                return cancion
        #si no, no devolvemos nada.
        return None

    # ------------------------------------------------------------



