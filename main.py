#importamos clases que heredan del Contenido:
from clases.Contenido.canciones import Cancion
from clases.Contenido.album import Album
from clases.Contenido.lista_reproduccion import ListaReproduccion

#importamos clases que heredan del Artista:
from clases.Artistas.cantantes import Cantantes
from clases.Artistas.grupo import Grupos
from clases.Artistas.orquesta import Orquestas


if __name__ == '__main__':
    playlist1 = ListaReproduccion('Playlist1', '2026', '40:00', ['Rock','Metal'])
    playlist1.mostrar_info()
