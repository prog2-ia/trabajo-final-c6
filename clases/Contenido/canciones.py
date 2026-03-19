import json
from clases.Contenido.contenido import Contenido

# Clase Cancion
class Cancion(Contenido):
    # Clase Canción: hereda de Contenido.
    def __init__(self, titulo, fecha_lanzamiento, duracion, genero, artista, discografia):
        super().__init__(titulo, fecha_lanzamiento, duracion, genero, artista)
        self.discografia = discografia

    # -------------------- PROPIEDADES --------------------
    @property
    def discografia(self):
        return self._discografia

    @discografia.setter
    def discografia(self, valor):
        if not isinstance(valor, str):
            print("La discografía debe ser texto.")
            self._discografia = "desconocida"
        else:
            self._discografia = valor

    # -------------------- MÉTODOS --------------------
    def mostrar_info(self):
        print("==== CANCION ====")
        super().mostrar_info()
        print(f"Discografia: {self.discografia}")

    @staticmethod
    def anadir_cancion(nueva_cancion, ruta_json="archivos/canciones_guardadas.json"):

        with open(ruta_json, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        canciones.append({
            "Titulo": nueva_cancion.titulo,
            "Artista": nueva_cancion.artista,
            "Fecha de lanzamiento": nueva_cancion.fecha_lanzamiento,
            "Duracion": nueva_cancion.formatear_duracion(),
            "Genero": nueva_cancion.genero,
            "Discografia": nueva_cancion.discografia
        })

        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(canciones, f, ensure_ascii=False, indent=4)

        print(f"Canción '{nueva_cancion.titulo}' añadida correctamente.")