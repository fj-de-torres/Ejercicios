import random as rd
import math

print(math.floor((rd.random() * 10)))

print(rd.randint(5, 10))

#Escoger aleatoriamente de entre los elementos de una lista:

saludos = ['hola', 'adios', 'hasta luego', 'a tomar por c***']
print(rd.choice(saludos))

print(rd.sample(saludos,2))

#Desordena la lista. Si luego voy cogiendo el primer elemento de la lista con el nuevo orden, es como iterrar por ella:

rd.shuffle(saludos)
print(saludos[0])
