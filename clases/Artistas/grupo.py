from clases.Artistas.artistas import Artista


# Subclase de Artista que representa un grupo musical.
class Grupos(Artista):

    def __init__(self, nombre, fecha_formacion, pais_origen, lider,
                 activo: bool, genero=None, canciones_populares=None,
                 componentes=None):

        super().__init__(nombre, fecha_formacion, pais_origen, activo,
                         genero, canciones_populares, componentes)

        self._lider = lider

    # -------- PROPIEDADES --------

    #Verifica que el atributo lider sea del tipo str
    @property
    def lider(self):
        return self._lider

    @lider.setter
    def lider(self, valor):
        if not isinstance(valor, str):
            print("El líder debe ser texto.")
        else:
            self._lider = valor

    # -------- MÉTODOS --------

    def agregar_miembro(self, nombre):
        if nombre not in self._componentes:
            self._componentes.append(nombre)
        else:
            print(f"{nombre} ya está en el grupo.")

    def eliminar_miembro(self, nombre):
        if nombre in self._componentes:
            self._componentes.remove(nombre)
        else:
            print(f"{nombre} no se encuentra en el grupo.")

    def contar_componentes(self):
        return len(self._componentes)