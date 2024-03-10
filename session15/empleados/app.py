class Empleado:
    def __init__(self,id:int,nombre:str,salario:float):
        self.__id = id
        self.__nombre = nombre
        self.__salario = salario

@property
def id(self):
    return self.__id
@property
def nombre(self):
    return self.__nombre
@property
def salario(self):
    return self.__sarario

@property
def set_id(self,id):
    self.__id = id
@property
def set_nombre(self,nombre):
    self.__nombre = nombre
@property
def set_salario(self,salario):
    self.__salario = salario

class Programador(Empleado):
    def __init__(self, id: int, nombre: str, salario: float,lenguaje):
        super().__init__(id, nombre, salario)
        self.__lenguaje = lenguaje
    
    @property
    def lenguaje(self):
        return self.__lenguaje
    @property
    def set_lenguaje(self,lenguaje):
        self.__lenguaje = lenguaje
    