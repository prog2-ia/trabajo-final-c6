# Superclase Artista
from abc import ABC, abstractmethod
import json


# Errores relacionados con la clase Artista.
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

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            raise ArtistaError("El nombre debe ser texto.")
        self._nombre = valor

    @property
    def fecha_formacion(self):
        return self._fecha_formacion

    @fecha_formacion.setter
    def fecha_formacion(self, valor):
        if not isinstance(valor, str):
            raise ArtistaError("La fecha de formación debe ser texto (str).")
        self._fecha_formacion = valor

    @property
    def pais_origen(self):
        return self._pais_origen

    @pais_origen.setter
    def pais_origen(self, valor):
        if not isinstance(valor, str):
            raise ArtistaError("El país de origen debe ser texto.")
        self._pais_origen = valor

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, valor):
        if not isinstance(valor, bool):
            raise ArtistaError("El atributo 'activo' debe ser booleano (True/False).")
        self._activo = valor

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        if not isinstance(valor, list):
            raise ArtistaError("El género debe ser una lista.")
        self._genero = valor

    @property
    def canciones_populares(self):
        return self._canciones_populares

    @canciones_populares.setter
    def canciones_populares(self, valor):
        if not isinstance(valor, list):
            raise ArtistaError("Las canciones populares deben ser una lista.")
        self._canciones_populares = valor

    @property
    def componentes(self):
        return self._componentes

    @componentes.setter
    def componentes(self, valor):
        if not isinstance(valor, list):
            raise ArtistaError("Los componentes deben ser una lista.")
        self._componentes = valor

    # ---------------- MÉTODOS ----------------

    #Metodo para guardar artista
    @staticmethod
    def guardar_artista(artista, ruta='archivos/artistas_guardados.json'):
        if not isinstance(artista, Artista):
            raise TypeError("Solo se pueden guardar objetos Artista.")

        # Guardamos el nombre antes de cualquier operación para usarlo en finally.
        nombre_artista = artista.nombre

        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)

        except FileNotFoundError:
            # Si el archivo no existe aún, empezamos con lista vacía.
            datos = []

        #Error encaso de error al formar el archivo json
        except json.JSONDecodeError:
            raise ArtistaError("El archivo JSON está corrupto o mal formado.")

        # Comprobamos que el artista no esté ya registrado.
        for a in datos:
            if a.get("Nombre", "").lower() == artista.nombre.lower():
                print(f"El artista '{artista.nombre}' ya existe en la base de datos.")
                return

        # Añadimos el nuevo artista.
        datos.append({
            "Nombre": artista.nombre,
            "Fecha de formación": artista.fecha_formacion,
            "País de origen": artista.pais_origen,
            "Activo": artista.activo,
            "Género": artista.genero,
            "Canciones populares": artista.canciones_populares,
            "Componentes": artista.componentes
        })

        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

        # BUG CORREGIDO: usamos 'nombre_artista' (str guardado antes),
        # no 'artista.nombre' que ya no es el objeto sino la lista.
        print(f"Artista '{nombre_artista}' guardado correctamente.")


    # Metodo para eliminar artista de la base de datos.
    @staticmethod
    def eliminar_artista(artista, ruta='archivos/artistas_guardados.json'):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)

        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

        except json.JSONDecodeError:
            raise ArtistaError("El archivo JSON está corrupto o mal formado.")

        encontrado = False
        for a in datos:
            if a.get("Nombre", "").lower() == artista.lower():
                datos.remove(a)
                encontrado = True
                break

        if not encontrado:
            raise ValueError(f"No se encontró el artista '{artista}'.")

        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

        print(f"Artista '{artista}' eliminado correctamente.")


    # Metodo para buscar artista en la base de datos.
    @staticmethod
    def buscar_artista(nombre, ruta='archivos/artistas_guardados.json'):
        try:
            with open(ruta, "r", encoding="utf-8") as f:

                datos = json.load(f)

        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

        except json.JSONDecodeError:
            raise ArtistaError("El archivo JSON está corrupto o mal formado.")

        encontrado = False
        for a in datos:
            if a.get("Nombre", "").lower() == nombre.lower():
                encontrado = True

                print(f"Nombre:              {a.get('Nombre')}")
                print(f"Fecha de formación:  {a.get('Fecha de formación')}")
                print(f"País de origen:      {a.get('País de origen')}")
                print(f"Activo:              {'Sí' if a.get('Activo') else 'No'}")
                print(f"Género:              {a.get('Género', [])}")
                print(f"Canciones populares: {a.get('Canciones populares', [])}")
                print(f"Componentes:         {a.get('Componentes', [])}")

                return a

        if not encontrado:
            raise ValueError(f"No se encontró el artista '{nombre}'.")
        return None


    # Metodo abstracto para mostrar la información en las subclases.
    @abstractmethod
    def mostrar_info(self):
        print(f"Nombre:              {self.nombre}")
        if self.componentes:
            print(f"Componentes:         {self.componentes}")
        print(f"Género(s):           {self.genero}")
        print(f"Fecha de formación:  {self.fecha_formacion}")
        print(f"País de origen:      {self.pais_origen}")
        if self.canciones_populares:
            print(f"Canciones populares: {self.canciones_populares}")
        print(f"Activo:              {'Sí' if self.activo else 'No'}")


    @staticmethod
    def mostrar_artistas(ruta='archivos/artistas_guardados.json'):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                artistas = json.load(f)

        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

        except json.JSONDecodeError:
            raise ArtistaError("El archivo JSON está corrupto o mal formado.")

        else:

            if not artistas:
                print("No hay artistas registrados.")
                return

            for a in artistas:

                print("\n========================")
                print(f"Nombre: {a.get('Nombre')}")
                print(f"Fecha de formación: {a.get('Fecha de formación')}")
                print(f"País de origen: {a.get('País de origen')}")
                print(f"Activo: {'Sí' if a.get('Activo') else 'No'}")
                print(f"Género: {a.get('Género')}")
                print(f"Canciones populares: {a.get('Canciones populares')}")
                print(f"Componentes: {a.get('Componentes')}")
