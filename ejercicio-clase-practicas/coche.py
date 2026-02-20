class Coche:
    kilom_recorridos=0

    def __init__(self, matricula, marca, kilometros=0, gasolina=0):
        self.matricula = matricula
        self.marca = marca
        self.kilometros = kilometros
        self.gasolina = gasolina
        type(self).kilom_recorridos+= self.kilometros

    def __str__(self):
        return(
            f'Matricula: {self.matricula}\n'
            f'Marca: {self.marca}\n'
            f'kilometros: {self.kilometros}\n'
            f'gasolina: {self.gasolina}\n'
        )

