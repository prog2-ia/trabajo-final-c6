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

    def __str__(self):
        return(
            f'Nombre del grupo/artista: {self.nombre}\n'
            f'Componente(s): {self.componentes}\n'
            f'Genero(s): {self.genero}\n'
            f'Fecha de creacion: {self.fecha_nacimiento}\n'
            f'Pais origen: {self.pais_origen}\n'
            f'Activo: {self.activo}\n'
            f'Canciones populares: {self.canciones_populares}\n'
        )

#Ejemplo de ejecucion.
'''
if __name__ == "__main__":
    grupo1 = Grupo('Bon Jovi',['Jon','David','Tico','Richie'],['Rock','Glam metal'],1983,'Estados Unidos',['Livin on a Prayer','Its My Life'],True)
    print(grupo1)
'''