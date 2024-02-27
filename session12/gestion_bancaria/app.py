from os import system
system("cls || clear")

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

class Cuenta:

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    # def propietario(self):
        
    def __init__(self,numero_cuenta:str ,saldo:str ,propietario:str):
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__propietario = propietario

    def __str__(self) -> str:
        return f"Número de cuenta: {self.__numero_cuenta}, Saldo: {self.__saldo}. Propietario: {Cliente.nombre}, DNI: {Cliente.dni}"
    
juan = Cliente('Juan López', '111A')
pedro = Cliente('Pedro Ramírez', '2222B')
def linea(charac:str = "-",times: int = 20):
    print(charac*times)

print(juan)
linea()
print(pedro)

cuenta_juan = Cuenta('1','25_000',juan.nombre)