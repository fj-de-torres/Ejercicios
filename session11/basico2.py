class CuentaBancaria:
    def __init__(self,titular,saldo_inicial:float):
        self.__saldo = float(saldo_inicial)
        self.__titular = titular

    @property
    def titular(self) -> str:
        return self.__titular
    
    @property
    def saldo(self) -> float:
        return self.__saldo
    
    @saldo.setter
    def saldo(self,correccion_saldo:float):
        if correccion_saldo >= 0:
            self.__saldo = correccion_saldo


    def obtener_saldo(self):
        return self.__saldo

    def realizar_deposito(self,cantidad_a_ingresar: float):
        self.__saldo += cantidad_a_ingresar

    def realizar_retiro(self,cantidad_a_retirar:float):
        self.__saldo -= cantidad_a_retirar