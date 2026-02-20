#Clase persona para el ejercicio de clase.

class Persona:
    def __init__(self, dni, nombre, apellido, coche=False):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.coche = coche

    def __str__(self):
        return(
            f'dni: {self.dni} \n'
            f'nombre: {self.nombre} \n'
            f'apellido: {self.apellido} \n'
            f'coche: {self.coche} \n'
        )
