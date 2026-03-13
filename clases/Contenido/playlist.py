#clase de lista de reproduccion.
import json
from clases.Contenido.contenido import Contenido
from clases.Contenido.canciones import Cancion

#clase de listas de reproduccion (playlist)
class ListaReproduccion(Contenido):
    def __init__(self,titulo, fecha_lanzamiento, duracion, genero,):
        super().__init__(titulo,fecha_lanzamiento,duracion,genero, artista='varios')
        self.lista = []
        self._cargada = False #para asegurarnos de que la lista se ha cargado correctamente.

    # ---------------------------------------------------------

    #cargamos canciones desde json (donde guardamos nuestra playlist)
    def cargar_canciones(self, ruta='archivos/playlists/playlist1.json'):
        if self._cargada:
            return self.lista
        #abrimos json
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)["canciones"]
        #recorremos archivo json y recogemos datos, y guardamos en una lista.
        for c in datos:
            cancion = Cancion(
                c["Titulo"],
                c["Fecha de lanzamiento"],
                c["Duracion"],
                c["Genero"],
                c["Artista"],
                c["Discografia"]
            )
            self.lista.append(cancion)
        self._cargada = True
        #devolvemos la lista.
        return self.lista

    # ---------------------------------------------------------

    def mostrar_info(self):
        print('==== PLAYLIST ====')
        super().mostrar_info()

        if not self._cargada:
            self.cargar_canciones()

        print('Lista de canciones:')
        if not self.lista:
            print('- (vacía)')
        else:
            for cancion in self.lista:
                print(f'- {cancion.titulo} — {cancion.artista} ({cancion.formatear_duracion()})')

    #---------------------------------------------------------

