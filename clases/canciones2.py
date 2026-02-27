# clase alternativa para canciones (usando herencia)

from contenido import Contenido

class Cancion(Contenido):
    def __init__(self,titulo, fecha_lanzamiento, duracion,genero,artista, discografia):
        super().__init__(titulo,fecha_lanzamiento,duracion,genero,artista,estado_reproduccion=False)
        self.discografia = discografia

    def mostrar_info(self):
        print('==== CANCION ====')
        super().mostrar_info()
        print(f'Discografia: {self.discografia}')

#-----------------------------------------
if __name__ == '__main__':
    cancion1 = Cancion("Livin' on a Prayer",1986,4,['Glam metal','Hard rock'],'Bon Jovi', 'Slippery When Wet')
    cancion1.mostrar_info()

    #intentamos reproducir la cancion
    cancion1.reproducir()
    print()
    #volvemos a ver si se esta reproduciendo
    cancion1.mostrar_info()