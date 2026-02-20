class Coche:
    kilom_recorridos=0

    def __init__(self, matricula, marca, kilometros, gasolina):
        self.matricula = int(input('Matricula: '))
        self.marca = input('Marca: ')
        self.kilometros = 0
        self.gasolina = 0
        type(self).kilom_recorridos+= kilometros


