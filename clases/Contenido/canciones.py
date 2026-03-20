import json
from clases.Contenido.contenido import Contenido

# Clase Cancion
class Cancion(Contenido):
    # Clase Canción: hereda de Contenido.
    def __init__(self, titulo, fecha_lanzamiento, duracion, genero, artista, discografia):
        super().__init__(titulo, fecha_lanzamiento, duracion, genero, artista)
        self.discografia = discografia

    # -------------------- PROPIEDADES --------------------

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

    # -------------------- MÉTODOS --------------------
    #Metodo para mostrar la informacion
    def mostrar_info(self):
        print("==== CANCION ====")
        super().mostrar_info()
        print(f"Discografia: {self.discografia}")

    #Metodo estatico para añadir cancion nueva al archivo json.
    @staticmethod
    def anadir_cancion(nueva_cancion, ruta_json="archivos/canciones_guardadas.json"):

        #Archivo json donde estan las canciones
        with open(ruta_json, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        #nos sirve para compobar si la cancion se ha anadido.
        canciones_antes = len(canciones)
        #Añade la cancion al archivo
        canciones.append({
            "Titulo": nueva_cancion.titulo,
            "Artista": nueva_cancion.artista,
            "Fecha de lanzamiento": nueva_cancion.fecha_lanzamiento,
            "Duracion": nueva_cancion.formatear_duracion(),
            "Genero": nueva_cancion.genero,
            "Discografia": nueva_cancion.discografia
        })

        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(canciones, f, ensure_ascii=False, indent=4)

        if len(canciones) == canciones_antes:
            print('La cancion no se ha anadido a la base de datos. ')
        else:
            print(f"Canción '{nueva_cancion}' añadida correctamente.")

    #------------------------------------------------------------

    #metodo para eliminar canciones de la base de datos.
    @staticmethod
    def eliminar_cancion(titulo,artista,ruta_json="archivos/canciones_guardadas.json"):

        # Archivo json donde estan las canciones
        with open(ruta_json, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        #recorremos el archivo json buscando el titulo y artista para borrar.
        canciones_antes = len(canciones)
        canciones = [c for c in canciones if not (
                    c["Titulo"].lower() == titulo.lower() and
                    c["Artista"].lower() == artista.lower()
            )]

        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(canciones, f, ensure_ascii=False, indent=4)

        if len(canciones) == canciones_antes:
            print('La cancion no existe en la base de datos.')
        else:
            print(f"Canción '{titulo}' de '{artista}' eliminada correctamente.")

    #------------------------------------------------------------

    #metodo para mostrar todas las canciones disponibles de la base de datos.
    @staticmethod
    def mostrar_canciones(ruta_json="archivos/canciones_guardadas.json"):

        # Archivo json donde estan las canciones
        with open(ruta_json, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        for cancion in canciones:
            print(f"\t -  {cancion['Titulo']} -  {cancion['Artista']} - ({cancion['Duracion']})")

    # ------------------------------------------------------------

    #metodo que sirve para filtrar cancioens.
    @staticmethod
    def filtrar_canciones(ruta_json="archivos/canciones_guardadas.json"):

        with open(ruta_json, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        print("\n==== FILTRAR CANCIONES ====")
        titulo = input("Filtrar por título (enter para omitir): ").strip().lower()
        artistas_busqueda = input("Filtrar por artista(s) separados por coma (enter para omitir): ").strip().lower()
        artistas = [a.strip() for a in artistas_busqueda.split(",")] if artistas_busqueda else []
        generos_busqueda = input("Filtrar por género(s) separados por coma (enter para omitir): ").strip().lower()
        generos = [g.strip() for g in generos_busqueda.split(",")] if generos_busqueda else []
        discografia = input("Filtrar por discografía (enter para omitir): ").strip().lower()

        if not titulo and not artistas and not generos and not discografia:
            print("\n==== RESULTADOS DEL FILTRADO ====")
            print("No se ha introducido ningún filtro.")
            return

        resultados = []

        #recorremos archivo json en busqueda de las canciones.
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
                generos_normalizados = [g.lower() for g in cancion["Genero"]]
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
            print("No se encontraron canciones que coincidan con los filtros.")
        else:
            for cancion_encontrada in resultados:
                print(f"{cancion_encontrada['Titulo']} — {cancion_encontrada['Artista']} - ({cancion_encontrada['Duracion']})")
                print(f"Géneros: {', '.join(cancion_encontrada['Genero'])}")
                print(f"Discografía: {cancion_encontrada['Discografia']}")
                print("-------------------------------------------")

