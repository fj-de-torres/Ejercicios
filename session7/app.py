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
