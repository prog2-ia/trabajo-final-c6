# clase de album
from clases.Contenido.contenido import Contenido
import json
import os

#Clase Album que hereda de contenido
class Album(Contenido):
    def __init__(self, titulo, artista, fecha_lanzamiento, duracion, genero,
                 numero_canciones):
        super().__init__(titulo, fecha_lanzamiento, duracion, genero, artista)

        # VALIDAMOS USANDO LOS SETTERS
        self.numero_canciones = numero_canciones

    # -------- PROPIEDADES --------
    # Comprueba que numero_cancion sea de tipo int y positivo
    @property
    def numero_canciones(self):
        return self._numero_canciones

    @numero_canciones.setter
    def numero_canciones(self, valor):
        if not isinstance(valor, int) or valor < 1:
            print("El número de canciones debe ser un entero positivo.")
            self._numero_canciones = 0     # deja un valor seguro
        else:
            self._numero_canciones = valor

    # -------- MÉTODOS --------

    #metodo que permite acceso a los albumes disponibles.
    #usamos la libreria os que nos permite manejo facil de las rutas.
    @staticmethod
    def listar_albumes(ruta="archivos/albumes"):

        #comprobamos si la ruta (archivos/albumes) existe.
        if os.path.exists(ruta):
            #recorremos la carpeta y apuntamos todos los archivos json, que son nuestros albumes.
            archivos = [album for album in os.listdir(ruta) if album.endswith(".json")]
        else:
            print("La carpeta no existe.")
            return []

        #si hay albumes en la lista (es decir, hemos encontrado en el paso anterior).
        if archivos:
            #mostramos todos enumerados.
            for i, nombre in enumerate(archivos, start=1):
                print(f"{i}- {nombre}")
        else:
            print("No hay albumes disponibles.")

        #devolvemos los albumes disponibles.
        return archivos

#--------------------------------------------------------

    #metodo que permite seleccionar un album de los disponibles
    @staticmethod
    def seleccionar_album(nombre_archivo, ruta="archivos/albumes"):

        #calculamos la ruta a base de lo que ha elegido el usuario.
        ruta_completa = ruta + "/" + nombre_archivo
        print(f"\nCargando album '{nombre_archivo}'...")

        #cargamos el archivo json con la ruta correspondiente.
        with open(ruta_completa, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        #comprobamos si el album contiene canciones.
        if len(canciones) == 0:
            print("El album esta vacío y no contiene ninguna cancion.")

            #si no contiene nada, preguntamos si eliminamos el album.
            opcion = input("Quieres eliminar el album vacio? (s/n): ").strip().lower()

            #validamos la opcion.
            while opcion not in ("s", "n"):
                print("Opcion no valida. Solo puedes escribir 's' o 'n'.")
                opcion = input("Quieres eliminar este album vacio? (s/n): ").strip().lower()

            #eliminamos o no segun la eleccion.
            if opcion == "s":
                os.remove(ruta_completa)
                print(f"Album '{nombre_archivo}' eliminado correctamente.")
            else:
                print("No se ha eliminado el album.")
            return None

        #creamos un objeto de clase album.
        album = Album(
            titulo=nombre_archivo.replace(".json", "").replace("_", " ").title(),
            artista=canciones[0]["Artista"],
            fecha_lanzamiento=canciones[0]["Fecha de lanzamiento"],
            duracion="0:00",
            genero=canciones[0]["Genero"],
            numero_canciones=len(canciones)
        )

        #guardamos las canciones para el album elegido
        album.canciones_album = canciones
        #guardamos la ruta del archivo que hemos abierto.
        album.ruta_archivo = ruta_completa
        #devolvemos el objeto para poder trabajar con el.
        return album

    #------------------------------------------------

    #metodo para mostrar info del album.
    def mostrar_info_album(self):
        print("\n==== INFORMACION DEL ALBUM ====")
        print(f"Titulo: {self.titulo}")
        print(f"Artista: {self.artista}")
        print(f"Año de lanzamiento: {self.fecha_lanzamiento}")
        print(f"Genero(s): {self.genero}")
        print(f"Numero de canciones: {self.numero_canciones}")
        print()

    #metodo para mostrar todas las canciones disponibles en el album
    def mostrar_canciones_album(self):
        print("\n==== LISTADO DE CANCIONES DEL ALBUM ====")
        for cancion in self.canciones_album:
            print(f"{cancion['Titulo']} — {cancion['Artista']} ({cancion['Duracion']})")
            print(f"Generos: {', '.join(cancion['Genero'])}")
            print(f"Discografia: {cancion['Discografia']}")
            print("----------------------------------------")
            print()

    #metodo que nos permite eliminar el album de la base de datos.
    def eliminar_album(self):
        os.remove(self.ruta_archivo)
        print(f"Album '{self.titulo}' eliminado correctamente.")
