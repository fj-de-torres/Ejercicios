## Clase Persona
from os import system
system("cls || clear")


class Persona:
    def __init__(self,nombre:str, edad:int) -> tuple:
        self.__nombre = nombre
        self.__edad = edad
    
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"
    
    def __str__(self,*personas) -> str:
        nombre = None
        edad = 0
        for nombre, edad in personas:
            nombre += personas + " "
            edad += edad
        return nombre,edad
    
juan = Persona('Juan',23)
pedro = Persona('Pedro',25)

print(juan)
print(pedro)
