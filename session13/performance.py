import time
from os import system

#para medición de tiempo en el que una función realiza una tarea:

def medicion_rendimiento(func):
    start = time.time() #es lo que inicia el crono
    func() #Le paso la función a medir.
    end = time.time()
    print(end - start)

def procesar(limite: int):
    return [x**2 for x in range(limite)]

system("cls || clear")
medicion_rendimiento(lambda : procesar(50000)) # porque no se le pueden pasar parámetros a la función a medir. Sólo la funcíon
print("-"*50)
import timeit

print(timeit.timeit("[x**2 for x in range(100)]"))
print(timeit.timeit("map(lambda x: x**2, range(100))"))
