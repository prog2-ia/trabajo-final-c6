from clases.Artistas.artistas import Artista, ArtistaError
import json

#Importamos ArtistaError

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
            raise ArtistaError("El director debe ser texto.")
        self._director = valor

    @property
    def instrumentos(self):
        return self._instrumentos

    @instrumentos.setter
    def instrumentos(self, valor):
        if not isinstance(valor, list):
            raise ArtistaError ("Los instrumentos deben ser una lista.")
        self._instrumentos = valor

    # -------- MÉTODOS --------
    # Metodo para agregar miembro
    def agregar_miembro(self, nombre):
        if not isinstance(nombre, str):
            raise ArtistaError("El nombre del miembro debe ser un string.")

        if nombre in self._componentes:
            raise ArtistaError(f"El miembro {nombre} ya está en la orquesta.")

        self._componentes.append(nombre)

    # Metodo para eliminar miembro
    def eliminar_miembro(self, nombre):
        if not isinstance(nombre, str):
            raise ArtistaError("El nombre del miembro debe ser un string.")

        if nombre not in self._componentes:
            raise ArtistaError(f"El miembro {nombre} no se encuentra en la orquesta.")

        self._componentes.remove(nombre)

    # Metodo para contar componentes de la orquesta
    def __len__(self) -> int:
        return len(self._componentes)

    # Metodo para agregar instrumentos
    def agregar_instrumento(self, instrumento):
        if not isinstance(instrumento, str):
            raise ArtistaError("El instrumento debe ser un string.")

        if instrumento in self._instrumentos:
            raise ArtistaError(f"El instrumento {instrumento} ya está registrado en la orquesta.")



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

    #Metodo para guardar orquestas
    @staticmethod
    def guardar_orquesta(orquesta, ruta='archivos/artistas_guardados.json'):
        if not isinstance(orquesta, Orquestas):
            raise TypeError("Solo se pueden guardar objetos Orquestas.")

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
                "Nombre": orquesta.nombre,
                "Fecha de formación": orquesta.fecha_formacion,
                "País de origen": orquesta.pais_origen,
                "Activo": orquesta.activo,
                "Género": orquesta.genero,
                'Director': orquesta.director,
                'Instrumentos': orquesta.instrumentos

            })

            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=4)

        finally:
            print(f"Artista '{orquesta.nombre}' guardado correctamente.")