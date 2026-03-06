# clase alternativa para canciones (usando herencia)

from clases.Contenido.contenido import Contenido


class Cancion(Contenido):
    def __init__(self,titulo, fecha_lanzamiento, duracion,genero,artista, discografia):
        super().__init__(titulo,fecha_lanzamiento,duracion,genero,artista,estado_reproduccion=False)
        self.discografia = discografia

    def mostrar_info(self):
        print('==== CANCION ====')
        super().mostrar_info()
        print(f'Discografia: {self.discografia}')

#-----------------------------------------

