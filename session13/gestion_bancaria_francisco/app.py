from os import system
from cliente import Cliente
from banco import Banco
from cuenta import Cuenta

system("cls || clear")

def linea(charac:str = "-",times: int = 80):
    print(charac*times)

#-------------------------------------------------------------------------------
if __name__ == "__main__":

    juan = Cliente('Juan López', '111A')
    cuenta_juan = Cuenta('1','25_000',juan.nombre)
    linea("-",80)
    print(juan)
    print(cuenta_juan)
    cuenta_juan.mostrar_informacion()
    linea()
    pedro = Cliente('Pedro Ramírez', '2222B')
    print(pedro)
    cuenta_pedro = Cuenta('2','50_000',pedro.nombre)
    print(cuenta_pedro)
    cuenta_pedro.mostrar_informacion()
    linea()
    banco_trinidad = Banco("Banco Trinidad",cuenta_juan)
    linea()
    print(banco_trinidad)
    banco_trinidad.agregar_cuenta(cuenta_juan)
    linea()
    print(banco_trinidad)
    linea()
    print(banco_trinidad.mostrar_informacion())
    linea()
    print(banco_trinidad)