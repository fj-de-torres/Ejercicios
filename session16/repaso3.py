"""
Repasar aspectos relevantes de POO
"""
from os import system
from colorama import Fore,Back,Style

class Zoo():
    """Clase que representa un zoológico"""
    def __init__(self) -> None:
        self.animals = []
    
    def add_animals(self,*animals):
        for animal in animals:
            self.animals.append()

    def __repre__(self) -> str:
        return self.animals
    
    def animals_by_color(self,color:str):
        """Retorna una lista con los animales del color especificado"""
        color_list = []
        for animal in self.animals:
            if animal.value() == color:
                color_list.append(animal)
        return color_list
    
    def animals_by_legs(self,legs:int):
        """Retorna una lista con los animales con la cantidad de patas especificada"""
        legs_list = []
        for animal in self.animals:
            if animal.values() == legs:
                legs_list.append(animal)
        return legs_list
    
    def num_of_legs(self):
        """Retorna la cantidad total de patas en el zoológico"""
        pass

class Animal(Zoo):
    def __init__(self,nombre:str,color:str,patas:int) -> None:
        self.diccio_animal = {}
        """Diccionario de animal como: 
        {
            "nombre":"nombre_animal:str",
            "color":"color_animal:str",
            "patas":"numero_patas:int"
            
            }"""
        self.diccio_animal[self.nombre]= nombre
        self.diccio_animal[self.color] = color
        self.diccio_animal[self.patas] = patas
        super().__init__().append(self.diccio_animal)
        
    if __name__ == "__main":
        pass