#importamos clases que heredan del Contenido:
from clases.Contenido.canciones import Cancion
from clases.Contenido.album import Album
from clases.Contenido.lista_reproduccion import ListaReproduccion

#importamos clases que heredan del Artista:
from clases.Artistas.cantantes import Cantantes
from clases.Artistas.grupo import Grupos
from clases.Artistas.orquesta import Orquestas


if __name__ == '__main__':
    cancion1 = Cancion("Livin' on a Prayer",1986,'4:11',['Glam metal','Hard rock'],'Bon Jovi', 'Slippery When Wet')
    cancion1.mostrar_info()

    print()
    print()

    lista1 = ListaReproduccion('Mi lista',2025,'47:0',['Rock','Glam rock'],["Livin' on a Prayer","Back in Black","Sweet Child O' Mine","Smells Like Teen Spirit","Highway to Hell","Enter Sandman","Don't Stop Believin'","Bohemian Rhapsody","Paranoid","Whole Lotta Love"])
    lista1.mostrar_info()

    print()
    print()

    album1 = Album('Slippery When Wet','Bon Jovi',1986, 44, ['Glam metal','Hard Rock'], 10, 'Estudio')
    album1.mostrar_info()
