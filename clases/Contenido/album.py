#clase de album
from clases.Contenido.contenido import Contenido

class Album(Contenido):
    def __init__(self,titulo,artista,anyo_lanzamiento,duracion,genero, numero_canciones, tipo, estado_reproduccion=False):
        super().__init__(titulo, anyo_lanzamiento, duracion, genero, artista)
        self._numero_canciones = numero_canciones
        self._tipo = tipo #con tipo me refiero si es estudio/single/EP/bestof

    # -------- PROPIEDADES --------

    #Valida que el valor de numero_canciones sea int y mayor que 1
    @property
    def numero_canciones(self):
        return self._numero_canciones

    @numero_canciones.setter
    def numero_canciones(self, valor):
        if not isinstance(valor, int) or valor < 1:
            print("El número de canciones debe ser un entero positivo.")
        else:
            self._numero_canciones = valor

    # Valida que el tipo de álbum sea str
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        if not isinstance(valor, str):
           print("El tipo de álbum debe ser texto.")
        else:
            self._tipo = valor

    # -------- MÉTODOS --------

    #la funcion que nos muestra la informacion del album.
    def mostrar_info(self):
        print('==== ALBUM ====')
        super().mostrar_info() #usamos la herencia porque simplemente tenemos que anadir informacion propia del album.
        print(f'Numero de Canciones: {self._numero_canciones}')
        print(f'Tipo de album: {self._tipo}')

#----------------------------------------

