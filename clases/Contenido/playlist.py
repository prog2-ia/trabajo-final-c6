import json
import os
from clases.Contenido.contenido import Contenido
from clases.Contenido.canciones import Cancion
from datetime import date

# clase de lista de reproduccion.

# Clase ListaReproducion que hereda de Contenido
class ListaReproduccion(Contenido):
    def __init__(self, titulo, fecha_lanzamiento, duracion, genero, artista=None):
        super().__init__(titulo, fecha_lanzamiento, duracion, genero, artista or [])
        self._lista = []          # lista interna de objetos Cancion
        self._cargada = False     # indica si la playlist esta cargada desde el json


    # ------------------------------------------------------------

    #metodo nos servira para sincronizar los generos de las playlists con las canciones.
    def _sincronizar_generos(self):
        generos = set()
        for c in self._lista:
            for g in c.genero:
                generos.add(g)
        self.genero = sorted(list(generos))

    # ------------------------------------------------------------


    # Comprobar que lista sea del tipo lista
    @property
    def lista(self):
        return self._lista

    @lista.setter
    def lista(self, valor):
        if not isinstance(valor, list):
            print("La lista debe ser una lista de canciones.")
            self._lista = []
        else:
            self._lista = valor


    # ------------------------------------------------------------


    #funcion que va a guardar la playlist despues de crearla en una ruta especifica, hecha en la misma funcion.
    def guardar_playlist(self):

        #creamos la ruta a partir del nombre de la playlist.
        nombre_archivo = self.titulo.lower().strip().replace(" ", "_")
        ruta = f"archivos/playlists/{nombre_archivo}.json"

        #nos aseguramos de que la ruta ya no existe (evitamos duplicatos)
        if os.path.exists(ruta):
            return

        #guardamos el archivo corresponediente.
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)

        self.ruta_archivo = ruta

        print("Creando una playlist...")
        print(f"Playlist '{self.titulo}' creada y guardada en {ruta}")


    # ------------------------------------------------------------


    #metodo para cargar canciones a una lista de una playlist.
    def cargar_canciones(self, ruta=None):

        #nos aseguramos que la ruta es correcta.
        if ruta is None:
            nombre_archivo = self.titulo.lower().strip().replace(" ", "_")
            ruta = f"archivos/playlists/{nombre_archivo}.json"

        #controlamos si la lista se ha cargado de las canciones.
        if self._cargada:
            return self._lista

        self._lista.clear()

        #abrimos el archivo para recorrerlo en busqueda de las canciones.
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read().strip()

            #si la playlist esta vacia
            if not contenido:
                #devolvemos una lista vacia.
                canciones = []
            else:
                #si no, devolvemos las canciones que contiene.
                canciones = json.loads(contenido)

        #recorremos la lista, para cada cancion guardaremos los datos recogidos del json.
        for c in canciones:
            if not isinstance(c, dict):
                continue

            self._lista.append(
                Cancion(
                    c["Titulo"],
                    c["Fecha de lanzamiento"],
                    c["Duracion"],
                    c["Genero"],
                    c["Artista"],
                    c["Discografia"]
                )
            )

        #sincronizamos los generos a parir de los generos de las canciones en la playlist.
        self._sincronizar_generos()
        self._sincronizar_artistas()

        #afirmamos que la lista se ha cargado y devolvemos la lista de canciones.
        self._cargada = True
        return self._lista


    # ------------------------------------------------------------


    #funcion que pemite anadir canciones a la playlist.
    def anadir_cancion_existente(self, cancion):

        #pasamos la cancion de ser un diccionario a ser un objeto de la clase cancion.
        if isinstance(cancion, dict):
            cancion = Cancion(
                cancion["Titulo"],
                cancion["Fecha de lanzamiento"],
                cancion["Duracion"],
                cancion["Genero"],
                cancion["Artista"],
                cancion["Discografia"]
            )

        #recorremos la lsita para asegurarnos que no habra duplicatos en la playlist.
        for c in self._lista:
            if c == cancion:
                print(f"La cancion '{cancion.titulo}' ya esta en la playlist.")
                return False

        #si no se repite, anadimos a la lista.
        self._lista.append(cancion)

        #sincronizamos los generos de la playlist a base de los de las canciones.
        self._sincronizar_generos()
        self._sincronizar_artistas()

        #ya tenemos los datos guardados, cambiamos el estado de cargda.
        self._cargada = True

        #guardamos archivo json con las canciones anadidas.
        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self._lista],f,ensure_ascii=False, indent=4)

        print(f"Cancion '{cancion.titulo}' añadida a la playlist '{self.titulo}'.")
        return True


    # ------------------------------------------------------------


    #funcion para mostrar info de la playlist.
    def mostrar_info(self):
        print("\n" + "=" * 40)
        print("        INFORMACIÓN DE LA PLAYLIST")
        print("=" * 40)

        #utilizamos la herencia para mostrar info del padre.
        super().mostrar_info()

        #para mostrar info neceistmaos cargar las canciones.
        if not self._cargada:
            self.cargar_canciones()

        # sincronizmos el genero.
        self._sincronizar_generos()

        print(f"Número de canciones: {len(self._lista)}")

        print("\nLista de canciones:")

        if not self._lista:
            print("- (vacía)")
        else:
            for c in self._lista:
                print(f"- {c.titulo} — {c.artista} ({c.formatear_duracion()})")

        print("=" * 40 + "\n")


    # ------------------------------------------------------------


    #funcion para eliminar la playlist entera de la base de datos.
    @staticmethod
    def eliminar_playlist(nombre):

        #a base del nombre introducido calculamos la ruta.
        nombre = nombre.lower().strip().replace(" ", "_")
        ruta = f"archivos/playlists/{nombre}.json"

        #comprobamos que la ruta a eliminar exitste.
        if not os.path.exists(ruta):
            print("La playlist no existe, no se puede eliminar.")
            return

        #eliminamos la ruta.
        os.remove(ruta)
        print(f"Playlist '{nombre}' eliminada correctamente.")


    # ------------------------------------------------------------


    #metodo para buscar playlists en la carpeta donde las guardamos.
    @staticmethod
    def buscar_playlist(titulo):

        #preparamos el titulo para la busqueda.
        titulo_normalizado = titulo.strip().lower().replace(' ','_')

        #indicamos la carpeta donde estan las playlists.
        carpeta = 'archivos/playlists'

        #recorremos la carpteta y buscamos si alguna coincide con el nombre preparado anteriormente.
        for playlist in os.listdir(carpeta):
            if playlist == titulo_normalizado + ".json":
                ruta = os.path.join(carpeta, playlist)
                print(f"La playlist '{titulo.title()}' encontrada correctamente. ")
                return ruta

        print(f"La playlist '{titulo.title()}' no existe en la base de datos. ")
        return None


    # ------------------------------------------------------------


    #funcion que nos sirve para obtener el artista completo (junto con feat.)
    def artista_completo(self):
        if not self.artista:
            return "varios"

        if isinstance(self.artista, str):
            return self.artista

        return ", ".join(self.artista)


    # ------------------------------------------------------------


    # con esta funcion cargaremos la playlist dada la ruta.
    @staticmethod
    def cargar_playlist(ruta):
        # intentamos conseguir los datos de la ruta.
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
        # manejamos los posibles errores que podrian ocurrir.
        except FileNotFoundError:
            raise FileNotFoundError(f"No se ha encontrado el archivo: {ruta}")
        except json.JSONDecodeError:
            raise ValueError("El archivo JSON esta corrupto o mal formado.")

        # la playlist es una lista de diccionarios, entonces tiene que ser una lista obligatoriamente.
        if not isinstance(datos, list):
            raise ValueError("La playlist debe ser una lista de canciones.")

        # obtenemos el nombre del archivo a base de la ruta y lo usamos para crear el titulo de la playlist para guardar lo en los datos.
        nombre = os.path.basename(ruta).replace(".json", "")
        titulo = nombre.replace("_", " ").title()

        # creamos una platlist vacia.
        playlist = ListaReproduccion(
            titulo=titulo,
            fecha_lanzamiento=date.today().year,
            duracion="0:00",
            genero=[],
            artista=[]
        )

        # en ella, reconstruimos las canciones a base de la informacion del json.
        playlist._lista = [
            Cancion(
                c["Titulo"],
                c["Fecha de lanzamiento"],
                c["Duracion"],
                c["Genero"],
                c["Artista"],
                c["Discografia"]
            )
            for c in datos if isinstance(c, dict)
        ]

        # sincronizamos los artistas de la playlist con las de canicones.
        artistas = set()
        for c in playlist._lista:
            principal, _ = Contenido.separar_artista_feat(c.artista)
            if principal:
                artistas.add(principal.title())

        playlist.artista = ", ".join(sorted(artistas))

        # sincronizmos los datos (genero).
        playlist._sincronizar_generos()

        playlist.ruta_archivo = ruta
        playlist._cargada = True

        # devolvemos el objeto playlist.
        return playlist


    # ------------------------------------------------------------


    # funcion para seleccionar la playlist del menu.
    @staticmethod
    def seleccionar_playlist(ruta_relativa, ruta="archivos/playlists"):

        # obtenemos la ruta completa de la playlist.
        ruta_completa = os.path.join(ruta, ruta_relativa)

        print(f"\nCargando playlist '{ruta_relativa}'...")

        # obtenemos el titulo a base de la ruta.
        titulo = ruta_relativa.replace(".json", "").replace("_", " ").title()

        # cargamos las canciones de la playlist en una lista.
        with open(ruta_completa, "r", encoding="utf-8") as f:
            contenido = f.read().strip()

            if not contenido:
                canciones = []
            else:
                canciones = json.loads(contenido)

        # creamos un objeto de playlist vacia.
        play = ListaReproduccion(
            titulo=titulo,
            fecha_lanzamiento=date.today().year,
            duracion="0:00",
            genero=[],
            artista=[]
        )

        # rellenamos la playlist con los datos recogidos.
        play._lista = [
            Cancion(
                c["Titulo"],
                c["Fecha de lanzamiento"],
                c["Duracion"],
                c["Genero"],
                c["Artista"],
                c["Discografia"]
            )
            for c in canciones
            if isinstance(c, dict)
        ]

        # sincronizamos los artistas de la playlist con las canciones.
        artistas = set()
        for c in play._lista:
            principal, _ = Contenido.separar_artista_feat(c.artista)
            if principal:
                artistas.add(principal.title())

        play.artista = ", ".join(sorted(artistas))

        # sincronizamos los generos.
        play._sincronizar_generos()

        play.ruta_archivo = ruta_completa
        play._cargada = True

        return play


    # ------------------------------------------------------------


    # funcion para eliminar una cancion de la playlist
    def eliminar_cancion_playlist(self, titulo, artista):

        eliminada = False

        # recorremos la lista y eliminamos la cancion que coincide
        nueva_lista = []
        for c in self._lista:
            if c.titulo.lower().strip() == titulo.lower().strip() and c.artista.lower().strip() == artista.lower().strip():
                eliminada = True
                continue
            nueva_lista.append(c)

        # actualizamos la lista
        self._lista = nueva_lista

        if not eliminada:
            print(f"La cancion '{titulo}' de {artista} no se encuentra en la playlist.")
            return False

        # sincronizamos los generos
        self._sincronizar_generos()

        # sincronizamos los artistas
        artistas = set()
        for c in self._lista:
            principal, _ = Contenido.separar_artista_feat(c.artista)
            if principal:
                artistas.add(principal.title())

        self.artista = ", ".join(sorted(artistas))

        self._cargada = True

        # guardar cambios en json
        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self._lista], f, ensure_ascii=False, indent=4)

        print(f"Cancion '{titulo}' eliminada de la playlist '{self.titulo}'.")
        return True


    # ------------------------------------------------------------


    #fuincion sirve para sincronizar artistas en con la playlist.
    def _sincronizar_artistas(self):
        artistas = set()

        for c in self._lista:
            principal, _ = Contenido.separar_artista_feat(c.artista)
            if principal:
                artistas.add(principal.title())

        self.artista = ", ".join(sorted(artistas))