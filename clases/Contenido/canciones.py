import json
import from clases.Otros.generos import Genero

#Importamos
with open("archivos/Lista_de_canciones/canciones.json", "r", encoding="utf-8") as f:
    canciones = json.load(f)




from clases.Contenido.contenido import Contenido

class Cancion(Contenido):
    def __init__(self,titulo, fecha_lanzamiento, duracion,genero,artista, discografia):
        super().__init__(titulo,fecha_lanzamiento,duracion,genero,artista)
        self.discografia = discografia

    def mostrar_info(self):
        print('==== CANCION ====')
        super().mostrar_info()
        print(f'Discografia: {self.discografia}')

#-----------------------------------------
    def añadir_cancion(self, cancion):




