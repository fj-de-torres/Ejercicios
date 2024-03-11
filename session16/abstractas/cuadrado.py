from figura_geometrica import FiguraGeometrica
from os import system
from sys import path
path.append("/home/francisco/Documents/Learning/PUE/Python/Ejercicios/")
from funfont import *

class Cuadrado(FiguraGeometrica):

    """Creates an object like: object = FiguraGeometrica("nombre_figura","lado")
    where \"nombre figura\" is the proper name of a geometric figura and \"lado\" is one of its sides """

    @property
    def lado(self):
        return self.__lado
    
    def __init__(self, nombre_figura:str,lado:float) -> None:
        super().__init__(nombre_figura)
        self.__lado = lado
    
    def calcular_area(self) -> float:
        area = self.lado ** 2
        return area
    
    def calcular_perimetro(self) -> float:
        perimetro = 4 * self.lado
        return perimetro

system("cls || clear")
cuadrado1 = Cuadrado("cuadrado",2.5)
print_columna("Área del cuadrado1",cuadrado1.calcular_area())
print_columna("Perímetro de cuadrado1",cuadrado1.calcular_perimetro())
#help(object)
