# Accessing APIs:

import os
import requests
from colorama import Fore, Back, Style

""" with open("/home/francisco/Documents/Learning/PUE/Python/Ejercicios/session20/nearby.json", "rt") as jason:
    diccionario = jason.read()

#print(diccionario)
for address in diccionario.keys():
    print(address) """


#Profesor:
import json

with open('/home/francisco/Documents/Learning/PUE/Python/Ejercicios/session20/nearby.json', 'r') as file:
    data = json.load(file)


for clave, dict_anidado in data.items():
    print("\n" + clave+":\n")
    for clave2, valor2 in dict_anidado.items():
        print(Fore.MAGENTA + f"{clave2!r}: {valor2!r}" + Fore.WHITE) #La r final es para que los caracteres especiales no se tengan en cuenta.
print()
print(Fore.YELLOW + f"{5 + 5 = }")
print()