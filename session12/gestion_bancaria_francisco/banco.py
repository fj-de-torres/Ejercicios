class Banco:

    @property
    def nombre_banco(self):
        return self.__nombre_banco

    @property
    def cuentas(self):
        return self._banco
    @property
    def cuenta(self):
        return self.__cuenta
    
    def __init__(self,nombre_banco:str,cuenta:str) -> None:
        self.__nombre_banco = nombre_banco
        self.__cuenta = cuenta
        self.__cuentas = list()

    def agregar_cuenta(self,cuenta:Cuenta):
        self.__cuentas.append(cuenta)
    
    def mostrar_informacion(self):
        pass

    def __str__(self) -> str:
        return f"Banco: {self.__nombre_banco}. Nº de cuentas asociadas: {len(self.__cuentas)}"

