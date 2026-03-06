#Superclase Artista: Incluye cantantes individuales

#Añadir formato para la fecha de formacion??
class Artista:
    def __init__(self, nombre, fecha_formacion, pais_origen, activo:bool, genero=None, canciones_populares=None, componentes=None):
        self.nombre = nombre
        #Si genero es None, crea una lista nueva
        self.genero = genero or []  # Lista de géneros musicales
        self.fecha_formacion = fecha_formacion  # Fecha de nacimiento o creación del grupo
        self.pais_origen = pais_origen
        #Si canciones_populares es None, crea una lista nueva
        self.canciones_populares = canciones_populares or []
        self.activo = activo
        self.componentes = componentes or []  # Lista de componentes, vacía si es solista

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}')
        if self.componentes:
            print(f'Componentes: {self.componentes}')
        print(f'Género(s): {self.genero}')
        print(f'Fecha de formación: {self.fecha_formacion}')
        print(f'País de origen: {self.pais_origen}')
        if self.canciones_populares:
            print(f'Canciones populares: {self.canciones_populares}')
        print(f'Activo: {"Sí" if self.activo else "No"}')

