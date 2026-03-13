import json
from clases.Otros.generos import Genero
from clases.Contenido.contenido import Contenido


# Clase Cancion
class Cancion(Contenido):
    def __init__(self, titulo, fecha_lanzamiento, duracion, genero, artista, discografia):
        super().__init__(titulo, fecha_lanzamiento, duracion, genero, artista)
        self.discografia = discografia

    def mostrar_info(self):
        print('==== CANCION ====')
        super().mostrar_info()
        print(f'Discografia: {self.discografia}')

    # Método estático para añadir canción al archivo JSON
    @staticmethod
    def añadir_cancion(nueva_cancion, ruta_json="archivos/Lista_de_canciones/canciones.json"):
        # Entrar en el archivo canción.json como lectura
        with open(ruta_json, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        # Añadir nueva canción (convertida a diccionario)
        canciones.append({
            "Titulo": nueva_cancion.titulo,
            "Artista": nueva_cancion.artista,
            "Fecha de lanzamiento": nueva_cancion.fecha_lanzamiento,
            "Duracion": nueva_cancion.duracion,
            "Genero": nueva_cancion.genero,
            "Discografia": nueva_cancion.discografia
        })

        # 3. Guardar de nuevo en el JSON
        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(canciones, f, ensure_ascii=False, indent=4)

        print(f"Canción '{nueva_cancion.titulo}' añadida correctamente.")