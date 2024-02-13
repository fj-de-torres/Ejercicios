# Listas:
## Comprehension List (listas de comprensión)

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
numeros_20_impares  = [numero -1 for numero in numeros_20 if numero % 2 != 0] #=> numero -1 es simplemente un cálculo que he querido hacer, no tiene nada que ver con el cálculo sobre los impares, que es otra cosa que se pretende aquí.
numeros_20_impares_v2 = [numero -1 for numero in numeros_20 if es_impar(numero)]

print(numeros_20_impares)
print(numeros_20_impares_v2)

numeros_20_cerocinco = list(map(lambda n : n + 0.5 , numeros_20))
print(numeros_20_cerocinco)
#print(numeros_20_impares)

print([numero for numero in map(lambda n : n + 0.5 , numeros_20)])