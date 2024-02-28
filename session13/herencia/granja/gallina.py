from animal import Animal
class Gallina(Animal):
    
    def comer(self):
        return super().comer() + " y picotear."
    
#Hay una parte común en el método comer que se hereda de la clase animal, y otra que se especifica en cada clase hija.