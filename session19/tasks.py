class Tarea:
    def __init__(self, descripcion, fecha, prioridad):
        self.descripcion = descripcion
        self.fecha = fecha
        self.prioridad = prioridad
        self.completada = False

    def __str__(self):
        return f'{self.nombre} - {self.descripcion}'