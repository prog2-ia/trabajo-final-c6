class Coche:
    kilom_recorridos=0

    def __init__(self, matricula, marca, kilometros, gasolina):
        self.matricula = int(input('Matricula: '))
        self.marca = input('Marca: ')
        self.kilometros = 0
        self.gasolina = 0
        type(self).kilom_recorridos+= kilometros

    def __str__(self):
        return(
            f'Matricula: {self.matricula}\n'
            f'Marca: {self.marca}\n'
            f'kilometros: {self.kilometros}\n'
            f'gasolina: {self.gasolina}\n'
        )

