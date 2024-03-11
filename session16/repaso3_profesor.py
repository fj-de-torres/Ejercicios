"""
Repasa raspectos relevantes de POO
"""

from animal import Snake, Spider, Wolf

def mostrar_animales(animals):
    """Muestra los animales"""
    for animal in animals:
        print(animal)

class Zoo():
    """Clase que representa un zoológico"""
    def __init__(self) -> None:
        self.animals = []
    
    
    def add_animals(self, *animals):
        """Agrega animales al zoológico"""
        for animal in animals:
            self.animals.append(animal)

    def __repr__(self) -> str:
        """Retorna una representación del zoológico"""
        return '\n'.join(str(animal) for animal in self.animals)    

    def animals_by_color(self, color: str):
        """Retorna una lista con los animales del color especificado"""
        return [animal for animal in self.animals if animal.color == color]

    def animals_by_legs(self, legs: int):
        """Retorna una lista con los animales con la cantidad de patas especificada"""
        #return [animal for animal in self.animals if animal.legs == legs]
        return list(filter(lambda animal: animal.legs == legs, self.animals))
    

    def num_of_legs(self):
        """Retorna la cantidad total de patas en el zoológico"""
        return sum(animal.legs for animal in self.animals)
    

if __name__ == "__main__":
    zoo = Zoo()
    zoo.add_animals(
        Wolf("Lobo", "Gris"),
        Spider("Araña", "Negra"),
        Snake("Serpiente", "Verde"))
    
    print(zoo)
    print("_" * 40)
    print("Animales de color gris:\n")
    mostrar_animales(zoo.animals_by_color("Gris"))
    print("_" * 40)
    print(f"Animales de 8 patas:\n")
    mostrar_animales(zoo.animals_by_legs(8))
    print("_" * 40)
    print("Patas en total del zoo:", zoo.num_of_legs()) #12