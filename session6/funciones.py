import os
from colorama import Fore,Back,Style

## Esto es modularizar:
from calculadora import sumar #, restar -> esta está en gris porque no existe en el otro módulo
os.system ("cls || clear")
if __name__ == "__main__":
    resultado = sumar(10,3)
    print(f"Resultado: {resultado}")

#### Método tradicional
#En este caso no he tenido que crear la función porque la importo desde "calculadora.py"
# def funcion_suma(num1,num2)
#     resultado = sumar(10,3)
#     print(f"Resultado: {resultado}")



