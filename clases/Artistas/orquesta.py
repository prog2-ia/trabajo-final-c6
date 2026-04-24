from clases.Artistas.artistas import Artista

class Orquestas(Artista):
    def __init__(self, nombre:str, fecha_formacion:str, pais_origen:str, director:str,
                 activo: bool, instrumentos=None, genero=None,
                 canciones_populares=None, componentes=None):

        super().__init__(nombre, fecha_formacion, pais_origen, activo,
                         genero, canciones_populares, componentes)

        # Validación mediante setters
        self.director = director
        self.instrumentos = instrumentos or []

    # -------- PROPIEDADES --------

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, valor):
        if not isinstance(valor, str):
            print("El director debe ser texto.")
            self._director = "desconocido"
        else:
            self._director = valor

    @property
    def instrumentos(self):
        return self._instrumentos

    @instrumentos.setter
    def instrumentos(self, valor):
        if not isinstance(valor, list):
            print("Los instrumentos deben ser una lista.")
            self._instrumentos = []
        else:
            self._instrumentos = valor

    # -------- MÉTODOS --------
    # Metodo para agregar miembro
    def agregar_miembro(self, nombre):
        if nombre not in self._componentes:
            self._componentes.append(nombre)
        else:
            print(f"El miembro {nombre} ya está en la orquesta.")
    def __iadd__(self, other):
        self._componentes.append(other)

    # Metodo para eliminar miembro
    def eliminar_miembro(self, nombre):
        if nombre in self._componentes:
            self._componentes.remove(nombre)
        else:
            print(f"El miembro {nombre} no se encuentra en la orquesta.")
    def __isub__(self, other):
        if other not in self._componentes:
            print(f"{other} no se encuentra en el grupo.")
        else:
            self._componentes.remove(other)

    # Metodo para contar componentes de la orquesta
    def contar_componentes(self) -> int:
        return len(self._componentes)

    # Metodo para agregar instrumentos
    def agregar_instrumento(self, instrumento):
        if instrumento not in self._instrumentos:
            self._instrumentos.append(instrumento)
        else:
            print(f"El instrumento {instrumento} ya está registrado en la orquesta.")

    def __iaddinstrumento__(self, instrumento):
        self._instrumentos.append(instrumento)


    # Metodo para mostrar informacion
    def mostrar_info(self):
        print('INFORMACIÓN CANTANTE')
        super().mostrar_info()
        print(f'Director: {self.director}')
        print(f'Instrumentos: {self.instrumentos}')



    def __str__(self):
        return (
            f"INFORMACIÓN ORQUESTA\n"
            f"{super().__str__()}\n"
            f"Director: {self.director}\n"
            f"Instrumentos: {self.instrumentos}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}\n"            
            f"{super().__str__()}\n"
            f"Director: {self.director}\n"
            f"Instrumentos: {self.instrumentos}"
        )
