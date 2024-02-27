class Cuenta:

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def propietario(self):
        return self.__propietario
    
    def __init__(self,numero_cuenta:str ,saldo:str ,propietario:str):
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__propietario = propietario

    def __str__(self) -> str:
        return f"Número de cuenta: {self.__numero_cuenta}, Saldo: {self.__saldo}. {self.__propietario}. "