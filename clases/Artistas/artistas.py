# Superclase Artista: Incluye cantantes individuales
from abc import ABC, abstractmethod

class Artista(ABC):
    # Clase base para representar artistas o grupos musicales.
    def __init__(self, nombre, fecha_formacion, pais_origen, activo: bool,
                 genero=None, canciones_populares=None, componentes=None):

        # Usamos los setters para validar correctamente
        self.nombre = nombre
        self.fecha_formacion = fecha_formacion
        self.pais_origen = pais_origen
        self.activo = activo

        # Listas encapsuladas y validadas
        self.genero = genero or []
        self.canciones_populares = canciones_populares or []
        self.componentes = componentes or []

    # ---------------- PROPIEDADES ----------------

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            print("El nombre debe ser texto.")
            self._nombre = "desconocido"
        else:
            self._nombre = valor

    @property
    def fecha_formacion(self):
        return self._fecha_formacion

    @fecha_formacion.setter
    def fecha_formacion(self, valor):
        if not isinstance(valor, str):
            print("La fecha de formación debe ser texto (str).")
            self._fecha_formacion = "desconocida"
        else:
            self._fecha_formacion = valor

    @property
    def pais_origen(self):
        return self._pais_origen

    @pais_origen.setter
    def pais_origen(self, valor):
        if not isinstance(valor, str):
            print("El país de origen debe ser texto.")
            self._pais_origen = "desconocido"
        else:
            self._pais_origen = valor

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, valor):
        if not isinstance(valor, bool):
            print("El atributo 'activo' debe ser booleano (True/False).")
            self._activo = False
        else:
            self._activo = valor

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        if not isinstance(valor, list):
            print("El género debe ser una lista de strings.")
            self._genero = []
        else:
            self._genero = valor

    @property
    def canciones_populares(self):
        return self._canciones_populares

    @canciones_populares.setter
    def canciones_populares(self, valor):
        if not isinstance(valor, list):
            print("Las canciones populares deben ser una lista.")
            self._canciones_populares = []
        else:
            self._canciones_populares = valor

    @property
    def componentes(self):
        return self._componentes

    @componentes.setter
    def componentes(self, valor):
        if not isinstance(valor, list):
            print("Los componentes deben ser una lista.")
            self._componentes = []
        else:
            self._componentes = valor

    # ---------------- MÉTODOS ----------------
    @abstractmethod
    def mostrar_info(self):
        print(f'Nombre: {self.nombre}')
        if self.componentes:
            print(f'Componentes: {self.componentes}')
        print(f'Género(s): {self.genero}')
        print(f'Fecha de formación: {self.fecha_formacion}')
        print(f'País de origen: {self.pais_origen}')
        if self.canciones_populares:
            print(f'Canciones populares: {self.canciones_populares}')
        print(f'Activo: {"Sí" if self.activo else "No"}')
