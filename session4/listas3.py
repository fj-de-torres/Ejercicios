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
item_borrado = lista_numeros.pop() # me borra el último nº y me lo entrega como salida a ese método
print(f"Ítem borrado: {item_borrado}")
enensimo_item_borrado = lista_numeros.pop(1) # Puedo elegir qué ítem quiero borrar; no necesariamente la última.