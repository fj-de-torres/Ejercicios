class Cliente:
    @property
    def nombre(self):
        return self.__nombre
    @property
    def dni(self):
        return self.__dni   

    def __init__(self,nombre:str,dni:str):
        self.__nombre = nombre
        self.__dni = dni

    def __str__(self):
        return f"Nombre: {self.__nombre}, DNI: {self.__dni}"