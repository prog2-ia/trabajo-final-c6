from clases.Artistas.artistas import Artista, ArtistaError

#Importamos ArtistaError

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
            raise ArtistaError("El líder debe ser texto.")
        self._lider = "desconocido"   # Valor seguro


    # -------- MÉTODOS --------

    #Agregar miembros
    def agregar_miembro(self, nombre):
        if not isinstance(nombre, str):
            raise ArtistaError("El nombre del miembro debe ser un string.")

        if nombre in self._componentes:
            raise ArtistaError(f"{nombre} ya está en el grupo.")

        self._componentes.append(nombre)


    #Eliminar miembro
    def eliminar_miembro(self, nombre):
        if not isinstance(nombre, str):
            raise ArtistaError("El nombre del miembro debe ser un string.")

        if nombre not in self._componentes:
            raise ArtistaError(f"{nombre} no se encuentra en el grupo.")

        self._componentes.remove(nombre)

    #Contar componentes del grupo
    def __len__(self) -> int:
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

