import json
from clases.Contenido.contenido import Contenido

# Clase Cancion
class Cancion(Contenido):
    # Clase Canción: hereda de Contenido.
    def __init__(self, titulo, fecha_lanzamiento, duracion, genero, artista, discografia, feat=None):
        super().__init__(titulo, fecha_lanzamiento, duracion, genero, artista,feat)
        self.discografia = discografia


    # ------------------------------------------------------------


    # Comprueba que discografia sea de tipo str
    @property
    def discografia(self):
        return self._discografia

    @discografia.setter
    def discografia(self, valor):
        if not isinstance(valor, str):
            raise TypeError("La discografía debe ser texto.")
        self._discografia = valor


    # ------------------------------------------------------------


    #Metodo estatico para añadir cancion nueva al archivo json.
    @staticmethod
    def anadir_cancion(nueva_cancion, ruta_json="archivos/canciones_guardadas.json"):

        # Cargamos el archivo json
        try:
            with open(ruta_json, "r", encoding="utf-8") as f:
                canciones = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta_json}")
        except json.JSONDecodeError:
            raise ValueError("El archivo JSON está corrupto o mal formado.")

        # Normalizamos para buscar duplicados
        titulo_nuevo = nueva_cancion.titulo.lower().strip()
        artista_principal_nuevo = nueva_cancion.artista.lower().strip()

        # recorremos el archivo buscando duplicatos.
        for cancion in canciones:
            titulo_guardado = cancion["Titulo"].lower().strip()
            artista_guardado_completo = cancion["Artista"]
            artista_principal_guardado, _ = Contenido.separar_artista_feat(artista_guardado_completo)

            if (titulo_guardado == titulo_nuevo and
                    artista_principal_guardado.lower().strip() == artista_principal_nuevo):
                raise ValueError(f"La cancion '{nueva_cancion.titulo.title()}' de {nueva_cancion.artista_completo()} ya existe en la base de datos.")

        # Si no hay duplicatos, anadimos la cancion.
        canciones.append(nueva_cancion.to_dict())

        #abrimos el archivo json en modo escritura y lo guardamos.
        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(canciones, f, ensure_ascii=False, indent=4)


    # ------------------------------------------------------------


    #metodo para eliminar canciones de la base de datos.
    @staticmethod
    def eliminar_cancion(titulo, artista, ruta_json="archivos/canciones_guardadas.json"):

        #cargamos el archivo json.
        try:
            with open(ruta_json, "r", encoding="utf-8") as f:
                canciones = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta_json}")
        except json.JSONDecodeError:
            raise ValueError("El archivo JSON está corrupto o mal formado.")

        #normalizamos los datos introducidos.
        titulo = titulo.lower().strip()
        artista = artista.lower().strip()

        #calculamos la cantidad de canciones para confirmar que se ha equivocado.
        canciones_antes = len(canciones)
        canciones_filtradas = []

        #recorremos el archivo buscando la cancion a eliminar.
        for cancion in canciones:
            titulo_cancion = cancion["Titulo"].lower().strip()
            artista_completo_cancion = cancion["Artista"]

            #obtenemos el artista principal de la cancion, feats no nos importan.
            artista_principal_cancion, _ = Contenido.separar_artista_feat(artista_completo_cancion)

            #si coincide, procedemos a guardar en la lista para eliminar y elimiar.
            if not (titulo_cancion == titulo and artista_principal_cancion.lower().strip() == artista):
                canciones_filtradas.append(cancion)

        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(canciones_filtradas, f, ensure_ascii=False, indent=4)

        if len(canciones_filtradas) == canciones_antes:
            print(f"La cancion '{titulo}' de {artista} no existe en la base de datos.")
        else:
            print(f"Cancion '{titulo}' de {artista} eliminada correctamente.")


    #------------------------------------------------------------


    #metodo para mostrar TODAS las canciones disponibles de la base de datos.
    @staticmethod
    def mostrar_canciones(ruta_json="archivos/canciones_guardadas.json"):

        # Archivo json donde estan las canciones
        try:
            with open(ruta_json, "r", encoding="utf-8") as f:
                canciones = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta_json}")
        except json.JSONDecodeError:
            raise ValueError("El archivo JSON está corrupto o mal formado.")

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
        try:
            with open(ruta_json, "r", encoding="utf-8") as f:
                canciones = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta_json}")
        except json.JSONDecodeError:
            raise ValueError("El archivo JSON está corrupto o mal formado.")

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
        #si encontontramos la cancion, la mostramos.
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

        #abrimos archivo json para recorrer canciones.
        try:
            with open(ruta_json, "r", encoding="utf-8") as f:
                canciones = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta_json}")
        except json.JSONDecodeError:
            raise ValueError("El archivo JSON está corrupto o mal formado.")

        #normalizamos los datos introducidos por el usuario.
        titulo = titulo.lower().strip()
        artista = artista.lower().strip()

        #recorremos el archivo en busqueda de las canciones.
        for cancion in canciones:
            titulo_guardado = cancion["Titulo"].lower().strip()
            artista_completo_guardado = cancion["Artista"]

            #separamos el artista principal de los invitados. usamos _ porque la funcion de separar devuelve lista de los invitados que no nos interesa en este caso.
            artista_principal, _ = Contenido.separar_artista_feat(artista_completo_guardado)

            #si encontramos la cancion cuyo titulo y artista principal encaja con lo introducido, lo devolvemos.
            if titulo_guardado == titulo and artista_principal.lower().strip() == artista:
                return cancion

        #si no, nada.
        return None

    # ------------------------------------------------------------

    #funcion que nos asegura que la cancion que introducimos siempre sera un diccioanrio para no tener errores a la hora de anadir canciones a los archivos json.
    def to_dict(self):
        return {
            "Titulo": self.titulo.title(),
            "Artista": self.artista_completo(),
            "Fecha de lanzamiento": self.fecha_lanzamiento,
            "Duracion": self.formatear_duracion(),
            "Genero": self.genero,
            "Discografia": self.discografia.title()
        }




