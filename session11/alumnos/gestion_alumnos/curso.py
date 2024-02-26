class Curso:
    
    def __init__(self, numero, tutor) -> None:
        self.alumnos = list()
        self.numero = numero
        self.tutor = tutor
    
    def realizar_examen(self):
        for alumno in self.alumnos:
            alumno.examinar()

    def listar_alumnos(self):
        for alumno in self.alumnos:
            print(alumno)