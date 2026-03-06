class Contenido:
    def __init__(self,titulo, fecha_lanzamiento, duracion,genero,artista, estado_reproduccion=False):
        self.titulo = titulo
        self.artista = artista
        self.fecha_lanzamiento = fecha_lanzamiento
        self.duracion = duracion
        #validamos el formato y convertimos la duraciona a segundos
        self.validar_duracion()
        self.genero = genero
        self.estado_reproduccion = estado_reproduccion

    # el metodo que nos sirve para mostrar toda la inforamcion del contendido (sea cancion, playlist, ...) la usaremos luego en la herencia.
    def mostrar_info(self):
        print(f'Titulo: {self.titulo}')
        print(f'Artista: {self.artista}')
        print(f'Fecha de lanzamiento: {self.fecha_lanzamiento}')
        print(f'Duracion: {self.formatear_duracion()}')
        print(f'Genero: {self.genero}')
        print(f'Estado de reproduccion: {"reproduciendo" if self.estado_reproduccion == True else "pausado"}')


    #metodos-------------------------------------------------------------------------------------------------

    #metodo de validar la duracion (recibe una cadena y convierte a segundos para poder operar con segundos):
    #como no hemos visto manejo de errores, si hay formato incorrecto o algo no cumple, pongo la duracion a 0.
    def validar_duracion(self):
        total = 0
        #comprobamos que es una cadena de texto
        if not isinstance(self.duracion,str):
            self.duracion = 0
            return self.duracion
        #hemos dicho que viene por por defecto el formato mm:ss
        partes = self.duracion.strip().split(':')
        #puede tener dos partes mm:ss o tres partes hh:mm:ss
        if len(partes) == 2 or len(partes)==3:
            #creamos una lista vacia para guardar los numeros y calcular los segundos.
            limpios = []
            for elemento in partes:
                elemento = elemento.strip()
                if elemento == '' or not(elemento.isdigit()):
                    self.duracion = 0
                    return self.duracion
                else:
                    limpios.append(elemento)
        else:
            self.duracion = 0
            return self.duracion
        #validamos los numeros introducidos en la cadena
        if len(partes)==2:
            #formato mm:ss
            numeros = []
            for elemento in limpios:
                numeros.append(int(elemento))
            mm = numeros[0]
            ss = numeros[1]
            #validamos los rangos temporales
            if mm < 0:
                self.duracion = 0
                return self.duracion
            if mm > 59:
                self.duracion = 0
                return self.duracion
            if ss < 0 or ss > 59:
                self.duracion = 0
                return self.duracion
            total +=mm * 60 + ss

        else:
            # formato hh:mm:ss
            numeros = []
            for elemento in limpios:
                numeros.append(int(elemento))
            hh = numeros[0]
            mm = numeros[1]
            ss = numeros[2]
            #validamos los rangos temporales
            if hh < 0:
                self.duracion = 0
                return self.duracion
            if mm < 0 or mm > 59:
                self.duracion = 0
                return self.duracion
            if ss < 0 or ss > 59:
                self.duracion = 0
                return self.duracion
            total += hh*3600+mm*60+ss

        self.duracion = total
        return self.duracion

    # metodo de formatear la duracion (recibe segundos caluclados por la funcion anterior y devuelve un formato de duracion):
    def formatear_duracion(self):
        total = self.duracion
        if total < 3600:
            m = total // 60
            s = total % 60
            if s < 10:
                seg = '0'+str(s)
            else:
                seg = str(s)
            resultado = str(m) + ':' + seg
        else:
            h = total //3600
            resto = total %3600
            m = resto//60
            s = resto % 60
            if h < 10:
                hor = '0'+str(h)
            else:
                hor = str(h)
            if m < 10:
                minu = '0'+str(m)
            else:
                minu = str(m)
            if s < 10:
                seg = '0'+str(s)
            else:
                seg = str(s)
            resultado = hor + ':' + minu + ':' + seg
        return resultado

    def validar_titulo(self):
        if self.titulo