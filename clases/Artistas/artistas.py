# Superclase Artista: Incluye cantantes individuales
from abc import ABC, abstractmethod

#Errores relacionados con la clase Artista.
class ArtistaError(Exception):
    pass

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

    # Comprueba que el nombre sea un string antes de asignarlo
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            raise ArtistaError("El nombre debe ser texto.")
        self._nombre = "desconocido"


    # Comprueba que la fecha_formacion sea un string antes de asignarlo
    @property
    def fecha_formacion(self):
        return self._fecha_formacion

    @fecha_formacion.setter
    def fecha_formacion(self, valor):
        if not isinstance(valor, str):
            raise ArtistaError("La fecha de formación debe ser texto (str).")
        self._fecha_formacion = "desconocida"

    # Comprueba que el pais_origen sea un string antes de asignarlo
    @property
    def pais_origen(self):
        return self._pais_origen

    @pais_origen.setter
    def pais_origen(self, valor):
        if not isinstance(valor, str):
            raise ArtistaError("El país de origen debe ser texto.")
        self._pais_origen = "desconocido"

    # Comprueba que activo sea un valor booleano antes de asignarlo
    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, valor):
        if not isinstance(valor, bool):
            raise ArtistaError("El atributo 'activo' debe ser booleano (True/False).")
        self._activo = valor

    # Comprueba que el genero sea una lista antes de asignarlo
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        if not isinstance(valor, list):
            raise ArtistaError("El género debe ser una lista de strings.")
        self._genero = valor

    # Comprueba que canciones_populares sea una lista antes de asignarlo
    @property
    def canciones_populares(self):
        return self._canciones_populares

    @canciones_populares.setter
    def canciones_populares(self, valor):
        if not isinstance(valor, list):
            raise ArtistaError("Las canciones populares deben ser una lista.")
        self._canciones_populares = valor

    # Comprueba que componentes sea una lista antes de asignarlo
    @property
    def componentes(self):
        return self._componentes

    @componentes.setter
    def componentes(self, valor):
        if not isinstance(valor, list):
            raise ArtistaError("Los componentes deben ser una lista.")
        self._componentes = valor

    # ---------------- MÉTODOS ----------------

    #Metodo abstracto para mostrar la información en las subclases
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
