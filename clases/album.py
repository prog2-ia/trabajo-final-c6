#clase de album

class Album:
    def __init__(self, titulo, artista, numero_canciones, anyo_lanzamiento):
        self.titulo = titulo
        self.artista = artista
        self.numero_canciones = numero_canciones
        self.anyo_lanzamiento = anyo_lanzamiento

    def __repr__(self):
        return(
            f'Titulo: {self.titulo}\n'
            f'Artista: {self.artista}\n'
            f'Numero de canciones: {self.numero_canciones}\n'
            f'Anyo de lanzamiento: {self.anyo_lanzamiento}\n'
        )

'''
#ejemplo de ejecucion:
if __name__ == '__main__':
    album1 = Album('Slippery When Wet','Bon Jovi',10,1986)
    print(album1)
'''