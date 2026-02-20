#Librería para formatear la fecha
from datetime import datetime

#Clase Canción
class Cancion:
    def __init__(self, titulo, artista, album, genero,duracion, fecha_lanzamiento, num_escuchas, discografica):
        #Argumentos de instancia

        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = list(genero) #Lista de géneros en caso de que pertenezca a más de uno
        self.duracion = int(duracion) #Tipo entero

        if isinstance(fecha_lanzamiento, str): #Comprueba si es un string y cambia el formato
            self.fecha_lanzamiento = datetime.strptime(fecha_lanzamiento, "%Y-%m-%d")
        else:
            self.fecha_lanzamiento = fecha_lanzamiento

        self.num_escuchas = int(num_escuchas) #Tipo entero

        self.discografica = discografica
