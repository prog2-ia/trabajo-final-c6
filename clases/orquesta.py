from artistas import Artista


class Orquestas(Artista):
    def __init__(self, nombre, fecha_formacion, pais_origen, director, activo:bool, instrumentos=None, genero=None, canciones_populares=None, componentes=None):
        super().__init__(nombre, fecha_formacion, pais_origen, activo, genero, canciones_populares, componentes)
        self.director=director
        # Lista de instrumentos
        self.instrumentos = instrumentos or []

        # Método para agregar un miembro
    def agregar_miembro(self, nombre):
        if nombre not in self.componentes:
            nombre.append(self.componentes)
        else:
            print(f"El miembro {nombre} ya está en la orquesta.")

        # Método para eliminar un miembro
    def eliminar_miembro(self, nombre):
        if nombre in self.componentes:
            nombre.remove(self.componentes)
        else:
            print(f"El miembro {nombre} no se encuentra en la orquesta.")

        # Método para contar integrantes
    def contar_componentes(self):
        return len(self.componentes)

        # Método para agregar nuevo instrumento
    def agregar_instrumento(self, instrumento):
        if instrumento not in self.instrumentos:
            self.instrumentos.append(instrumento)
        else:
            print(f"El instrumento {instrumento} ya está registrado en la orquesta.")
