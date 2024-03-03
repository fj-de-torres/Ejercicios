from collections import namedtuple
import random as rd
import math as m

class estudiantes_cls(list):
    def calcular_promedio (self):
        return sum([estudiante.nota for estudiante in self])/len(self)

def crear_lista_estudiantes(nombres: list):
    lista_estudiantes = list()
    for nombre in nombres:
        nuevo_estudiante = (nombre , rd.randint(6, 15) , rd.randint(0,100))
        lista_estudiantes.append (tuple(nuevo_estudiante))
    return lista_estudiantes


nombres = ('Diego', 'Sofia','Sira', 'Lúa', 'Ines', 'Alba')
lista_estudiantes = crear_lista_estudiantes (nombres)
estudiante = namedtuple ('Estudiante',['nombre','edad','nota'])
lista_estudiantes_named = list (map(estudiante._make, lista_estudiantes))
lista_cls = estudiantes_cls (lista_estudiantes_named)
print(lista_cls.calcular_promedio())
