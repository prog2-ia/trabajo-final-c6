# Importamos json
import json

# Cargamos los generos validos desde el json
with open("archivos/generos_disponibles.json", "r", encoding="utf-8") as f:
    generos_validos = json.load(f)["generos"]


class Contenido:
    def __init__(self, titulo:str, fecha_lanzamiento:str, duracion:str, genero:str, artista:str, feat=None):
        # Atributos encapsulados
        self._titulo = titulo
        self._artista = artista
        self.fecha_lanzamiento = fecha_lanzamiento

        # Duración se valida y se convierte a segundos
        self._duracion = duracion
        self.validar_duracion()

        # Género se valida mediante property
        self._genero = None
        self.genero = genero


        self.feat = feat or []


    # ------------------------------------------------------------


    @property
    def feat(self):
        return self._feat

    @feat.setter
    def feat(self, valor):
        if valor is None or valor == "":
            self._feat = []
        elif isinstance(valor, str):
            self._feat = [valor.strip()]
        elif isinstance(valor, list):
            self._feat = [v.strip() for v in valor]
        else:
            print("Feat. debe ser texto o lista.")
            self._feat = []


    # ------------------------------------------------------------


    # Comprueba que titulo sea de tipo str
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not isinstance(valor, str):
            print("El título debe ser texto.")
        else:
            self._titulo = valor


    # ------------------------------------------------------------


    # Comprueba que artista sea de tipo str
    @property
    def artista(self):
        return self._artista

    @artista.setter
    def artista(self, valor):
        if valor is None:
            self._artista = None
        elif not isinstance(valor, str):
            print("El artista debe ser texto.")
        else:
            self._artista = valor


    # ------------------------------------------------------------


    # Comprueba que fecha_lanzamiento sea de tipo str
    @property
    def fecha_lanzamiento(self):
        return self._fecha_lanzamiento

    @fecha_lanzamiento.setter
    def fecha_lanzamiento(self, valor):
        if valor is None:
            self._fecha_lanzamiento = None
        elif isinstance(valor, (int, str)):
            self._fecha_lanzamiento = str(valor)
        else:
            raise TypeError("La fecha de lanzamiento debe ser un año (int) o texto.")

    # ------------------------------------------------------------


    # Valida el formato de la duracion
    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        self._duracion = valor
        self.validar_duracion()


    # ------------------------------------------------------------


    # Comprueba que el genero pertenezca al archivo json
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        if valor is None or valor == []:
            self._genero = []
            return

        generos_normalizados = [g.lower() for g in generos_validos]

        if isinstance(valor, str):
            valor = [valor]

        aceptados = []
        for g in valor:
            g_norm = g.lower()
            if g_norm in generos_normalizados:
                aceptados.append(g.capitalize())

            else:
                print(f"Género '{g}' no válido")

        self._genero = aceptados


    # ------------------------------------------------------------


    #Metodo para buscar la informacion
    def mostrar_info(self):
        print()
        print(f'Titulo: {self.titulo}')
        print(f'Artista: {self.artista_completo()}')
        print(f'Fecha de lanzamiento: {self.fecha_lanzamiento}')
        print(f'Duracion: {self.formatear_duracion()}')
        print(f'Genero(s): {self._genero}')

    def __str__(self):
        return (
            f'INFORMACION CONTENIDO'
            f"Título : {self.titulo}\n"
            f"Artista : {self.artista}\n"
            f"Feat    : {self.feat if self.feat else 'ninguno'}\n"
            f"Género  : {self.genero}\n"
            f"Duración: {self.duracion}\n"
            f"Lanzado : {self.fecha_lanzamiento}"
        )
    def __repr__(self):
        return (
            f'{type(self)}'
            f"Título : {self.titulo}\n"
            f"Artista : {self.artista}\n"
            f"Feat    : {self.feat if self.feat else 'ninguno'}\n"
            f"Género  : {self.genero}\n"
            f"Duración: {self.duracion}\n"
            f"Lanzado : {self.fecha_lanzamiento}"
        )


    # ------------------------------------------------------------


    # Metodo privado para formatear segundos
    @staticmethod
    def _formatear_segundos(total) -> str:
        if total < 3600:
            m = total // 60
            s = total % 60
            seg = f"0{s}" if s < 10 else str(s)
            return f"{m}:{seg}"
        else:
            h = total // 3600
            resto = total % 3600
            m = resto // 60
            s = resto % 60

            hor = f"0{h}" if h < 10 else str(h)
            minu = f"0{m}" if m < 10 else str(m)
            seg = f"0{s}" if s < 10 else str(s)

            return f"{hor}:{minu}:{seg}"


    # ------------------------------------------------------------


    # Validar duración: convierte mm:ss o hh:mm:ss a segundos
    def validar_duracion(self) -> int:
        if not isinstance(self._duracion, str):
            self._duracion = 0
            return self._duracion

        partes = self._duracion.strip().split(':')

        if len(partes) not in (2, 3):
            self._duracion = 0
            return self._duracion

        limpios = []
        for elemento in partes:
            elemento = elemento.strip()
            if not elemento.isdigit():
                self._duracion = 0
                return self._duracion
            limpios.append(int(elemento))

        if len(limpios) == 2:
            mm, ss = limpios
            if mm < 0 or mm > 59 or ss < 0 or ss > 59:
                self._duracion = 0
                return self._duracion
            total = mm * 60 + ss

        else:
            hh, mm, ss = limpios
            if hh < 0 or mm < 0 or mm > 59 or ss < 0 or ss > 59:
                self._duracion = 0
                return self._duracion
            total = hh * 3600 + mm * 60 + ss

        self._duracion = total
        return self._duracion


    # ------------------------------------------------------------


    # Me_todo limpio sin duplicación de código
    def formatear_duracion(self) ->str:
        return self._formatear_segundos(self._duracion)


    # ------------------------------------------------------------


    #Metodo estatico para mostrar la duracion
    #Calcula la duración total de una lista de objetos Contenido y la devuelve en formato HH:MM:SS o MM:SS.
    @staticmethod
    def calcular_duracion_contenidos(contenidos: list["Contenido"]) -> str:
        total_segundos = sum(c.duracion for c in contenidos if isinstance(c, Contenido))
        return Contenido._formatear_segundos(total_segundos)
    # ------------------------------------------------------------


    #esta funcion sirve para calcular el artista completo de la cancion (para mostrarlos)
    def artista_completo(self):

        #si no tenemos artista asignado, devolvemos valor por defecto.
        if not self.artista:
            return "varios"

        #si es una lista, las juntasmo.
        if isinstance(self.artista, list):
            return ", ".join(a.title() for a in self.artista)

        #devolvemos.
        return self.artista.title()

    # ------------------------------------------------------------


    #como mostramos los artistas con feat. esta funcion nos servira para separar el artista principal del resto.
    @staticmethod
    def separar_artista_feat(artista: str):

        #Nos aseguramos de que el artista viene dado como una cadena de texto.
        if not isinstance(artista, str):
            #si no, devolvemos por defecto versiones vacias.
            return "", []

        #obtenemos y normalizamos el texto de artista que recibimos
        artista_normalizado = artista.strip().lower()

        #calculamos el indice donde se encuentra la palabra feat.
        posicion = artista_normalizado.find("feat.")
        #si no aparece feat:
        if posicion == -1:
            #devolvemos solo el artista, pues no hay colaboracion.
            return artista_normalizado, []

        #en caso de que haya feat.
            #obtenemos el artista principal
        artista_principal = artista_normalizado[:posicion].strip()
        #normalizamos el artista principal para poder devolverlo guapo y limpio.
        artista_principal = artista_principal.rstrip("-").rstrip(",").strip()

            #controlamos la parte despues del feat (las colaboraciones)
        feats_normalizados = artista_normalizado[posicion + len("feat."):].strip()
        feats = [f.strip() for f in feats_normalizados.split(",") if f.strip()]

        #devolvemos el artista principal, y los feats si los hay.
        return artista_principal, feats