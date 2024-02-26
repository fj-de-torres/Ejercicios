class Alumno:
    #datos (atributos, estado)
    def __init__(self, indent: str, nombre: str, apellido: str, curso: int ):
        self.identificador = indent
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.notas = []

    #comportamiento (responsabilidad)
    #metodo magico
    def __str__(self):
        return f"{self.nombre} {self.apellido}"    