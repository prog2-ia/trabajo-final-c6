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


    ## ------------------------------------------------------------


    # Comprueba que numero_cancion sea de tipo int y positivo
    @property
    def numero_canciones(self):
        return self._numero_canciones

    @numero_canciones.setter
    def numero_canciones(self, valor):
        if valor is None:
            self._numero_canciones = 0
        elif isinstance(valor, int) and valor >= 0:
            self._numero_canciones = valor
        else:
            print("El numero de canciones debe ser un numero entero valido.")
            self._numero_canciones = 0


    # ------------------------------------------------------------


    #metodo que permite acceso a los albumes disponibles.
    #usamos la libreria os que nos permite manejo facil de las rutas.
    @staticmethod
    def listar_albumes(ruta="archivos/albumes"):

        #comprobamos que la carpeta de albumes existe.
        if not os.path.exists(ruta):
            print("La carpeta no existe.")
            return []

        #aqui guardamemos los albumes disponibles para cada artista.
        albumes = []

        #calculamos las rutas para cada artista.
        for artista in os.listdir(ruta):
            ruta_artista = ruta + "/" + artista
            if os.path.isdir(ruta_artista):
                for archivo in os.listdir(ruta_artista):
                    if archivo.endswith(".json"):
                        print(f"{len(albumes) + 1}- {artista}/{archivo}")
                        albumes.append(f"{artista}/{archivo}")

        #si no encontramos albumes
        if not albumes:
            print("No hay albumes disponibles.")

        #devolvemos los albumes que se han encontrado.
        return albumes


    # ------------------------------------------------------------


    #metodo que permite seleccionar un album de los disponibles
    @staticmethod
    def seleccionar_album(ruta_relativa, ruta="archivos/albumes"):

        # calculamos la ruta completa para acceder al album.
        ruta_completa = ruta + "/" + ruta_relativa
        print(f"\nCargando album '{ruta_relativa}'...")

        # abrimos el json con la ruta calculada.
        with open(ruta_completa, "r", encoding="utf-8") as f:
            canciones = json.load(f)

        # obtenemos el titulo del archivo a partir de la ruta calculada.
        archivo = ruta_relativa.split("/")[-1]

        # Si el album esta vacio, dejamos los datos como desconocidos.
        if len(canciones) == 0:
            artista_carpeta = ruta_relativa.split("/")[0]
            artista_detectado = artista_carpeta.replace("_", " ").title()

            album = Album(
                titulo=archivo.replace(".json", "").replace("_", " ").title(),
                artista=artista_detectado,
                fecha_lanzamiento=None,
                duracion="0:00",
                genero=[],
                numero_canciones=None
            )

            album.canciones_album = []
            album.ruta_archivo = ruta_completa
            return album

        # si el album tiene canciones, entonces podemos llenar datos del album.
        artista_completo = canciones[0]["Artista"]
        artista_principal, _ = Contenido.separar_artista_feat(artista_completo)

        album = Album(
            titulo=archivo.replace(".json", "").replace("_", " ").title(),
            artista=artista_principal,
            fecha_lanzamiento=canciones[0]["Fecha de lanzamiento"],
            duracion="0:00",
            genero=canciones[0]["Genero"],
            numero_canciones=len(canciones)
        )

        album.canciones_album = canciones
        album.ruta_archivo = ruta_completa
        return album


    # ------------------------------------------------------------


    #metodo para mostrar info del album.
    def mostrar_info_album(self):
        super().mostrar_info()
        print(f"Numero de canciones: {self.numero_canciones}")
        print()


    # ------------------------------------------------------------


    #metodo para mostrar todas las canciones disponibles en el album
    def mostrar_canciones_album(self):
        print("\n==== LISTADO DE CANCIONES DEL ALBUM ====")
        if self.numero_canciones == 0:
            print('El album todavia no contiene canciones.\n')
            return None

        for cancion in self.canciones_album:
            print(f"{cancion['Titulo'].title()} — {cancion['Artista'].title()} ({cancion['Duracion']})")
            print(f"Generos: {', '.join(g.title() for g in cancion['Genero'])}")
            print(f"Discografia: {cancion['Discografia'].title()}")
            print("----------------------------------------")
            print()


    # ------------------------------------------------------------


    #metodo que nos permite eliminar el album de la base de datos.
    def eliminar_album(self):
        #eliminamos el archivo json que queremos eliminar.
        os.remove(self.ruta_archivo)
        print(f"Album '{self.titulo.title()}' eliminado correctamente.")
        #comprobamos si la carpeta esta vacia para eliminarla si se da el caso.
        self.eliminar_carpeta_artista()


    # ------------------------------------------------------------


    #este metodo nos permite eliminar la carpeta del artista si no hay ninguin album dentro.
    def eliminar_carpeta_artista(self):

        #guardamos la ruta completa del archivo
        ruta_archivo = self.ruta_archivo

        # Extraemos la carpeta del artista.
        #divide el stringo empezando por la derecha usando como separador /, accediendo a la posicion 0, que es la carpeta del artista.
        carpeta_artista = ruta_archivo.rsplit("/", 1)[0]

        #Comprobamos si la carpeta realmente existe el las rutas.
        if os.path.exists(carpeta_artista):

            #si existe, miramos si hay algun archivo (album) dentro.
            archivos = os.listdir(carpeta_artista)
            #EN CASO DE QUE HAYA ALGUN ARCHIVO NO VISIBLE, ESTOS NO SE TENDRAN EN CUENTA.
            archivos_visibles = [f for f in archivos if not f.startswith(".")]

            #si no hay archivos en la carpeta.
            if len(archivos_visibles) == 0:
                #eliminamos la carpeta del artista.
                os.rmdir(carpeta_artista)
                print(f"Carpeta de {carpeta_artista.title()} eliminada por estar vacia.")

    # ------------------------------------------------------------



    #este metodo nos permitira crear la carpeta del artista nuevo que no existe en la base de datos al crear un album suyo.
    @staticmethod
    def crear_album(titulo,artista, ruta="archivos/albumes"):

        #obtenemos la ruta de la carpeta de artistas utilizando el metodo de crear la carpeta del artista.
        ruta_artista = Album.crear_carpeta_artista(artista, ruta)

        #normalizamos el nombre del archivo que vamos a guardar.
        nombre_archivo = titulo.strip().lower().replace(" ", "_") + ".json"
        #calculamos la ruta a este archivo.
        ruta_completa = ruta_artista + "/" + nombre_archivo

        #comporbamos si el album ya existe para no meter duplicatos.
        if os.path.exists(ruta_completa):
            print(f"El album '{nombre_archivo.title()}' ya existe en la base de datos.")
            #si existe, no devolvemos nada.
            return None

        #si no existe, creamos un json vacio.
        with open(ruta_completa, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)

        #mostramos por panalla que el album junto con la carpeta del artista se ha creado correctamente.
        print(f"Album '{titulo.title()}' creado correctamente.")
        return nombre_archivo


    # ------------------------------------------------------------


    #metodo nos permite anadir canciones al album.
    def anadir_cancion_existente(self, cancion):

        # normalizamos la entrada que introduce el usuario
        titulo_nuevo = cancion["Titulo"].lower().strip()
        artista_nuevo = cancion["Artista"].lower().strip()

        # comporbamos si la cancion ya existe en el album para que no haya duplicatos.
        for c in self.canciones_album:
            if c["Titulo"].lower().strip() == titulo_nuevo and c["Artista"].lower().strip() == artista_nuevo:
                print(f"La cancion '{cancion['Titulo']}' de {cancion['Artista']} ya esta en el album.")
                #si la cancion ya existe, no devolvemos nada.
                return None

        #si la cancion no existe en el album, la anadimos.
        #la discografia de la cancion anadida por logica va a ser el nombre del album.
        cancion["Discografia"] = self.titulo

        #anadimos la cancion a la lista de canciones del album.
        self.canciones_album.append(cancion)

        #esta parte nos permite actualizar la informacion del album si no habia ninguna cancion antes.
        if self.numero_canciones == 0:
            # Asignamos como artista del album el artista principal de la cancion.
            artista_principal, _ = Contenido.separar_artista_feat(cancion["Artista"])
            self.artista = artista_principal
            # Lo mismo con la fecha.
            self.fecha_lanzamiento = cancion["Fecha de lanzamiento"]
            # Y generos.
            self.genero = cancion["Genero"]

        #como hemos anadido una cancion, tenemos que actualizar el numero de canciones del album.
        self.numero_canciones = len(self.canciones_album)

        #Guardamos los cambios en el archivo json correspondiene del album sobre el cual hemos estado trabajando.
        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(self.canciones_album, f, ensure_ascii=False, indent=4)

        #mostramos que la cancion se ha anadido con exito al album.
        print(f"Cancion '{cancion['Titulo']}' anadida al album '{self.titulo.title()}'.")


    # ------------------------------------------------------------


    #este metodo nos permite mejor organizacion de albumes y artistas.
    @staticmethod
    def crear_carpeta_artista(artista, ruta_base="archivos/albumes"):

        #calculamos la ruta de la carpeta que queremos crear.
        carpeta = artista.lower().replace(" ", "_")
        ruta_artista = ruta_base + "/" + carpeta

        #si la ruta no existe, la guardamos
        if not os.path.exists(ruta_artista):
            os.makedirs(ruta_artista)

        #devolvemos la ruta.
        return ruta_artista


    # ------------------------------------------------------------


    # este metodo nos permitira eliminar una cancion del album en el que estemos.
    def eliminar_cancion_album(self, titulo, artista):

        # normalizamos los datos introducidos
        titulo = titulo.lower().strip()
        artista = artista.lower().strip()

        # calculamos cuantas canciones hay antes para confirmar eliminacion
        canciones_antes = len(self.canciones_album)
        canciones_filtradas = []

        # recorremos las canciones del album para buscar la cancion a eliminar
        for cancion in self.canciones_album:
            titulo_cancion = cancion["Titulo"].lower().strip()
            artista_completo_cancion = cancion["Artista"]

            # obtenemos el artista principal de la cancion
            artista_principal_cancion, _ = Contenido.separar_artista_feat(artista_completo_cancion)

            # si no coincide, la mantenemos
            if not (titulo_cancion == titulo and artista_principal_cancion.lower().strip() == artista):
                canciones_filtradas.append(cancion)

        # actualizamos la lista de canciones del album
        self.canciones_album = canciones_filtradas

        # actualizamos el numero de canciones del album
        self.numero_canciones = len(self.canciones_album)

        # guardamos cambios en el archivo json del album
        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(self.canciones_album, f, ensure_ascii=False, indent=4)

        # mostramos el resultado de la operacion
        if len(self.canciones_album) == canciones_antes:
            print(f"La cancion '{titulo.title()}' de {artista.title()} no existe en el album.")
        else:
            print(
                f"Cancion '{titulo.title()}' de {artista.title()} eliminada correctamente del album '{self.titulo.title()}'.")


