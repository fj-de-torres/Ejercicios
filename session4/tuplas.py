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

print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + str(tupla5 [-1])+ Style.RESET_ALL)


t1, t2, t3, t4 = lista_tuplas #Si desempacamos todo, es todo. O sea, hay que incluir hasta t4
print(t1,t2,t3,t4,sep ="---")
#Para muchas más que desempacar:
t1, *_ = lista_tuplas #Sólo quiero el primero. *_ es un agujero negro al que van el resto y no me dará error
t1, *resto = lista_tuplas #Sí sale el resto. Pero todos dentro de una lista.
#Cogiendo otros de dentro:

_,t2, _,_ = lista_tuplas


#Convertir una lista en una tupla:

print(list((2,5,8)))
# print(lista) #Ya es tupla
# print(type(lista))
tupla = tuple([1,2,3,4])
print(tupla)
print(type(tupla))

