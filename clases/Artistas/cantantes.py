from clases.Artistas.artistas import Artista

#Clase Cantantes que hereda de Artistas
class Cantantes(Artista):
    def __init__(self, nombre:str, fecha_formacion:str, pais_origen:str, tipo_voz:str,
                 activo: bool, genero=None, canciones_populares=None,
                 componentes=None, colaboraciones=None, instrumentos=None):

        super().__init__(nombre, fecha_formacion, pais_origen, activo,
                         genero, canciones_populares, componentes)

        # Usar setters para validación
        self.tipo_voz = tipo_voz
        self.colaboraciones = colaboraciones or []
        self.instrumentos = instrumentos or []

    # -------- PROPIEDADES --------

    # Comprueba que el tipo_voz sea un string antes de asignarlo
    @property
    def tipo_voz(self):
        return self._tipo_voz

    @tipo_voz.setter
    def tipo_voz(self, valor):
        if not isinstance(valor, str):
            print("El tipo de voz debe ser texto.")
            self._tipo_voz = "desconocido"
        else:
            self._tipo_voz = valor

    # Comprueba que colaboraciones sea una lista antes de asignarlo
    @property
    def colaboraciones(self):
        return self._colaboraciones

    @colaboraciones.setter
    def colaboraciones(self, valor):
        if not isinstance(valor, list):
            print("Las colaboraciones deben ser una lista.")
            self._colaboraciones = []
        else:
            self._colaboraciones = valor

    # Comprueba que instrumentos sea una lista antes de asignarlo
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

    # Metodo para agregar colaboraciones
    def agregar_colaboracion(self, colaboracion):
        self._colaboraciones.append(colaboracion)

    def __iaddcolaboracion(self, colaboracion):
        self.colaboraciones.append(colaboracion)


    # Metodo para agregar instrumentos
    def agregar_instrumento(self, instrumento):
        self._instrumentos.append(instrumento)

    def __iaddinstrumento(self, instrumento):
        self.instrumentos.append(instrumento)

    # Metodo para mostrar informacion
    def mostrar_info(self):
        print('INFORMACIÓN CANTANTE')
        super().mostrar_info()
        print(f'Tipo de voz: {self.tipo_voz}')
        print(f'Colaboraciones: {self.colaboraciones}')
        print(f'Instrumentos: {self.instrumentos}')


    def __str__(self):
        return (
            f"INFORMACIÓN CANTANTE\n"
            f"{super().__str__()}\n"
            f"Tipo de voz: {self.tipo_voz}\n"
            f"Colaboraciones: {self.colaboraciones}\n"
            f"Instrumentos: {self.instrumentos}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}\n"            
            f"{super().__str__()}\n"
            f"Tipo de voz: {self.tipo_voz}\n"
            f"Colaboraciones: {self.colaboraciones}\n"
            f"Instrumentos: {self.instrumentos}"
        )


