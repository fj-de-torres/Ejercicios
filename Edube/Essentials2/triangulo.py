"""
Ahora vamos a colocar la clase Point (ver Lab 3.4.1.14) dentro de otra clase. Además, vamos a poner tres puntos en una clase, lo que nos permitirá definir un triángulo.¿Cómo podemos hacerlo?

La nueva clase se llamará Triangle y esto es lo que queremos:

    El constructor acepta tres argumentos - todos ellos son objetos de la clase Point.
    Los puntos se almacenan dentro del objeto como una lista privada
    La clase proporciona un método sin parámetros llamado perimeter(), que calcula el perímetro del triángulo descrito por los tres puntos; el perímetro es la suma de todas las longitudes de los lados (lo mencionamos para que conste, aunque estamos seguros de que tú mismo lo conoces perfectamente).

Completa la plantilla que te proporcionamos en el editor, ejecuta tu código y verifica si tu salida se ve igual que la nuestra:

Salida esperada

3.414213562373095
"""
import os
from sys import path

where_am_i = os.path.dirname(__file__)
if 'Ejercicios' in where_am_i:
    while os.path.basename(os.getcwd()) != 'Ejercicios':
        os.chdir('..')

current_path = os.getcwd()
path.append(current_path)

from funfont import *
os.chdir(where_am_i)

from cartesianas import Point
import math



class Triangle:

    @property
    def vertice1(self):
        return self.__vertice1
    @property 
    def vertice2(self):
        return self.__vertice2
    @property
    def vertice3(self):
        return self.__vertice3
    
    def __init__(self, point1:Point, point2:Point, point3:Point):
        self.__vertice1 = point1
        self.__vertice2 = point2
        self.__vertice3 = point3

    def perimeter(self):

        return self.vertice1.distance_from_point(self.vertice2) + self.vertice1.distance_from_point(self.vertice2) + self.vertice2.distance_from_point(self.vertice3)
        

os.system("cls || clear")

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
