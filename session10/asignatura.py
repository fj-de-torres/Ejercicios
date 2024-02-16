
class Asignatura:
    def __init__(self, nombre:str, nota_corte: float):
        self.nombre = nombre
        self.nota_corte = nota_corte

    def esta_aprobada(self, nota_alumno: float) -> bool:
        return nota_alumno >= self.nota_corte   