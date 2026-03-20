# Importamos json
import json

# Cargamos los géneros válidos desde el JSON
with open("archivos/generos_disponibles.json", "r", encoding="utf-8") as f:
    generos_validos = json.load(f)["generos"]


class Contenido:

    def __init__(self, titulo, fecha_lanzamiento, duracion, genero, artista):
        # Atributos encapsulados
        self._titulo = titulo
        self._artista = artista
        self._fecha_lanzamiento = fecha_lanzamiento

        # Duración se valida y se convierte a segundos
        self._duracion = duracion
        self.validar_duracion()

        # Género se valida mediante property
        self._genero = None
        self.genero = genero

    #--------------------PROPIEDADES --------------------

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

    # Comprueba que artista sea de tipo str
    @property
    def artista(self):
        return self._artista

    @artista.setter
    def artista(self, valor):
        if not isinstance(valor, str):
            print("El artista debe ser texto.")
        else:
            self._artista = valor

    # Comprueba que fecha_lanzamiento sea de tipo str
    @property
    def fecha_lanzamiento(self):
        return self._fecha_lanzamiento

    @fecha_lanzamiento.setter
    def fecha_lanzamiento(self, valor):
        if not isinstance(valor, str):
            print("La fecha de lanzamiento debe ser texto.")
        else:
            self._fecha_lanzamiento = valor

    # Valida el formato de la duracion
    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        self._duracion = valor
        self.validar_duracion()

    # Comprueba que el genero pertenezca al archivo json
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        generos_normalizados = [g.lower() for g in generos_validos]

        if isinstance(valor, str):
            valor = [valor]

        aceptados = []
        for g in valor:
            g_norm = g.lower()
            if g_norm in generos_normalizados:
                aceptados.append(g)
            else:
                print(f"Género '{g}' no válido")

        self._genero = aceptados

    #-------------------- MÉTODOS ---------------------------

    #Metodo para buscar la informacion
    def mostrar_info(self):
        print(f'Titulo: {self.titulo}')
        print(f'Artista: {self.artista}')
        print(f'Fecha de lanzamiento: {self.fecha_lanzamiento}')
        print(f'Duracion: {self.formatear_duracion()}')
        print(f'Genero(s): {self._genero}')

    # Metodo privado para formatear segundos
    @staticmethod
    def _formatear_segundos(total):
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

    # Validar duración: convierte mm:ss o hh:mm:ss a segundos
    def validar_duracion(self):
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

    # Me_todo limpio sin duplicación de código
    def formatear_duracion(self):
        return self._formatear_segundos(self._duracion)

    #Metodo estatico para mostrar la duracion
    @staticmethod
    def mostrar_duracion(lista_contenidos):
        total_segundos = sum(con.duracion for con in lista_contenidos)

        # Creamos objeto temporal solo para formatear
        temp = Contenido("temp", "temp", "0:00", "temp", "temp")
        resultado = temp._formatear_segundos(total_segundos)

        print("Duración total de la playlist:", resultado)
        return resultado