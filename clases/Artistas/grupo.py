from clases.Artistas.artistas import Artista

# Subclase de Artista que representa un grupo musical.
class Grupos(Artista):

    def __init__(self, nombre:str, fecha_formacion:str, pais_origen:str, lider:str,
                 activo: bool, genero=None, canciones_populares=None,
                 componentes=None):

        super().__init__(nombre, fecha_formacion, pais_origen, activo,
                         genero, canciones_populares, componentes)

        # Usamos el setter para validar
        self.lider = lider

    # -------- PROPIEDADES --------

    # Comprueba que lider sea un str antes de asignarlo
    @property
    def lider(self):
        return self._lider

    @lider.setter
    def lider(self, valor):
        if not isinstance(valor, str):
            print("El líder debe ser texto.")
            self._lider = "desconocido"   # Valor seguro
        else:
            self._lider = valor

    # -------- MÉTODOS --------

    #Agregar miembros
    def agregar_miembro(self, nombre):
        if nombre not in self._componentes:
            self._componentes.append(nombre)
        else:
            print(f"{nombre} ya está en el grupo.")

    def __iadd__(self, other):
        self._componentes.append(other)

    #Eliminar miembro
    def eliminar_miembro(self, nombre):
        if nombre in self._componentes:
            self._componentes.remove(nombre)
        else:
            print(f"{nombre} no se encuentra en el grupo.")
    def __isub__(self, other):
        if other not in self._componentes:
            print(f"{other} no se encuentra en el grupo.")
        else:
            self._componentes.remove(other)

    def contar_componentes(self) -> int:
        return len(self._componentes)

    def mostrar_info(self):
        print('INFORMACIÓN GRUPO')
        super().mostrar_info()
        print(f'Lider: {self.lider}')

    def __str__(self):
         return (
            f"INFORMACIÓN GRUPO\n"
            f"{super().__str__()}\n"
            f"Lider: {self.lider}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}\n"            
            f"{super().__str__()}\n"
            f"Lider: {self.lider}"

        )

