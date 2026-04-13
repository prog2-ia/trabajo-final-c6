#clase de productor.
class Productor:
    def __init__(self,producciones):
        self.producciones = producciones or []

    #usamos getter y setter para validar que el dato que pasamos es una lista.
    @property
    def producciones(self):
        return self._producciones

    @producciones.setter
    def producciones(self,valor):
        if not  isinstance(valor,list):
            print('Las producciones deben estar contenidas en una lista.')
            self._producciones = []
        else:
            self._producciones = valor

    #metodo que permite agregar producciones.
    def agregar_producciones(self,produccion):
        self.producciones.append(produccion)

    def __iadd__(self, other):
        self.producciones.append(other)