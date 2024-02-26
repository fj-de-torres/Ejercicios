from gestion_alumnos.crud import *
from gestion_alumnos.curso import Curso


if __name__ == "__main__":
    
    curso = Curso(1, 'Luis Garcia')
    
    matricular(3,'Koldo','Lopez',1, curso)
    #print(clase)
    mostrar_alumnos(curso)
    print("_" * 40)
    matricular(1,'Maria','Lopez',1, curso)
    mostrar_alumnos(curso)

    curso.realizar_examen()
