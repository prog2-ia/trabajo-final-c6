import json
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
            print("La lista debe ser una lista de canciones.")
            self._lista = []
        else:
            self._lista = valor


    # ------------------------------------------------------------


    #Metodo para guardar playlist
    @staticmethod
    def guardar_playlist(titulo,fecha_lanzamiento,duracion, genero ):
        ruta = f"archivos/playlists/{titulo.lower().strip()}.json"

        # Estructura del archivo
        datos = {
            "titulo": titulo,
            "fecha_lanzamiento": fecha_lanzamiento,
            "genero": genero,
            "canciones": []   # inicialmente vacio
        }

        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

        print(f"Playlist '{titulo}' creada y guardada en {ruta}")


    # ------------------------------------------------------------


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

    #Agregar canción a la playlist
    def __iadd__(self, cancion):
        """
        Sobrecarga del operador += para añadir una canción a la playlist.
        """
        if not isinstance(cancion, Cancion):
            print("Solo se pueden añadir objetos de tipo Cancion.")

        # Cargar canciones si aún no están cargadas
        if not self._cargada:
            self.cargar_canciones()

        # Añadir a la lista interna
        self._lista.append(cancion)

        # Guardar en el archivo JSON
        ruta = f"archivos/playlists/{self.titulo}.json"

        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)

        datos["canciones"].append({
            "Titulo": cancion.titulo,
            "Fecha de lanzamiento": cancion.fecha_lanzamiento,
            "Duracion": cancion.duracion,
            "Genero": cancion.genero,
            "Artista": cancion.artista,
            "Discografia": cancion.discografia
        })

        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

        print(f"Canción '{cancion.titulo}' añadida a la playlist '{self.titulo}'.")

        return self

    # ------------------------------------------------------------


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