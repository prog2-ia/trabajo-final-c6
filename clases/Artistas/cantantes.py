from clases.Artistas.artistas import Artista

class Cantantes(Artista):
    def __init__(self, nombre, fecha_formacion, pais_origen,tipo_voz, activo:bool, genero=None, canciones_populares=None, componentes=None, colaboraciones=None, instrumentos=None):
        super().__init__(nombre, fecha_formacion, pais_origen, activo, genero, canciones_populares, componentes)
        self.tipo_voz = tipo_voz
        #Lista de artistas con los que ha colaborado
        self.colaboraciones = colaboraciones or []
        #Lista de instrumentos que toca
        self.instrumentos = instrumentos or []

   #Método para agregar nueva colaboración musical
    def agregar_colaboracion(self, colaboracion):
        self.colaboraciones.append(colaboracion)

    # Método para agregar nuevo instrumento
    def agregar_instrumento(self, instrumento):
        self.instrumentos.append(instrumento)
