#clase de lista de reproduccion.
from clases.Contenido.contenido import Contenido

class ListaReproduccion(Contenido):
    def __init__(self,titulo, fecha_lanzamiento, duracion, genero, lista_canciones,estado_reproduccion=False):
        super().__init__(titulo,fecha_lanzamiento,duracion,genero, artista='varios')
        self.lista_canciones = lista_canciones

    def mostrar_info(self):
        print(f'==== LISTA DE REPRODUCCION ====')
        super().mostrar_info()
        print(f'Lista de canciones:')
        for cancion in self.lista_canciones:
            print(f'-  {cancion}')


#-------------------------------------------
