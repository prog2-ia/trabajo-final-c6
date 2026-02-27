class Contenido:
    def __init__(self,titulo, fecha_lanzamiento, duracion,genero,artista, estado_reproduccion=False):
        self.titulo = titulo
        self.artista = artista
        self.fecha_lanzamiento = fecha_lanzamiento
        self.duracion = duracion
        self.genero = genero
        self.estado_reproduccion = estado_reproduccion

    # el metodo que nos sirve para mostrar toda la inforamcion del contendido (sea cancion, playlist, ...) la usaremos luego en la herencia.
    def mostrar_info(self):
        print(f'Titulo: {self.titulo}')
        print(f'Artista: {self.artista}')
        print(f'Fecha de lanzamiento: {self.fecha_lanzamiento}')
        print(f'Duracion: {self.duracion}')
        print(f'Genero: {self.genero}')
        print(f'Estado de reproduccion: {'reproduciendo' if self.estado_reproduccion == True else 'pausado'}')

    #metodos:
    # reproducir el contenido
    def reproducir(self):
        self.estado_reproduccion = True

    # pausar el contenido
    def pausar(self):
        self.estado_reproduccion = False


