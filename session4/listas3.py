from colorama import Fore, Back, Style
import os
os.system("cls || clear")
""" #Eliminando elementos de una lista:

numeros = range(1,400,4)  # Creación de números del 1 al 400 cogidos de 4 en 4
numeros2 = range(400)
print(type(numeros))

# Pero para ver el contenido:
print (list(numeros))
print (list(numeros2)) """

#Y se puede usar para recorrer un for:
lista_numeros = [1,5,9] 
"""
for item in range(len(lista)):
    print(item)
 for item in range(10):
    print(item)

def convertir_items_a_string(lista):
    lista_str = list()
    for numero in lista:
        lista_str.append(str(numero))
    return lista_str """

""" rango_a_cadena = '*'.join(convertir_items_a_string((list(numeros))))
print(rango_a_cadena) """

def eliminar_item(lista:list,pos: int): #'Type hint': De esta manera estoy definiendo qué tipo de elemento es. Pero puedo instertar un dato de tipo diferente y no dará error. Pero puede tener consecuencias en el código.
    #TODO: verificar los parámetros de entrada
    #if iter in lista:
        #lista.remove(item)
        #Por posición:
        #pos = lista.index(item) # Pero... ¿y si no existe el elento?
        #if pos >= 0 and pos < len(lista)
    if pos in range(len(lista)):
        del lista[pos]
        print(Fore.GREEN + "Mission possible!"+ Style.RESET_ALL)

    else:
        print(Fore.RED + "Mission: " + Style.BRIGHT + "Impossible"+ Style.RESET_ALL)
    return lista # aunque no haría falta aquí porque estar trabajando con una variable local (y lista y lista_numeros apuntan a la misma dirección de memoria).
""" 
print(f"ANTES: {lista_numeros}")
lista_numeros = eliminar_item(lista_numeros, int(input("Ítem a borrar: ")))
print(f"DESPUES: {lista_numeros}")
 """

print(f"ANTES: {lista_numeros}")
lista_numeros = eliminar_item(lista_numeros, int(input("Pos ítem a borrar: ")))
print(f"DESPUES: {lista_numeros}")

#Método que elimina el último número:
#item_borrado = lista_numeros.pop() # me borra el último nº y me lo entrega como salida a ese método
#print(f"Ítem borrado: {item_borrado}")
#enensimo_item_borrado = lista_numeros.pop(1) # Puedo elegir qué ítem quiero borrar; no necesariamente la última.
print(lista_numeros.sort()) #Da None
lista_numeros.sort(reverse=True) #Ahora sí, y hemos elegido que sea en orden inverso:
print(lista_numeros)
lista1 = list(range(1,5))
lista2 = list(range(10,15))
lista_total = lista1 + lista2

print(lista_total)

lista3 = lista1 *3 #[1,2,1,2,1,2]
#También se puede hacer así:
lista_total2 = lista1.extend(lista2) #Devuelve un None. Para añadirla a la anterior, se hace como con .pop():
lista1.extend(lista2)
print(lista_total)

#lista3 = lista2[:]

lista3 = lista2.copy() # Es un método que también clona, como en el caso anterior.

#Se pueden hacer listas de varias dimensiones: 𝙢𝙖𝙩𝙧𝙞𝙘𝙚𝙨 -> listas de listas
matriz = [[1,2,3], [4,5,6], [6,4,1]]

print(matriz[0][-1])

matriz3d = [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]
print (matriz3d [1][1][1])

#Una lista de tuplas también es una matriz, pero no puedo modificar los elementos. Es decir, puedo modificar el contenedor pero no el contenido.