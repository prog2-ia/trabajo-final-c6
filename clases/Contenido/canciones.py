import json
from clases.Otros.generos import Genero
from clases.Contenido.contenido import Contenido


# Clase Cancion
class Cancion(Contenido):
    #Clase Canción: hereda de Contenido.
    def __init__(self, titulo, fecha_lanzamiento, duracion, genero, artista, discografia):
        super().__init__(titulo, fecha_lanzamiento, duracion, genero, artista)
        self._discografia = discografia

    # --------------------PROPIEDADES --------------------
    #Validar que la discografia introducida sea de tipo str.
    @property
    def discografia(self):
        return self._discografia
    @discografia.setter
    def discografia(self, discografia):
        if not isinstance(discografia, str):
            print('La discografía debe ser texto')
        else:
            self._discografia = discografia

    #--------------------MÉTODOS --------------------
    def mostrar_info(self):
        print('==== CANCION ====')
        super().mostrar_info()
        print(f'Discografia: {self.discografia}')

    # Méodo estático para añadir canción al archivo JSON
    @staticmethod
    def anadir_cancion(nueva_cancion, ruta_json="archivos/canciones_guardadas.json"):
        # Entrar en el archivo canción.json como lectura
        with open(ruta_json, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        # Añadir nueva canción (convertida a diccionario)
        canciones.append({
            "Titulo": nueva_cancion.titulo,
            "Artista": nueva_cancion.artista,
            "Fecha de lanzamiento": nueva_cancion.fecha_lanzamiento,
            "Duracion": nueva_cancion.formatear_duracion(),
            "Genero": nueva_cancion.genero,
            "Discografia": nueva_cancion.discografia
        })

        # 3. Guardar de nuevo en el JSON
        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(canciones, f, ensure_ascii=False, indent=4)

        print(f"Canción '{nueva_cancion.titulo}' añadida correctamente.")