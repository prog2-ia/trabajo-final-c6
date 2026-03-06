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

    # Métodos Estado_animo

    # Determinar si es un estado de animo positivo: Necesario para crear playlist
    def es_positivo(self):
        positivos = ["Feliz", "Entusiasmado", "Motivado", "Alegre"]
        return self.nombre in positivos
    #Estado de ánimo negativo
    def es_negativo(self):
        return not self.es_positivo()

    # Cambia el estado de ánimo a uno nuevo.

    def cambiar_estado(self, nuevo_nombre, nueva_descripcion):
        self.nombre = nuevo_nombre
        self.descripcion = nueva_descripcion
