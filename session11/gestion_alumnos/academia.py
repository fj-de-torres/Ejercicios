from gestion_alumnos.crud import *
from gestion_alumnos.curso import Curso
class Academia:
    #datos
   
""" 
    #comportamiento:
    def matricular_alumnos(*alumnos: tuple, curso):
        curso.alumnos = list(alumnos)

        #[matricular() for alumno in alumnos ]#Porque matricular() matricular uno, a uno. También le paso el curso al cual se van a matricular
 """

class Academia:

    #comportamiento
    def matricular_alumnos(curso: Curso, *alumnos: tuple):
        curso.alumnos = list(alumnos)
        return curso      
