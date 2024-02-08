#𝒲𝑜𝓇𝓁𝒹 𝑜𝒻 𝒯𝓊𝓅𝓁𝑒𝓈:
import os
os.system("cls || clear")
from colorama import Fore, Back, Style
#Tupla: colección de datos que es INMUTABLE

tupla1 = (1,2,3)

#Perfecto para proteger dimensiones de datos

tupla2 = tupla1[:]

print(id(tupla1))
print(id(tupla2))
#Son iguales porque son valores de sólo lectura. No las puedo modificar, por eso no hace falta que se asignen posiciones de moria distintas
tupla3 = tupla2[0:2]
print(tupla3)
for item in tupla2:
    print(item)
tupla5 = 1,2,3,4,5
print(type(tupla5)) #¡No hacen falta nos paréntesis! Es decir, un return de más de un valor a la vez, es una tupla.
def procesar_data() -> tuple: # esto significa que estoy definiendo que sea una tupla su resultado
    return 1,2,3

n = 1, # tupla de una unidad
print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + str(type(n)))

lista_tuplas = [(1,2), (4,6),('Juan',9),(True,False)] #Lista de tuplas. También puedo tener una tupla de listas

print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + str(tupla5 [-1]))