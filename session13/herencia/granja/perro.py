from animal import Animal
class Perro(Animal):
    
    def comer(self):
        return super().comer() + " Comer como un perro."