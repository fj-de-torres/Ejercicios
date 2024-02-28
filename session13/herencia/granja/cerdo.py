from animal import Animal
class Cerdo(Animal):
    
    def comer(self):
        return super().comer() + " Comer como un cerdo."