# Subclases específicas con métodos propios
from orquesta import Orquestas


class Duo(Orquestas):
    def es_duo(self):
        if len(self.componentes) == 2:
            print("Es un duo")
        else:
            print("No es un duo")


class Trio(Orquestas):
    def es_trio(self):
        if len(self.componentes) == 3:
            print("Es un trio")
        else:
            print("No es un trio")

class Cuarteto(Orquestas):
    def es_cuarteto(self):
        if len(self.componentes) == 4:
            print("Es un cuarteto")
        else:
            print("No es un cuarteto")

class Sinfonica(Orquestas):

    def agregar_seccion(self, seccion):
        if seccion not in self.instrumentos:
            self.instrumentos.append(seccion)
            print(f"Sección {seccion} agregada a la Sinfónica")
        else:
            print(f" La sección {seccion} ya existe")