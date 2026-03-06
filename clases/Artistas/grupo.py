from artistas import Artista


class Grupos(Artista):
    def __init__(self, nombre, fecha_formacion, pais_origen, lider, activo:bool, genero=None, canciones_populares=None, componentes=None):
        super().__init__(nombre, fecha_formacion, pais_origen, activo, genero, canciones_populares, componentes)
        self.lider=lider



    #Método para agregar un miembro
    def agregar_miembro(self, nombre):
        if nombre not in self.componentes:
            nombre.append(self.componentes)

    # Método para eliminar un miembro
    def eliminar_miembro(self, nombre):
        if nombre  in self.componentes:
            nombre.remove(self.componentes)

    #Método para contar integrantes

    def contar_componentes(self):
        return len(self.componentes)