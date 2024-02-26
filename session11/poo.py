from gestion_alumnos.crud import *
from gestion_alumnos.curso import Curso


if __name__ == "__main__":
    
    academia = Academia()
    curso = Curso(1, 'Luis Garcia')

    academia.matricular_alumnos(curso, Alumno(1,'Koldo','Lopez',1), Alumno(2,'Maria','Lopez',1))
    
    curso.listar_alumnos(curso)
    
    curso.realizar_examen()
