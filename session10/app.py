# Objetos en Pyhton *(Objects in Python)*:
import os
from escuela import Escuela
from curso import Curso
from asignatura import Asignatura
from alumno import Alumno


os.system("cls || clear")
#Moveré las clases a módulos. Es decir, archivos distintos.
#Las clases se crean con la palabra reservada class. La convención es que sus nombre empienzan en mayúsculas:


if __name__=="__main__":
    pass
    #Crear una escuela:
    pue = Escuela("PUE","Fernando") #Acabo de instanciar el objeto PUE a través de la clase escuela.

    """ 
    print(pue.nombre)
    print(pue.director)
 """

    #Crear los cursos de esa escuela y asociarlos a la misma:
    python_essentials_1 = Curso("PCAP1")
    python_essentials_2 = Curso("PCAP2")
    pue.anyadir_curso(python_essentials_1)
    pue.anyadir_curso(python_essentials_2)
    #Crear los alumnos de os cursos de la escuela:
    juan = Alumno('Juan Palomo', 23, 123)
    maria = Alumno ('Maria Pelaez', 22, 1234)
    luis = Alumno('Luis Aute', 21, 12345)
    alicia = Alumno('Alicia Perez', 21, 123456)
    jaime = Alumno('Jaime Urrutia',24,1234567)

#### Asignaturas: 
    mates = Asignatura("Matemáticas", 6.8)
    ingles = Asignatura("Inglés",6.0)
    programacion = Asignatura("Programación", 7.0)

""" 
    python_essentials_1.matricular(juan)
    python_essentials_1.matricular(maria)
    python_essentials_1.matricular(luis)
 """
python_essentials_1.matricular(juan, maria, luis)
    #Asocial los alumnos a las asignaturas

#Listado de alumnos:
""" 
pue.listar_alumnos()
 """
python_essentials_2.matricular(alicia,jaime)



#### Matriculado de alumnos:
#1. Opción 1:

#2. Opción 2:
python_essentials_1.matricular_asignaturas(mates,ingles) #Cada curso matricula sus asignaturas
python_essentials_2.matricular_asignaturas(programacion)
pue.listar_alumnos()

"""
a, b = ['1,'2']
a = 1
b = 2
Si tengo ([1,2]) y necesito (1,2)
quiero eliminar (dejar volar todo lo que hay dentro de la tupla. La tupla no "volará" porque es fija)
"""