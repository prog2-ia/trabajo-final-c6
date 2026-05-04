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


    # Metodo para guardar playlist
    def guardar_playlist(self):

        # la ruta del archivo vendra a partir de su nombre
        nombre_archivo = self.titulo.lower().strip().replace(" ", "_")
        ruta = f"archivos/playlists/{nombre_archivo}.json"

        # si la ruta ya existe, no la tocamos
        if os.path.exists(ruta):
            return

        # abrimos el json en modo escritura para guardar una playlist vacia
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)

        self.ruta_archivo = ruta

        print("Creando una playlist...")
        print(f"Playlist '{self.titulo}' creada y guardada en {ruta}")


    # ------------------------------------------------------------


    # funcion que nos sirve para cargar canciones de un archivo json
    def cargar_canciones(self, ruta=None):

        # definimos por defecto la ruta
        if ruta is None:
            nombre_archivo = self.titulo.lower().strip().replace(" ", "_")
            ruta = f"archivos/playlists/{nombre_archivo}.json"

        # si ya esta cargada, no volvemos a cargar
        if self._cargada:
            return self._lista

        # limpiamos la lista antes de cargar
        self._lista.clear()

        # abrimos el json para recorrer las canciones
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read().strip()

            # si el archivo esta vacio, asumimos playlist vacia
            if not contenido:
                canciones = []
            else:
                canciones = json.loads(contenido)

        # creamos objetos Cancion a partir del json
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

        # marcamos la lista como cargada
        self._cargada = True
        return self._lista


    # ------------------------------------------------------------


    # metodo que nos permitira anadir canciones a la playlist
    # acepta un objeto Cancion o un diccionario
    def anadir_cancion_existente(self, cancion):

        # si llega un diccionario, lo convertimos a objeto Cancion
        if isinstance(cancion, dict):
            cancion = Cancion(
                cancion["Titulo"],
                cancion["Fecha de lanzamiento"],
                cancion["Duracion"],
                cancion["Genero"],
                cancion["Artista"],
                cancion["Discografia"]
            )

        # comprobamos si la cancion ya esta en la playlist
        for c in self._lista:
            if c == cancion:
                print(f"La cancion '{cancion.titulo}' ya esta en la playlist.")
                return False

        # añadimos la cancion a la lista interna
        self._lista.append(cancion)
        self._cargada = False

        # guardamos la playlist usando to_dict
        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(
                [c.to_dict() for c in self._lista],
                f,
                ensure_ascii=False,
                indent=4
            )

        print(f"Cancion '{cancion.titulo}' añadida a la playlist '{self.titulo}'.")
        return True


    # ------------------------------------------------------------


    # Metodo para mostrar info
    def mostrar_info(self):
        super().mostrar_info()

        # cargamos canciones si es necesario
        if not self._cargada:
            self.cargar_canciones()

        # mostramos el listado de canciones
        print("Lista de canciones:")
        if not self._lista:
            print("- (vacia)")
        else:
            for c in self._lista:
                print(f"- {c.titulo} — {c.artista} ({c.formatear_duracion()})")
        print()


    # ------------------------------------------------------------


    # metodo que nos permitira eliminar una playlist
    @staticmethod
    def eliminar_playlist(nombre):

        nombre = nombre.lower().strip().replace(" ", "_")
        ruta = f"archivos/playlists/{nombre}.json"

        if not os.path.exists(ruta):
            print("La playlist no existe, no se puede eliminar.")
            return

        os.remove(ruta)
        print(f"Playlist '{nombre}' eliminada correctamente.")


    # ------------------------------------------------------------


    # funcion que nos permitira seleccionar una playlist existente
    @staticmethod
    def seleccionar_playlist(ruta_relativa, ruta="archivos/playlists"):

        ruta_completa = os.path.join(ruta, ruta_relativa)
        print(f"\nCargando playlist '{ruta_relativa}'...")

        titulo = ruta_relativa.replace(".json", "").replace("_", " ").title()

        with open(ruta_completa, "r", encoding="utf-8") as f:
            contenido = f.read().strip()

            # si el archivo esta vacio, asumimos playlist vacia
            if not contenido:
                canciones = []
            else:
                canciones = json.loads(contenido)

        # obtenemos generos y artistas desde las canciones
        generos = set()
        artistas = set()

        for c in canciones:
            if not isinstance(c, dict):
                continue

            for gen in c.get("Genero", []):
                generos.add(gen)

            artista = c.get("Artista")
            if artista:
                principal, _ = Contenido.separar_artista_feat(artista)
                artistas.add(principal)

        play = ListaReproduccion(
            titulo=titulo,
            fecha_lanzamiento=date.today().year,
            duracion="0:00",
            genero=list(generos),
            artista=list(artistas)
        )

        # reconstruimos la lista interna como objetos Cancion
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

        play.ruta_archivo = ruta_completa
        play._cargada = True

        return play


    # ------------------------------------------------------------


    # funcion que permite mostrar el artista completo de la playlist
    def artista_completo(self):
        if not self.artista:
            return "varios"
        return ", ".join(self.artista)


    # ------------------------------------------------------------


    # esta funcion sirve para eliminar una cancion de la playlist
    def eliminar_cancion_playlist(self, titulo, artista):

        titulo = titulo.lower().strip()
        artista = artista.lower().strip()

        cantidad_antes = len(self._lista)

        # filtramos la lista eliminando la cancion coincidente
        self._lista = [
            c for c in self._lista
            if not (
                c.titulo.lower().strip() == titulo and
                Contenido.separar_artista_feat(c.artista)[0].lower().strip() == artista
            )
        ]

        self._cargada = False

        # guardamos los cambios en el json
        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(
                [c.to_dict() for c in self._lista],
                f,
                ensure_ascii=False,
                indent=4
            )

        if len(self._lista) == cantidad_antes:
            print(f"La cancion '{titulo.title()}' no existe en la playlist.")
        else:
            print(f"Cancion '{titulo.title()}' eliminada correctamente.")