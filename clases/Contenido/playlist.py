import json
import os
from clases.Contenido.contenido import Contenido
from clases.Contenido.canciones import Cancion

# clase de lista de reproduccion.

# Clase ListaReproducion que hereda de Contenido
class ListaReproduccion(Contenido):
    def __init__(self, titulo, fecha_lanzamiento, duracion, genero):
        super().__init__(titulo, fecha_lanzamiento, duracion, genero, artista="varios")
        self._lista = []
        self._cargada = False
        # Guardamos la playlist al crearla
        self.guardar_playlist()


    # ------------------------------------------------------------


    #Comprobar que lista sea del tipo lista
    @property
    def lista(self):
        return self._lista

    @lista.setter
    def lista(self, valor):
        if not isinstance(valor, list):
            raise TypeError("La lista debe ser una lista de canciones.")
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

        playlist = {
            "titulo": self.titulo,
            "fecha_lanzamiento": self.fecha_lanzamiento,
            "duracion": '0:00',
            "genero": [],
            "artista": [],
            "canciones": {}
        }

        #Probamos a abrir el archivo JSON
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(playlist, f, ensure_ascii=False, indent=4)

        #Error del sistema operativo (OSError): Ocurre cuando no se puedo realizar la operación solicitada
        except OSError:
            raise OSError(f"No se pudo crear la playlist en {ruta}")
        finally:
            print(f"Playlist '{self.titulo}' creada en {ruta}")


    # ------------------------------------------------------------

    # Metodo estático para seleccionar una playlist
    @staticmethod
    def seleccionar_playlist(nombre_archivo, ruta="archivos/playlists"):
        ruta_completa = os.path.join(ruta, nombre_archivo)

        try:
            with open(ruta_completa, "r", encoding="utf-8") as f:
                datos = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró la playlist: {ruta_completa}")
        except json.JSONDecodeError:
            raise ValueError("El archivo JSON de la playlist está corrupto o mal formado.")

        playlist = ListaReproduccion(
            titulo=datos["titulo"],
            fecha_lanzamiento=datos["fecha_lanzamiento"],
            duracion=datos["duracion"],
            genero=datos["genero"]
        )

        playlist._lista = []  # lista vacía
        playlist._cargada = False
        playlist.ruta_archivo = ruta_completa

        return playlist


    # funcion que nos sirve para cargar canciones de un archivo json.
    def cargar_canciones(self, ruta=None):
        if ruta is None:
            ruta = f"archivos/playlists/{self.titulo}.json"

        if self._cargada:
            return self._lista


        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)

            canciones = datos.get("canciones", [])
            if not isinstance(canciones, list):
                raise ValueError("El campo 'canciones' debe ser una lista.")

            for c in canciones:
                try:
                    cancion = Cancion(
                        c["Titulo"],
                        c["Fecha de lanzamiento"],
                        c["Duracion"],
                        c["Genero"],
                        c["Artista"],
                        c["Discografia"]
                    )
                except KeyError as e:
                    raise KeyError(f"Falta la clave {e} en una canción del JSON.")

                self._lista.append(cancion)

        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

        except json.JSONDecodeError:
            raise ValueError("El archivo JSON está corrupto o mal formado.")

        self._cargada = True
        return self._lista

    #Metodo para eliminar canciones de la playlist
    def eliminar_cancion_playlist(self, titulo, artista):
        titulo = titulo.lower().strip()
        artista = artista.lower().strip()

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("No se encontró el archivo de la playlist.")
        except json.JSONDecodeError:
            raise ValueError("El archivo JSON de la playlist está corrupto.")

        canciones = datos.get("canciones", [])
        nuevas = []
        encontrada = False

        for c in canciones:
            titulo_c = c["Titulo"].lower().strip()
            artista_principal, _ = Contenido.separar_artista_feat(c["Artista"])

            if titulo_c == titulo and artista_principal.lower().strip() == artista:
                encontrada = True
            else:
                nuevas.append(c)

        if not encontrada:
            raise ValueError(f"La canción '{titulo.title()}' de {artista.title()} no está en la playlist.")

        datos["canciones"] = nuevas

        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

        print(f"Canción '{titulo.title()}' eliminada correctamente de la playlist '{self.titulo.title()}'.")


    # ------------------------------------------------------------

    #Metodo estático para eliminar playlist
    @staticmethod
    def eliminar_playlist(nombre, ruta="archivos/playlists"):
        nombre_archivo = nombre.lower().replace(" ", "_") + ".json"
        ruta_completa = os.path.join(ruta, nombre_archivo)

        try:
            os.remove(ruta_completa)
        except FileNotFoundError:
            raise FileNotFoundError(f"La playlist '{nombre}' no existe.")

        #Error operativo del sistema
        except OSError:
            raise OSError("No se pudo eliminar la playlist.")

        print(f"Playlist '{nombre.title()}' eliminada correctamente.")


    #Metodo para mostrar info
    def mostrar_info(self):
        print("==== PLAYLIST ====")
        super().mostrar_info()

        if not self._cargada:
            self.cargar_canciones()

        print("Lista de canciones:")
        if not self._lista:
            print("- (vacía)")
        else:
            for cancion in self._lista:
                print(f"- {cancion.titulo} — {cancion.artista} ({cancion.formatear_duracion()})")