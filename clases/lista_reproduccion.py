#clase de lista de reproduccion.

class ListaReproduccion:
    def __init__(self,nombre, lista_canciones,duracion, genero_predominante):
        self.nombre = nombre
        self.lista_canciones = lista_canciones
        self.duracion = duracion
        self.genero_predominante = genero_predominante

    def __repr__(self):
        return(
            f'Nombre: {self.nombre}\n'
            f'Canciones: {self.lista_canciones}\n'
            f'Duracion: {self.duracion}\n'
            f'Genero predominante: {self.genero_predominante}\n'
        )
'''
#Ejemplo de ejecucion
if __name__ == '__main__':
    lista1 = ListaReproduccion('Lista1', ["Livin' on a Prayer", "It's My Life", "You Give Love a Bad Name", "Dream On", "Walk This Way", "Crazy", "Sweet Child O' Mine", "Welcome to the Jungle", "November Rain", "Paradise City"],52,'rock' )
    print(lista1)
'''