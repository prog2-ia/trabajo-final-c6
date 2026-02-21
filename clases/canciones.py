#Librería para formatear la fecha
from datetime import datetime

#Clase Canción
class Cancion:
    def __init__(self, titulo, artista, album, genero,duracion, fecha_lanzamiento, num_escuchas, discografica):
        #Argumentos de instancia
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = int(duracion) #Tipo entero
        self.num_escuchas = int(num_escuchas) #Tipo entero
        self.discografica = discografica


        # Lista de géneros en caso de que pertenezca a más de uno
        if genero is None:
            self.genero = []
        elif isinstance(genero, list):
            self.genero = genero
        else:
            self.genero = [genero]

        # Comprueba si es un string y cambia el formato
        if isinstance(fecha_lanzamiento, str):
            self.fecha_lanzamiento = datetime.strptime(fecha_lanzamiento, "%Y-%m-%d")
        else:
            self.fecha_lanzamiento = fecha_lanzamiento

    def __str__(self):
        return (f"{self.titulo} - {self.artista}\n"
                f"Álbum: {self.album}\n"
                f"Género(s): {', '.join(self.genero)}\n"
                f"Duración: {self.duracion} seg\n"
                f"Escuchas: {self.num_escuchas}\n"
                f"Discográfica: {self.discografica}\n"
                f"Fecha lanzamiento: {self.fecha_lanzamiento.strftime('%Y-%m-%d')}")

    def __repr__(self):
        return (f"{type(self).__name__}("
                f"titulo='{self.titulo}', "
                f"artista='{self.artista}', "
                f"album='{self.album}', "
                f"genero={self.genero}, "
                f"duracion={self.duracion}, "
                f"fecha_lanzamiento='{self.fecha_lanzamiento.strftime('%Y-%m-%d')}', "
                f"num_escuchas={self.num_escuchas}, "
                f"discografica='{self.discografica}')")