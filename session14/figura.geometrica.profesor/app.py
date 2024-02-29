from rectangulo import Rectangulo
from triangulo import Triangulo
from figura_geometrica import Figura_Geometrica
from funfont import *

triangulo = Triangulo(2,3,1,2)
rectangulo = Rectangulo(2,5)

figuras: list[Figura_Geometrica] = list() #Me estoy creando una lista de objetos llamadados figuras geométricas.

figuras.append(triangulo)
#También puedo hacer:
figuras.extend([triangulo,rectangulo])

for figura in figuras:
    print(figura.calcular_area())
    print_columna(f"figura.calcular_area()",figura.calcular_area())

#columna = PrettyTable
#help(triangulo)
print(triangulo.__dict__)