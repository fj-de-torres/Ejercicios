#from cliente import Cliente
class SaldoNegativoException(Exception):
    pass
class NumeroCuentaExistenteError(Exception):
    pass
    
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
        try:
            if int(saldo) >= 0:
                self.__saldo = saldo
            else:
                raise SaldoNegativoException("¡No se admite un saldo negativo!")
            
        except SaldoNegativoException as nex:
            print(nex)
        self.__propietario = propietario
        self.__numero_cuenta = numero_cuenta

    def __str__(self) -> str:
        return f"Número de cuenta: {self.__numero_cuenta}, Saldo: {self.__saldo}. {self.__propietario}. "
    
    def mostrar_informacion(self):
        print(self.__str__())
        return (self.__numero_cuenta, self.__saldo, self.__propietario)