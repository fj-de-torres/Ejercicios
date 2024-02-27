# Clase Cuenta_Bancaria:

```
class Cuenta_Bancaria:
    #getters
    @property
    def titular(self):
        return self.__titular

    def __init__(self, saldo: float, titular: str) -> None:
        self.__saldo = saldo
        self._titulsar = titular
```
Estas son las responsabilidades de la clase:
```
    def obtener_saldo(self) -> float:
        return self.__saldo
    
    def realizar_deposito(self, cantidad: float):
        self.__saldo += cantidad
    
    def realizar_retiro(self, cantidad: float):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            raise Exception("No hay saldo suficiente")
```
