import json


from clases.Artistas.artistas import Artista
from clases.Artistas.artistas import ArtistaError



#Errores relacionados con la clase Cantante.
class CantanteError(Exception):
    pass

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
            raise CantanteError("El tipo de voz debe ser texto.")
        self._tipo_voz = "desconocido"


    # Comprueba que colaboraciones sea una lista antes de asignarlo
    @property
    def colaboraciones(self):
        return self._colaboraciones

    @colaboraciones.setter
    def colaboraciones(self, valor):
        if not isinstance(valor, list):
            raise CantanteError("Las colaboraciones deben ser una lista.")
        self._colaboraciones = []

    # Comprueba que instrumentos sea una lista antes de asignarlo
    @property
    def instrumentos(self):
        return self._instrumentos

    @instrumentos.setter
    def instrumentos(self, valor):
        if not isinstance(valor, list):
            raise CantanteError("Los instrumentos deben ser una lista.")
        self._instrumentos = []


    # -------- MÉTODOS --------

    # Metodo para agregar colaboraciones
    def agregar_colaboracion(self, colaboracion):
        if not isinstance(colaboracion, str):
            raise CantanteError("La colaboración debe ser un string.")
        self._colaboraciones.append(colaboracion)

    def __iadd__(self, colaboracion):
        if not isinstance(colaboracion, str):
            raise CantanteError("La colaboración debe ser un string.")
        self.colaboraciones.append(colaboracion)


    # Metodo para agregar instrumentos
    def agregar_instrumento(self, instrumento):
        if not isinstance(instrumento, str):
            raise CantanteError("El instrumento debe ser un string.")
        self._instrumentos.append(instrumento)

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


    #Metodo para guardar cantante
    @staticmethod
    def guardar_cantante(cantante, ruta='archivos/artistas_guardados.json'):
        if not isinstance(cantante, Cantantes):
            raise TypeError("Solo se pueden guardar objetos Cantantes.")

        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)

        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

        except json.JSONDecodeError:
            raise ArtistaError("El archivo JSON está corrupto o mal formado.")

        else:

            # Añadimos el nuevo artista.
            datos.append({
                "Nombre": cantante.nombre,
                "Fecha de formación": cantante.fecha_formacion,
                "País de origen": cantante.pais_origen,
                "Activo": cantante.activo,
                "Género": cantante.genero,
                "Canciones populares": cantante.canciones_populares,
                "Componentes": cantante.componentes,
                'Tipo de voz': cantante.tipo_voz,
                'Colaboraciones': cantante.colaboraciones,
                'Instrumentos': cantante.instrumentos

            })

            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=4)

        finally:
            print(f"Artista '{cantante.nombre}' guardado correctamente.")




