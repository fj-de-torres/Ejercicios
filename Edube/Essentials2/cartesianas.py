"""
Cada punto ubicado en el plano puede describirse como un par de coordenadas habitualmente llamadas x y y. Queremos que escribas una clase en Python que almacene ambas coordenadas como números flotantes. Además, queremos que los objetos de esta clase evalúen las distancias entre cualquiera de los dos puntos situados en el plano.

La tarea es bastante fácil si empleas la función denominada hypot() (disponible a través del módulo math) que evalúa la longitud de la hipotenusa de un triángulo rectángulo (más detalles aquí: https://en.wikipedia.org/wiki/Hypotenuse) y aquí: https://docs.python.org/3.7/library/math.html#trigonometric-functions.

Así es como imaginamos la clase:

    Se llama Point.
    Su constructor acepta dos argumentos (x y y respectivamente), ambos por defecto se igualan a cero.
    Todas las propiedades deben ser privadas.
    La clase contiene dos métodos sin parámetros llamados getx() y gety(), que devuelven cada una de las dos coordenadas (las coordenadas se almacenan de forma privada, por lo que no se puede acceder a ellas directamente desde el objeto).
    La clase proporciona un método llamado distance_from_xy(x,y), que calcula y devuelve la distancia entre el punto almacenado dentro del objeto y el otro punto dado en un par de números flotantes.
    La clase proporciona un método llamado distance_from_point(point), que calcula la distancia (como el método anterior), pero la ubicación del otro punto se da como otro objeto de clase Point.

Completa la plantilla que te proporcionamos en el editor, ejecuta tu código y verifica si tu salida se ve igual que la nuestra.
Salida esperada

1.4142135623730951
1.4142135623730951
"""
import os
import math
from sys import path

where_am_i = os.path.dirname(__file__)
if 'Ejercicios' in where_am_i:
    while os.path.basename(os.getcwd()) != 'Ejercicios':
        os.chdir('..')
current_path = os.getcwd()

#current_directory = os.path.basename(current_path)
path.append(current_path)
os.chdir(where_am_i)
from funfont import *
def clear():
    os.system("cls || clear")

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def __mensajito(self):
        print(funfont("Yo, hipotenuso")+","+ Style.BRIGHT + " por tus coordenadas, así te uso:"+ Style.NORMAL,sep="\n",end=" ")
    def __str__(self):
        return f"{self.__x,self.__y}"
    
    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        distance = math.hypot(x-self.__x,y-self.__y)
        self.__mensajito()
        print("\n")
        return distance

    def distance_from_point(self, point):
        #point = tuple(point)
        distance = math.hypot(point.getx()-self.__x,point.gety()-self.__y)
        self.__mensajito()
        print("\n")
        return distance

clear()

point1 = Point(0, 0)
point2 = Point(1, 1)
#print(point2)
print_columna("point1.distance_from_point(point2)",point1.distance_from_point(point2))
clear()

#linea(times=100)
print_columna("point2.distance_from_xy(2, 0)",point2.distance_from_xy(2, 0))
print()
