#listas
#comprehension list

lista = list()
lista2 = [1,2,3,4]

#numeros_20 = list(range(20))
numeros_20 = range(20)

def cuadrado(num: int) -> int:
    return num ** 2

numeros_20_actualizado = [cuadrado(numero) for numero in numeros_20]
#print(numeros_20)
#print(numeros_20_actualizado)

elevar_cuadrado = lambda numero : numero ** 2

numeros_20_actualizado_v2 = [elevar_cuadrado(numero) for numero in numeros_20]
#numeros_20_actualizado_v2 = [(lambda n : n ** 2)(numero) for numero in numeros_20]
print(numeros_20_actualizado_v2)

es_impar = lambda n: n % 2 != 0

#procesar, de numeros_20, solo los impares
numeros_20_impares = [numero - 1 for numero in numeros_20 if numero % 2 != 0]
#[numero - 1 for numero in numeros_20 if es_impar(numero)]

numeros_20_cerocinco = list(map(lambda n : n + 0.5 , numeros_20))
print(numeros_20_cerocinco)
#print(numeros_20_impares)

print([numero for numero in map(lambda n : n + 0.5 , numeros_20)])


#dada una lista de alumnos, obtener una NUEVA lista conteniendo solo los alumnos que han obtenido 7 o mas
# usando comprehension list
alumnos = [('Maria', 6.5), ('Jaime', 7.5)]

alumnos_aprobados = [alumno for alumno in alumnos if alumno[1] > 7.0]
print(alumnos_aprobados)

#conjuntos
conjunto = {numero for numero in [1,2,3,4,5,6,7,7,7,7,7,7]}
print(conjunto)

#diccionarios
alumnos_diccionario = {nombre:nota for nombre, nota in alumnos if nota > 6.5}
print(alumnos_diccionario)

#tuplas
alumnos_nota_tupla = tuple([nota for nombre, nota in alumnos])
print(alumnos_nota_tupla)







