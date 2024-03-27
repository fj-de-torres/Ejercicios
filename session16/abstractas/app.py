import os
from sys import path
from cuadrado import Cuadrado
from triangulo import Triangulo

where_am_i = os.path.dirname(__file__)
if 'Ejercicios' in where_am_i:
    while os.path.basename(os.getcwd()) != 'Ejercicios':
        os.chdir('..')

current_path = os.getcwd()
path.append(current_path)

from funfont import *
os.chdir(where_am_i)

if __name__ == "__main__":

    os.system("cls || clear")
    triangulo1 = Triangulo("Triángulo1",7,7,7,7 * .5)
    print_columna("Área triángulo 1",triangulo1.calcular_area())
    print_columna("Perímetro triángulo1",triangulo1.calcular_perimetro())

