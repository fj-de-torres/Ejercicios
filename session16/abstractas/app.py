from cuadrado import Cuadrado
from triangulo import Triangulo
from sys import path
path.append("/home/francisco/Documents/Learning/PUE/Python/Ejercicios/")
from funfont import *
from os import system

if __name__ == "__main__":

    system("cls || clear")
    triangulo1 = Triangulo("Triángulo1",7,7,7,7 * .5)
    print_columna("Área triángulo 1",triangulo1.calcular_area())
    print_columna("Perímetro triángulo1",triangulo1.calcular_perimetro())

