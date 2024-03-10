import os
import requests
class Empleado:

    @property
    def id(self):
        return self.__id
    @property
    def nombre(self):
        return self.__nombre
    @property
    def salario(self):
        return self.__salario

    @property
    def set_id(self,id):
        self.__id = id
    @property
    def set_nombre(self,nombre):
        self.__nombre = nombre
    @property
    def set_salario(self,salario):
        self.__salario = salario

    def __init__(self,id:int,nombre:str,salario:float):
        self.__id = id
        self.__nombre = nombre
        self.__salario = salario

    def __str__(self):
        return f"id: {self.id}, Nombre: {self.nombre}, Salario: {self.salario}"
    
    def __repr__(self) -> str:
        return f"<Empleado> - {self.id} - {self.nombre} - {self.salario}"
    

class Programador(Empleado):

    @property
    def lenguaje(self):
        return self.__lenguaje
    @property
    def set_lenguaje(self,lenguaje):
        self.__lenguaje = lenguaje

    def __init__(self, id: int, nombre: str, salario: float,lenguaje):
        super().__init__(id, nombre, salario)
        self.__lenguaje = lenguaje
    
    def __str__(self) -> str:
        return super().__str__() + f", Lenguaje: {self.lenguaje}"
    
    def __repr__(self) -> str:
        return super().__repr__() + f" - {self.lenguaje}"

if __name__ == "__main__":
    os.system("cls || clear")
    fulano = Programador(1,"Fulano",50_000,"Java")
    print(fulano)
    print(repr(fulano))
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    data = response.json()
    head = ['id' , 'name','username' , 'email' , 'website']
    print(data[0])
    ruta_directorio = os.path.dirname(__file__)
    subdir_path = os.path.join(ruta_directorio, 'data')
    try:
        if not os.path.exists(subdir_path):
    # If it does not exist, create it
            os.makedirs(subdir_path)
    except :
        