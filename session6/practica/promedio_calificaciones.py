"""
# Promedio de Calificaciones por Asignatura
### Se desea escribir un programa que calcule el promedio de calificaciones de los estudiantes en diferentes asignaturas. Cada asignatura y las calificaciones de los estudiantes para esa asignatura serán ingresadas por el usuario. El programa debe ser capaz de mostrar el promedio de calificaciones para cada asignatura.

## Objetivos:
1. Permitir al usuario ingresar múltiples asignaturas y las calificaciones correspondientes de los estudiantes.
2. Calcular el promedio de calificaciones para cada asignatura.
3. Mostrar el promedio de calificaciones por asignatura.
"""
import os
from colorama import Fore, Back, Style

os.system("cls || clear")

### 1. Opción 1. Pido nombre de cada estudiante y, a continuación, una asignatura y una nota
### 2. Opción 2. La lista de estudiantes es conocida y sólo se necesitan las asignaturas y sus notas. 

### 3. Opción 3. Me centro en obtener conjuntos (diccionarios) de asignatura - notas.
        ####1. Pido nombre de asignatura
        ####2. Pido lista de notas para esa asignatura.
        ####3.
### 4. Calcular el promedio de las calificaciones (¿average()?) para cada lista de asignaturas
### 5. Mostrar el promedio el promedio obtenido (print con formato de average)

### 3. Opción 3. Me centro en obtener conjuntos (diccionarios) de asignatura - notas.
    ##### 1. I request the user:
""" 
marks = None
subject = None
subject_list = list()
subject_and_marks_list = dict()


def get_subject():
    subject = input("Please, enter subject name: ")
    return subject

def get_marks () -> list:
    marks_list = list()
    subject_and_marks_list = dict()
    subject = get_subject()
    marks_list = input("Please enter marks separted by space: ").split()
    marks_list_floated = list(map(lambda lista_notas :float(lista_notas),marks_list))
    print(marks_list_floated)
    #Alternative way of turning the list of string marks into float:
    for indice,nota in enumerate(marks_list):
        marks_list[indice] = float(nota)
        print(indice,type(marks_list[indice]),marks_list[indice])

def link_subject_marks(subject:str,marks_list:tuple) -> dict:
    subject_and_marks_list[subject] = marks_list
    # print(marks_list)
    # print(subject_and_marks_list)
    return subject_and_marks_list

def marks_average(subject:str) -> float:
    marks = subject_and_marks_list[subject]
    suma = sum(marks)
    marks_number = len(marks)
    return suma / marks_number

subject = get_subject()
marks_list = get_marks()
print(link_subject_marks(subject,marks_list))
print(subject_and_marks_list)
#print(marks_average(subject_and_marks_list,"lengua"))
 """
#Create diccionary pair subject <-> marks list: I request the user to enter the name of a subject followed by a list of marks separated by spaces:
class_dictionary = dict()
def subject_marks_dic(subject:str,marks_list:list) -> dict:
    subject = input("Please enter subject name: ")
    marks_list = input("Please enter marks separated by one space:")
    marks_floated_list = list(map(lambda marks : float(marks),marks_list))
    class_dictionary.update{subject : marks_floated_list}
    return class_dictionary

def marks_average(marks_dictionary:dict) -> float:
    marks = marks_dictionary.values()
    marks_average = lambda class_dictionary : sum(marks)/len(marks)
    return marks_average

