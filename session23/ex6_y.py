#𝕱𝖗𝖆𝖓𝖈𝖎𝖘𝖈𝖔 𝕵. 𝖉𝖊 𝕿𝖔𝖗𝖗𝖊𝖘

class LivingBeing:
    def __init__(self,name):
        self.__name = name

    def print_info(self):
        return f"{self.__name},"

class Persona(LivingBeing):

    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @name.setter
    def name(self,new_name):
        self.__name = new_name
    @age.setter
    def age(self,new_age):
        self.__age = new_age
    
    def __init__(self,name:str,age:str) -> None:
        self.__name = name
        self.__age = age
    
    def print_info(self):
        return " ".join(super().print_info(), self.age)

class Animal(LivingBeing):

    @property
    def name(self):
        return self.__name
    @property
    def species(self):
        return self.__species
    @name.setter
    def name(self,new_name):
        self.__name = new_name

    @species.setter
    def species(self,new_species):
        self.__species = new_species
    
    def __init__(self,name:str,species:str) -> None:
        self.__name = name
        self.__species = species
    
    def print_info(self):
        return " ".join(super().print_info(),self.species)
    

    pedro = Persona("Pedro","20")
    pedro.print_info()
