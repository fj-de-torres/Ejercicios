#dominio: gestion academica
#ED - lista Alumnos
from gestion_alumnos.crud import *
class Curso:

class Curso:
    
    def __init__(self, numero, tutor) -> None:
        self.alumnos = list()
        self.numero = numero
        self.tutor = tutor
    
    def realizar_examen(self, ):
        for alumno in self.alumnos:
            alumno.examinar()


if __name__ == "__main__":
    
    curso = [] # como programa principal

    matricular(3,'Koldo','Lopez',1, curso)
    #print(clase)
    mostrar_alumnos(curso)
    print("_" * 40)
    matricular(1,'Maria','Lopez',1, curso)
    mostrar_alumnos(curso)
    
    realizar_examen(curso)