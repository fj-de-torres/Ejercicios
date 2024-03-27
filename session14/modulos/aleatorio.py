import os
import random as rd
import math
from sys import path
where_am_i = os.path.dirname(__file__)
if 'Ejercicios' in where_am_i:
    while os.path.basename(os.getcwd()) != 'Ejercicios':
        os.chdir('..')
current_path = os.getcwd()

#current_directory = os.path.basename(current_path)
path.append(current_path)
os.chdir(where_am_i)
from funfont import *
from colorama import Fore,Back, Style

# print(Fore.BLACK + Style.BRIGHT + Back.GREEN + "¡Hola!" + Style.RESET_ALL)

# print(funfont("¡Pasen y vean!"))

print(math.floor((rd.random() * 10)))

print(rd.randint(5, 10))

#Escoger aleatoriamente de entre los elementos de una lista:

saludos = ['hola', 'adios', 'hasta luego', 'a tomar por c***']
print(rd.choice(saludos))

print(rd.sample(saludos,2))

#Desordena la lista. Si luego voy cogiendo el primer elemento de la lista con el nuevo orden, es como iterrar por ella:

rd.shuffle(saludos)
print(funfont(saludos[0]))

linea_gruesa(times=57)
print(funfont("Hola"))
