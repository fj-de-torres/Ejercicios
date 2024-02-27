""" from cliente import Cliente

class Cuenta:
#Es importante, en algunos casos, que algún atributo se autogenere:
    def __init__(self, numero_cuenta:str, saldo:str, propietario: Cliente) -> None:
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__propietario = propietario

def mostrar_informacion(self):
    return f"{self.__numero_cuenta} - {self.__saldo} - {self.__propietario}"
#self.__proietario ha de ser el resultado del método mágico __str__ del cliente
 """

from cliente import Cliente

class Cuenta:

    def __init__(self, numero_cuenta: str, saldo: float, propietario: Cliente) -> None:
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__propietario = propietario

    def mostrar_informacion(self):
        return f"{self.__numero_cuenta} - {self.__saldo} - {self.__propietario}"
