from animal import Animal
class Vaca(Animal):
    
    def comer(self):
        return super().comer() + " y rumiar."