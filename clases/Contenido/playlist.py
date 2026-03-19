# clase de lista de reproduccion.
import json
from clases.Contenido.contenido import Contenido
from clases.Contenido.canciones import Cancion

class ListaReproduccion(Contenido):
    def __init__(self, titulo, fecha_lanzamiento, duracion, genero):
        super().__init__(titulo, fecha_lanzamiento, duracion, genero, artista="varios")
        self._lista = []
        self._cargada = False

        # Guardamos la playlist al crearla
        self.guardar_playlist()

    # ---------------------------------------------------------

    def guardar_playlist(self):
        ruta = f"archivos/playlists/{self.titulo}.json"

        # Estructura del archivo
        datos = {
            "titulo": self.titulo,
            "fecha_lanzamiento": self.fecha_lanzamiento,
            "genero": self.genero,
            "canciones": []   # inicialmente vacio
        }

        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

        print(f"Playlist '{self.titulo}' creada y guardada en {ruta}")

    # ---------------------------------------------------------
    # funcion que nos sirve para cargar canciones de un archivo json.
    def cargar_canciones(self, ruta=None):
        if ruta is None:
            ruta = f"archivos/playlists/{self.titulo}.json"

        if self._cargada:
            return self._lista

        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)["canciones"]

        for c in datos:
            cancion = Cancion(
                c["Titulo"],
                c["Fecha de lanzamiento"],
                c["Duracion"],
                c["Genero"],
                c["Artista"],
                c["Discografia"]
            )
            self._lista.append(cancion)

        self._cargada = True
        return self._lista

    # ---------------------------------------------------------

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