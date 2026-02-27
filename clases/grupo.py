#clase grupos del proyecto.

class Grupo:
    def __init__(self, nombre, componentes, genero, fecha_nacimiento, pais_origen, canciones_populares, activo=True):
        self.nombre = nombre
        self.componentes = componentes #Una lista de componentes (en caso de que sea un grupo habra mas componentes)
        self.fecha_nacimiento = fecha_nacimiento #Fecha de creacion del grupo/artista
        self.pais_origen = pais_origen #Pais origen
        self.genero = genero #Genero musical del grupo/artista (puede ser de mas generos por eso es lista)
        self.activo = activo #Numero de anyos activo
        self.canciones_populares = canciones_populares #lista de canciones populares del grupo/artista

    # la funcion que nos sirve para mostrar la inforamacion almacenada de los artistas.
    def mostrar_info(self):
        print(f'Nombre del grupo/artista: {self.nombre}')
        print(f'Componentes: {self.componentes}')
        print(f'Genero: {self.genero}')
        print(f'Fecha de formacion: {self.fecha_nacimiento}')
        print(f'Pais de origen: {self.pais_origen}')
        print(f'Canciones Populares: {self.canciones_populares}')
        print(f'Activo: {"Si" if self.activo == True else "No"}')



#-------------------------------------------
if __name__ == "__main__":
    grupo1 = Grupo('Bon Jovi',['Jon','David','Tico','Richie'],['Rock','Glam metal'],1983,'Estados Unidos',['Livin on a Prayer','Its My Life'],True)
    grupo1.mostrar_info()
