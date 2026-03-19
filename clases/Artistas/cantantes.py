from clases.Artistas.artistas import Artista

class Cantantes(Artista):
    def __init__(self, nombre, fecha_formacion, pais_origen, tipo_voz,
                 activo: bool, genero=None, canciones_populares=None,
                 componentes=None, colaboraciones=None, instrumentos=None):

        super().__init__(nombre, fecha_formacion, pais_origen, activo,
                         genero, canciones_populares, componentes)

        # Usar setters para validación
        self.tipo_voz = tipo_voz
        self.colaboraciones = colaboraciones or []
        self.instrumentos = instrumentos or []

    # -------- PROPIEDADES --------

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

    def agregar_colaboracion(self, colaboracion):
        self._colaboraciones.append(colaboracion)

    def agregar_instrumento(self, instrumento):
        self._instrumentos.append(instrumento)