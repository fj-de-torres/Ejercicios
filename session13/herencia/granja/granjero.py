from animal import Animal

class Granjero():

    def __init__(self, animales: list[Animal]):
        self.__animales = animales

    def dar_de_comer(self):
        for animal in self.__animales:
            print(animal.comer())
