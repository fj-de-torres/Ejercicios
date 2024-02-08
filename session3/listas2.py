import os
os.system("cls || clear")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if len(numeros) != 0: #no vacia
    pass # equivale a poner ...

numeros[-1] = 8

print(numeros)

# ¿Cuántos 8 hay?
print(f"Hay: {numeros.count(8)} 8s")
print (numeros[:3])

# numeros [0:2] = 0  => Error. No lo permite

tramo = numeros[0:2]
print(tramo, type(tramo))

#Una manera de 𝗖𝗟𝗢𝗡𝗔𝗥 una lista:
numeros_clonados = numeros[:]
print(numeros_clonados)
print(id(numeros_clonados))
print(id(numeros)) # Hemos clonado. Son elementos diferentes. Lo que haga a uno no repercute en el otro.

numerosv2 = numeros
numeros [0:2] = 20, 40 #Esto sí funciona como sustitución de elementos en una lista.
print(id(numerosv2))
print(id(numeros))
print(numeros,numerosv2, numeros_clonados)