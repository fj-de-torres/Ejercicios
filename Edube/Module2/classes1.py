from os import system
system("cls || clear")
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__person_dict = {}

    def __str__(self):
        return "{"+f"\'name':{self.name},'age':{self.age}"+"}"
    
    def dicionary(self):
        self.__person_dict['name'] = self.name
        self.__person_dict['age'] = self.age
        return self.__person_dict
    
p2 = Person("Maite",25)
dict_p2 = p2.dicionary()
print(p2.name,p2.age,sep=",")
print(dict_p2)
print(type(dict_p2))
    
        