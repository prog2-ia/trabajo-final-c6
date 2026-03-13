#clase de album
#CAMBIAR NOMBRE A DISCOGRAFIA
from clases.Contenido.contenido import Contenido


class Album(Contenido):
    def __init__(self,titulo,artista,anyo_lanzamiento,duracion,genero, numero_canciones, tipo, estado_reproduccion=False):
        super().__init__(titulo, anyo_lanzamiento, duracion, genero, artista)
        self.numero_canciones = numero_canciones
        self.tipo = tipo #con tipo me refiero si es estudio/single/EP/bestof

    #la funcion que nos muestra la informacion del album.
    def mostrar_info(self):
        print('==== ALBUM ====')
        super().mostrar_info() #usamos la herencia porque simplemente tenemos que anadir informacion propia del album.
        print(f'Numero de Canciones: {self.numero_canciones}')
        print(f'Tipo de album: {self.tipo}')

#----------------------------------------

