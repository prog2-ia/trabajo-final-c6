import json
import os
from clases.Contenido.contenido import Contenido
from clases.Contenido.canciones import Cancion

# clase de lista de reproduccion.

# Clase ListaReproducion que hereda de Contenido
class ListaReproduccion(Contenido):
    def __init__(self, titulo, fecha_lanzamiento, duracion, genero, artista=None):
        super().__init__(titulo, fecha_lanzamiento, duracion, genero, artista or [])
        self._lista = []
        self._cargada = False
        self.canciones = []


    # ------------------------------------------------------------


    #Comprobar que lista sea del tipo lista
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


    #Metodo para guardar playlist
    def guardar_playlist(self):

        # la ruta del archivo vendra a partir de su nombre.
        nombre_archivo = self.titulo.lower().strip().replace(" ", "_")
        ruta = f"archivos/playlists/{nombre_archivo}.json"

        # si la ruta ya existe, no la tocamos.
        if os.path.exists(ruta):
            return

        #creamos un diccionario que vamos a guardar en el archivo json.
        playlist = {
            "titulo": self.titulo,
            "fecha_lanzamiento": self.fecha_lanzamiento,
            "duracion": '0:00',
            "genero": [],
            "artista": [],
            "canciones": []
        }

        #abrimos el json en modo escritura para guardar la playlist.
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(playlist, f, ensure_ascii=False, indent=4)

        print("Creando una playlist...")
        print(f"Playlist '{self.titulo}' creada y guardada en {ruta}")


    # ------------------------------------------------------------


    # funcion que nos sirve para cargar canciones de un archivo json.
    def cargar_canciones(self, ruta=None):

        #definimos por defecto la ruta para pasar por este paso.
        if ruta is None:
            #obtenemos la ruta a base del nombre de la playlist.
            nombre_archivo = self.titulo.lower().strip().replace(" ", "_")
            ruta = f"archivos/playlists/{nombre_archivo}.json"

        #controlamos si se han cargado las canciones a la lista.
        if self._cargada:
            return self._lista

        #hay que limpiar la lista antes de guardar las canciones para evitar los duplicatos.
        self._lista.clear()

        #abrimos el json para recorrer las canciones.
        with open(ruta, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        #recorremos las canciones de las canciones guardadas en json.
        for cancion in canciones:
            cancion1 = Cancion(
                cancion["Titulo"],
                cancion["Fecha de lanzamiento"],
                cancion["Duracion"],
                cancion["Genero"],
                cancion["Artista"],
                cancion["Discografia"]
            )
            self._lista.append(cancion1)

        #indicamos que la lista se ha cargado y la devolvemos.
        self._cargada = True
        return self._lista


    # ------------------------------------------------------------


    #metodo que nos permitira anadir canciones a la playlist.
    def anadir_cancion_existente(self, cancion):

        # normalizamos datos para comparar las canciones encontradas.
        titulo_nuevo = cancion["Titulo"].lower().strip()
        artista_nuevo = cancion["Artista"].lower().strip()

        # comprobamos si la cancion ya esta en la playlist.
        for c in self.canciones:
            if (c["Titulo"].lower().strip() == titulo_nuevo and c["Artista"].lower().strip() == artista_nuevo):
                print(f"La cancion '{cancion['Titulo']}' de {cancion['Artista']} ya esta en la playlist.")
                return False

        # anadimos la cancion a la lista de canciones.
        self.canciones.append(cancion)

        # volvemos a guardar la playlist con las canciones.
        playlist = {
            "titulo": self.titulo,
            "fecha_lanzamiento": self.fecha_lanzamiento,
            "duracion": self.duracion,
            "genero": self.genero,
            "canciones": self.canciones
        }


        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(playlist, f, ensure_ascii=False, indent=4)

        print(f"Cancion '{cancion['Titulo']}' añadida a la playlist '{self.titulo}'.")
        return True


    # ------------------------------------------------------------


    #Metodo para mostrar info
    def mostrar_info(self):
        super().mostrar_info()

        #necesitamos cargar las canciones para poder representarlos en un listado.
        if not self._cargada:
            self.cargar_canciones()

        #represetnamos el mencionado listado de las canciones.
        print("Lista de canciones:")
        if not self._lista:
            print("- (vacía)")
        else:
            for cancion in self._lista:
                print(f"- {cancion.titulo} — {cancion.artista} ({cancion.formatear_duracion()})")
        print()


    # ------------------------------------------------------------


    #metodo que nos permitira eliminar la playlist de la lista.
    @staticmethod
    def eliminar_playlist(nombre):

        # la ruta del archivo vendra a partir de su nombre.
        nombre = nombre.lower().strip().replace(" ", "_")
        ruta = f"archivos/playlists/{nombre}.json"

        #comprobamos si realmente existe la ruta (playlist) en la lista.
        if not os.path.exists(ruta):
            print(f'La playlist no existe, no se puede eliminar.')
            return

        #eliminamos la ruta de la playlist que queremos borrar.
        os.remove(ruta)

        print("Eliminando la playlist...")
        print(f"Playlist '{nombre}' eliminada correctamente.")


# ------------------------------------------------------------


    #funcion que nos permitira seleccionar una de las playlist de la lista entera en el menu.
    @staticmethod
    def seleccionar_playlist(ruta_relativa, ruta="archivos/playlists"):

        #calculamos la ruta completa del archivo
        ruta_completa = os.path.join(ruta, ruta_relativa)
        print(f"\nCargando playlist '{ruta_relativa}'...")

        #abrimos el archivo json con la ruta.
        with open(ruta_completa, "r", encoding="utf-8") as f:
            playlist = json.load(f)
            #diccionario.

        #obtenemos el nombre del archivo.
        #obtenemos el nombre de la playlist a partir de la ruta.
        titulo = ruta_relativa.replace(".json", "").replace("_", " ").title()

        #obtenemos la lista de las canciones, si no hay, ponemos una lista vacia por defecto.
        canciones = playlist

        #creamos un conjunto para guardar los generos y evistar los duplicatos.
        generos = set()
        for cancion in canciones:
            for genero in cancion.get("Genero", []):
                generos.add(genero)

        #igual que en el paso anterior.
        artistas = set()
        for cancion in canciones:
            artista = cancion.get("Artista")
            if artista:
                partes = artista.replace("feat.", "feat").split("feat")
                for parte in partes:
                    artistas.add(parte.strip())

        play = ListaReproduccion(
            titulo=titulo,
            fecha_lanzamiento=None,
            duracion="0:00",
            genero=list(generos),
            artista=list(artistas)
        )

        play.canciones = canciones
        play.ruta_archivo = ruta_completa
        return play


    # ------------------------------------------------------------


    #funcion que permitira mostarar los artista completos de las canciones. La sobreescribimos del contenido.
    def artista_completo(self):
        if not self.artista:
            return "varios"
        return ", ".join(self.artista)


    # ------------------------------------------------------------

