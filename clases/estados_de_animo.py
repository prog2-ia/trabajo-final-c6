class EstadoAnimo:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return (f"Género: {self.nombre}\n"
                f"Descripción: {self.descripcion}")

    def __repr__(self):
        return (f"{type(self).__name__}("
                f"nombre='{self.nombre}', "
                f"descripcion='{self.descripcion}')")