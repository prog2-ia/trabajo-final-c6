import json
from contenido import Contenido

# clase de lista de reproduccion.

# Clase ListaReproducion que hereda de Contenido
class ListaReproduccion(Contenido):
    def __init__(self, titulo, fecha_lanzamiento, duracion, genero):
        super().__init__(titulo, fecha_lanzamiento, duracion, genero, artista="varios")
        self._lista = []
        self._cargada = False
        # Guardamos la playlist al crearla
        self.guardar_playlist()

    # ---------- PROPIEDADES ----------
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


    # ----------METODOS----------------
    #Metodo para guardar playlist
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
            cancion = 'Cancion'(
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