from funfont import *
from os import system

class FiguraGeometrica:

    @property
    def lado1(self):
        return self._lado1
    @property
    def lado2(self):
        return self._lado2
    
    def __init__(self,lado1:float,lado2:float) -> None:
        self._lado1 = lado1
        self._lado2 = lado2
    
    def calcular_area(self,lado1:float,lado2:float)->float:
        print("Estamos trabajando en ello...")
    
class Rectangulo(FiguraGeometrica):

    def __init__(self, lado1: float, lado2: float) -> None:
        super().__init__(lado1, lado2)

    def calcular_area(self) -> float:
        return self._lado1 * self._lado2

class Triangulo(FiguraGeometrica):
    def __init__(self, lado1: float, lado2: float, altura: float) -> None:
        super().__init__(lado1, lado2)
        self._altura = altura

    @property
    def altura(self):
        return self._altura
    
    def calcular_area(self) -> float:
        return (self._lado1 * self._altura) / 2
    
system("cls || clear")
t1 = Triangulo(2,4,9)
#print(t1.calcular_area())
r1 = Rectangulo(2,4)

print_columna("t1.calcular_area()",t1.calcular_area())
print_columna("r1.calcular_area()",r1.calcular_area())

