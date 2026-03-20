# clase de album
from clases.Contenido.contenido import Contenido


#Clase Album que hereda de contenido
class Album(Contenido):
    def __init__(self, titulo, artista, anyo_lanzamiento, duracion, genero,
                 numero_canciones, tipo):

        super().__init__(titulo, anyo_lanzamiento, duracion, genero, artista)

        # VALIDAMOS USANDO LOS SETTERS
        self.numero_canciones = numero_canciones
        self.tipo = tipo

    # -------- PROPIEDADES --------
    # Comprueba que numero_cancion sea de tipo int y positivo
    @property
    def numero_canciones(self):
        return self._numero_canciones

    @numero_canciones.setter
    def numero_canciones(self, valor):
        if not isinstance(valor, int) or valor < 1:
            print("El número de canciones debe ser un entero positivo.")
            self._numero_canciones = 0     # deja un valor seguro
        else:
            self._numero_canciones = valor

    # Comprueba que tipo sea de tipo str
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        if not isinstance(valor, str):
            print("El tipo de álbum debe ser texto.")
            self._tipo = "desconocido"
        else:
            self._tipo = valor

    # -------- MÉTODOS --------

    # Metodo para mostrar informacion
    def mostrar_info(self):
        print('==== ALBUM ====')
        super().mostrar_info()
        print(f'Numero de Canciones: {self.numero_canciones}')
        print(f'Tipo de álbum: {self.tipo}')
