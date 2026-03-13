

class Genero:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return (f"Género: {self.nombre}\n"
                f"Descripción: {self.descripcion}")

    def __repr__(self):
        return (f"{type(self).__name__}("
                f"nombre='{self.nombre}', "
                f"descripcion='{self.descripcion}')")

    '''
    Método para indicar la popularidad de un género: Importarte para crear Playlist de géneros concretos con canciones populares.
    '''
    def es_popular(self):
        populares = ["Pop", "Rock", "Reggaetón", "Hip Hop", "Electrónica"]
        return self.nombre in populares

    #Cambia el nombre y descripción del género.
    def actualizar_genero(self, nuevo_nombre, nueva_descripcion):
        self.nombre = nuevo_nombre
        self.descripcion = nueva_descripcion

