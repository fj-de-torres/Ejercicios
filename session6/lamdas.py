# Lamda: funciones anónimas:

def sumar(x:int, y:int) -> int:
    return x + y
def cacular_algo_complejo():
    return 10
lambda x, y : x + y # Equivale a lo anterior, pero de momento es una función anónima. No tiene nombre

sumar_lambda = lambda x, y : x + y #No puedo tipar las variables x: int, y:int, etc.

r1 = sumar_lambda(10,3)
r2 = sumar(10,3)

print(r1 == r2)
sumar_lamda2 = lamda x, y : calcular_algo_complejo() # De esta manera, podría definir funciones lamda de más de una línea de código, pouesto que en su única línea de código estoy invocando una función que sí que tiene más de una línea.

###### Otro ejemplo:

def calcular(x:int, y: int, d:dict):
    proceso1 = lambda a, b :a * x + b * y

    res = proceso1(10,1)

#### Funcionalidades lambda:
##### map -> transformación: un arreglo a la función alumnos con nota x * .5 (arreglo un resultado)
##### filtrado -> filtrado: alumnos que han obtenido una nota > 7. Me devuelve una colección que cumple las condiciones del filtrado.

alumnos = [('maite,6.0'), ('alicia', 8.0), ('luis', 7.5), ('juan',7.0)]

alumnos_mas_siete = filter()