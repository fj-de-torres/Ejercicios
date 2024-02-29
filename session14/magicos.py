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

    def __le__(self, estudiante: object):
        pass
    
    def __ge__(self,estudiante: object):
        pass
    
    def __ne__(self, estudiante: object) -> bool:
        pass   

juan = Student(40, 60, 20)
maria = Student(40, 60, 20)
system("cls || clear")
print_columna("print(juan == maria)",juan==maria)

juan = Student(40, 60, 20)
maria = Student(40, 30, 20)
system("cls || clear")
print_columna("print(juan == maria)",juan==maria)

    