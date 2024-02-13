# Listas:
## Comprehension List (listas de comprensión)
import os
os.system("cls || clear")
lista = list()
lista2 = [1,2,3,4]

numeros_20 = list(range(20))

#Código Miguel:
def cuadrado(num: int) -> int:
    return num ** 2
#### Ejemplo de una comprehension list:

numeros_20_actualizado = [numero * 2 for numero in numeros_20]
print(numeros_20)
print(numeros_20_actualizado)
elevar_cuadrado = lambda numero : numero ** 2 # podría haber usado otra palabra en vez de numero.


numeros_20_actualizado_v2 = [elevar_cuadrado(numero) for numero in numeros_20]
print(numeros_20_actualizado_v2)
numeros_20_actualizado_v3 = [(lambda n : n ** 2) (numero) for numero in numeros_20] #No es lo aconsejable, aunque técnicamente viable.
print(numeros_20_actualizado_v3)

#### Procesar, de numeros_20, sólo los impares:
es_impar = lambda n: n%2 != 0
numeros_20_impares  = [numero -1 for numero in numeros_20 if numero % 2 != 0] #=> numero -1 es simplemente un cálculo que he querido hacer, no tiene nada que ver con el cálculo sobre los impares, que es otra cosa que se pretende aquí. (De un compañero:*con el "numero - 1"  los convierte en par , si un poco confuso que ponga impares y salgan pares :)*)
numeros_20_impares_v2 = [numero -1 for numero in numeros_20 if es_impar(numero)]

print(numeros_20_impares)
print(numeros_20_impares_v2)

numeros_20_cerocinco = list(map(lambda n : n + 0.5 , numeros_20))
print(numeros_20_cerocinco)
#print(numeros_20_impares)

print([numero for numero in map(lambda n : n + 0.5 , numeros_20)])

#### Dada una lista de alumnas, obtener una NUEVA lista conteniendo solo las alumnas que han obtenido 7 ó más. Usando *comprehension lists*
os.system ("cls || clear")
alumnas = [('Maria de la O', 9.5),('La Jenny', 7.5),('Mari Puri',5),('Mengana', 4.9)]

alumnas_aventajadas = [ (nombre,notas) for nombre , notas in alumnas if notas >= 7]
print(alumnas_aventajadas)

##### Solución del profesor:
aventajadas = [alumna for alumna in alumnas if alumna[1] > 7.0]
print(aventajadas)

## ¿Habrá comprehension sets *(or what the Hell)*?

conjunto = {numero for numero in [1,2,3,4,5,6,7,7,7,7]}
#Hemos creado, dinámicamente, una estructura partiendo de otra. Otro ejemplo sería crear dinámicamente un dicionario:

##### Diccionarios:

diccionario_alumnas = {alumna[0]:alumna[1] for alumna in alumnas } #*(Or how to understand girl students)*

print(diccionario_alumnas)

###### Tuplas:

alumans_nota_tupla = (nota for nombre, nota in alumnas) #nos ha salido un *generador*

alumnas_nota_tupla_v2 = tuple( [nota for nombre, nota in alumnas]) #Esto sí que es una tupla.