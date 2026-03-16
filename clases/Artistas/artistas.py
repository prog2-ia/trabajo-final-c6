#Superclase Artista: Incluye cantantes individuales

#Añadir formato para la fecha de formacion??
class Artista:
    #Clase base para representar artistas o grupos musicales.


    def __init__(self, nombre, fecha_formacion, pais_origen, activo: bool, genero=None, canciones_populares=None, componentes=None):

        # Usamos los setters para validar automáticamente
        self._nombre = nombre
        self._fecha_formacion = fecha_formacion
        self._pais_origen = pais_origen
        self._activo = activo

        # Listas encapsuladas
        self.genero = genero or []
        self.canciones_populares = canciones_populares or []
        self.componentes = componentes or []

    # ---------------- PROPIEDADES ----------------

    #Propiedad para validar que el nombre sea tipo str
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            print("El nombre debe ser texto.")
        else:
            self._nombre = valor

    # Propiedad para validar que la fecha de formacion sea del tipo str
    @property
    def fecha_formacion(self):
        return self._fecha_formacion

    @fecha_formacion.setter
    def fecha_formacion(self, valor):
        if not isinstance(valor, str):
            print("La fecha de formación debe ser texto (str).")
        else:
            self._fecha_formacion = valor


    # Propiedad para validar que el pais sea del tipo str
    @property
    def pais_origen(self):
        return self._pais_origen

    @pais_origen.setter
    def pais_origen(self, valor):
        if not isinstance(valor, str):
            print("El país de origen debe ser texto.")
        else:
            self._pais_origen = valor

    # Propiedad para validar que el atributo activo sea del tipo bool
    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, valor):
        if not isinstance(valor, bool):
            print("El atributo 'activo' debe ser booleano (True/False).")
        else:
            self._activo = valor


    # Propiedad para validar que el atributo genero sea una lista de str
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        if not isinstance(valor, list):
            print("El género debe ser una lista de strings.")
        else:
            self._genero = valor


    # Propiedad para validar que el atributo canciones_populares sea una lista
    def canciones_populares(self):
        return self._canciones_populares

    @canciones_populares.setter
    def canciones_populares(self, valor):
        if not isinstance(valor, list):
            print("Las canciones populares deben ser una lista.")
        else:
            self._canciones_populares = valor


    # Propiedad para validar que el atributo componentes sea una lista
    @property
    def componentes(self):
        return self._componentes

    @componentes.setter
    def componentes(self, valor):
        if not isinstance(valor, list):
            print("Los componentes deben ser una lista.")
        else:
            self._componentes = valor

    # ---------------- MÉTODOS ----------------

    def mostrar_info(self):
        print(f'Nombre: {self._nombre}')
        if self._componentes:
            print(f'Componentes: {self._componentes}')
        print(f'Género(s): {self._genero}')
        print(f'Fecha de formación: {self._fecha_formacion}')
        print(f'País de origen: {self._pais_origen}')
        if self._canciones_populares:
            print(f'Canciones populares: {self._canciones_populares}')
        print(f'Activo: {"Sí" if self._activo else "No"}')