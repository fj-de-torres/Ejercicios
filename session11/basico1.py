from os import system
from colorama import Fore, Style, Back
system("cls || clear")
class Persona:
    def __init__(self,nombre:str,edad:int):
        self.__nombre = nombre
        self.__edad = edad

    def saludar(self):
        print(Fore.YELLOW + "="*20)
        print("|" + " " * 18 +"|")
        print("|" + Fore.WHITE + f"¡Hola {self.__nombre}!".center(18," ")+ Fore.YELLOW + "|")
        print(Fore.YELLOW + "|" + " " * 18 +"|")
        print("="*20)

p1 = Persona("Pedro", 45)
p2 = Persona("Pablo", 53)

p1.saludar()
p2.saludar()

cadena1 = """
====================
|                  |
|   ¡Hola Pedro!   |
|                  |
====================
"""
cadena2 = """
====================
|                  |
|   ¡Hola Pedro!   |
|                  |
====================
"""
#print (cadena1 + cadena2)