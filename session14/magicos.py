from funfont import *
from os import system

class Student:

    @property
    def grades(self):
        return self.__math + self.__history + self.__writing

    def __init__(self, math:int, history:int, writing:int):
        self.__math = math
        self.__history = history
        self.__writing = writing
    
    def __eq__(self, estudiante: object) -> bool:
        return self.grades == estudiante.grades
    
    def __gt__(self, estudiante: object):
        pass
    
    def __lt__(self, estudiante: object):
        pass
    
    def __le__(self, estudiante: object):
        pass
    
    def __ge__(self, estudiante: object):
        pass

    def __ne__(self, estudiante: object) -> bool:
        pass
    


    

juan = Student(40, 60, 20)
maria = Student(40, 60, 20)

print(juan == maria)


#from dataclasses import dataclass
import dataclasses

@dataclasses.dataclass
class Coche:
    matricula: str


class Parking:
    
    @property
    def coches(self):
        return self.__coches

    @coches.setter
    def coches(self, lista_coches):
        self.__coches = lista_coches

    def __init__(self) -> None:
        self.__coches = None

    def __setitem__(self, pos, item):
        self.__coches[pos] = item

    def __getitem__(self, pos):
        return self.__coches[pos]


parking_saba = Parking()
parking_saba.coches = [Coche('A12'),Coche('A13'),Coche('A14')]

# print(parking_saba[0])
# parking_saba[0] = Coche('B50')
# print(parking_saba[0])


for coche in parking_saba:
    print(coche)
