import os
from colorama import Fore,Back,Style
#### Se recomienda cargar únicamente las funciones que necesitaré de cada módulo que importe, puesto que todo lo que importe se va a cargar en memoria. Importar con un *, lo importa TODO de un módulo.
## Esto es modularizar:
from calculadora import sumar, sumar_v2, restar #-> esta está en gris porque no existe en el otro módulo
# #### Si importo el módulo directamente:
# import calculadora
# #pues entonces tengo que llamar a las funciones de esta manera:
# resultado = calculadora.sumar(10,3)
# print(f"Resultado: {resultado}")

#Y podemos utilizar alias:
#import calculadora as calc, y usar la función azín:

#resultado = calc.sumar(10,3)
#print("Resultado: {resultado}")

os.system ("cls || clear")

def matricular_alumnos(curso: dict, **d_alumnos): #Recordar que lo opcional ha de estar al final. Por eso pongo primero "curso"
    curso.update(d_alumnos)
    return curso

if __name__ == "__main__": #Todo lo que va a continuación se ejecuta si se trata del programa principal

    alumnos = dict(a=1) #Se podrá hacer cuando el key sea un string. Es válida pero poco versátil (a=1, etc)
    alumnos = {
        "111H": ("juan",19),
        "222H": ("maria",20),
        "333H": ("jaime", 21)
    }

    #### Matricular nuevos alumnos:
    nuevos_alumnos = {
        "444H": "luis",
        "555H": "silvia"
    }
    #### Antes de matricular a los alumnos:
    print (f"ANTES MAT: {alumnos}")
    alumnos = matricular_alumnos(curso=alumnos, **nuevos_alumnos) #Le estoy pasando el contenido. Le estoy pasando los pares de dentro del diccionario
    print(f"DESPUES MAT: {alumnos}")
    resultado = sumar(10,3)
    print(f"Resultado: {resultado}")

#### Método tradicional
#En este caso no he tenido que crear la función porque la importo desde "calculadora.py"
# def funcion_suma(num1,num2)
#     resultado = sumar(10,3)
#     print(f"Resultado: {resultado}")

#### Supongamos:
def calcular(x:int = 0, y: int = 0, z: int = 0) -> int:
    return x + y + z
 # => estoy definiendo una función de 3 parámetros pero estoy haciendo que el tercero sea opcional dándole un valor por defecto (= 0 en este caso), para permitir que se pasen sólo dos parámetros.
# **¡Siempre se ponen primero los obligatorios y luego los opcionales!**
resultado2 = calcular(1,5,7)
print(f"Resultado2: {resultado2}")

#Además, en principio, tengo que respetar el orden en que los defino.
#### ¿Se puede alterar el orden de la llamada?:
#Sí:
resultado2 = calcular (z=0,x=3,y=5)
print(resultado2)

resultado = sumar_v2(10,3,1,1,1,1,1,1,1,1,1)
print(f"Resultado_sumarv2:{resultado}")

valores_a_sumar = [2,5,2,8,0]
resultado = sumar_v2(*valores_a_sumar) #Rompo la lista para coger los valores de dentro. Así no tengo que saber con antelación la cantidad de valores que voy a pasarle

""" resultado = sumar_v3(10,3,1,1,1,1,1,1,1,1,1, otro_param=str='*') -> int:
    print(otro_param * 60)
    return sum(numeros)
    print(f"Resultado_sumarv2:{resultado}")
 """

