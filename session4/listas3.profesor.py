#eliminar items

numeros = range(400)
print(type(numeros))
#print(list(numeros))


lista_numeros = [5,1,9]

""" for item in range(len(lista_numeros)):
    print(item)

for item in lista_numeros:
    print(item)
 """

def convertir_items_a_string(lista):
    lista_str = list()
    for numero in lista:
        lista_str.append(str(numero))
    
    return lista_str


rango_a_cadena = '-'.join(convertir_items_a_string(list(range(10))))
print(rango_a_cadena)

def eliminar_item(lista: list, item: int): #type hint
    #TODO: verificar los parameteros de entrada
    if item in lista:
        lista.remove(item)
        
    return lista

def eliminar_item_por_posicion(lista: list, pos: int):
    #pos = lista.index(item)
    if pos >= 0 and pos < len(lista):
    #if pos in range(len(lista)):
        del lista[pos]

    return lista

""" print(f"ANTES:{lista_numeros}")
lista_numeros = eliminar_item(lista_numeros, int(input("Item a borrar?:")))
print(f"DESPUES:{lista_numeros}") """

#print(f"ANTES:{lista_numeros}")
#lista_numeros = eliminar_item_por_posicion(lista_numeros, int(input("Pos item a borrar?:")))
#print(f"DESPUES:{lista_numeros}")


#item_borrado = lista_numeros.pop(0)
#print(item_borrado)


lista_numeros.sort(reverse=True)
print(lista_numeros)

lista1 = list(range(1,5))
lista2 = list(range(10,15))


lista_total = lista1 + lista2
print(lista_total)

lista1.extend(lista2)
print(f"LTOTAL:{lista1}")

#lista3 = lista2[:]
lista3 = lista2.copy()

matriz = [[1,2,3], [2,4,6], [6,4,1]]

print(matriz[0][-1])




