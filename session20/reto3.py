# Accessing APIs:

import os
from sys import path
import requests
from colorama import Fore, Back, Style
where_am_i = os.path.dirname(__file__)
if 'Ejercicios' in where_am_i:
    while os.path.basename(os.getcwd()) != 'Ejercicios':
        os.chdir('..')

current_path = os.getcwd()
#current_directory = os.path.basename(current_path)
path.append(current_path)
os.chdir(where_am_i)
print(Fore.YELLOW + os.getcwd() + Fore.WHITE)

#exit()

#Profesor:
import json

with open(os.path.join(where_am_i,'nearby.json'), 'r') as file:
    data = json.load(file)


for clave, dict_anidado in data.items():
    print("\n" + clave+":\n")
    for clave2, valor2 in dict_anidado.items():
        print(Fore.MAGENTA + f"{clave2!r}: {valor2!r}" + Fore.WHITE) #La r final es para que los caracteres especiales no se tengan en cuenta.
print()
print(Fore.YELLOW + f"{5 + 5 = }")
print()