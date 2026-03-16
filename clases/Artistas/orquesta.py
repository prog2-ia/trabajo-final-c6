from clases.Artistas.artistas import Artista

class Orquestas(Artista):
    def __init__(self, nombre, fecha_formacion, pais_origen, director, activo:bool, instrumentos=None, genero=None, canciones_populares=None, componentes=None):
        super().__init__(nombre, fecha_formacion, pais_origen, activo, genero, canciones_populares, componentes)
        self._director = director
        self.__instrumentos = instrumentos or []

    # -------- PROPIEDADES --------

    #Verificar que el atributo director sea de tipo str
    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, valor):
        if not isinstance(valor, str):
            print("El director debe ser texto.")
        else:
            self._director = valor

    #Verificar que el atributo instrumentos sea de tipo list
    @property
    def instrumentos(self):
        return self._instrumentos

    @instrumentos.setter
    def instrumentos(self, valor):
        if not isinstance(valor, list):
            print("Los instrumentos deben ser una lista.")
        else:
            self._instrumentos = valor

    # Agregar un miembro
    def agregar_miembro(self, nombre):
        if nombre not in self.componentes:
            self._componentes.append(nombre)
        else:
            print(f"El miembro {nombre} ya está en la orquesta.")

        # Eliminar un miembro
    def eliminar_miembro(self, nombre):
        if nombre in self.componentes:
            self._componentes.remove(nombre)
        else:
            print(f"El miembro {nombre} no se encuentra en la orquesta.")

        # Contar integrantes
    def contar_componentes(self):
        return len(self.componentes)

        # Agregar nuevo instrumento
    def agregar_instrumento(self, instrumento):
        if instrumento not in self._instrumentos:
            self._instrumentos.append(instrumento)
        else:
            print(f"El instrumento {instrumento} ya está registrado en la orquesta.")
