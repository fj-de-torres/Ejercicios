from cuenta import Cuenta
class Banco(Cuenta):

    @property
    def nombre_banco(self):
        return self.__nombre_banco

    @property
    def cuentas(self):
        return self._banco
    @property
    def cuenta(self):
        return self.__cuenta
    @property
    def detalle_cuentas(self):
        return self.__detalle_cuentas
    
    def __init__(self,nombre_banco:str,cuenta:str) -> None:
        self.__nombre_banco = nombre_banco
        self.__cuenta = super().__init__(cuenta,saldo,propietario)
        self.__cuentas = list()
        self.__detalle_cuentas = ()

    def agregar_cuenta(self,cuenta:Cuenta):
        self.__cuentas.append(cuenta)
    
    def mostrar_informacion(self):
        # for _ in self.__cuentas:
        #     self.__detalle_cuentas = tuple(Cuenta.mostrar_informacion(self.__cuenta))
        return self.__str__()

    def __str__(self) -> str:
        return f"Banco: {self.__nombre_banco}. Nº de cuentas asociadas: {len(self.__cuentas)}"

