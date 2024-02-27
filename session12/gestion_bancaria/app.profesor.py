from cuenta import Cuenta
from cliente import Cliente
from banco import Banco

if __name__ == "__main__":


    cliente1 = Cliente("Luis", "111H")
    cliente2 = Cliente("Alicia", "222H")

    
    cuenta1 = Cuenta("A1", 900.0, cliente1)
    cuenta2 = Cuenta("A2", 650.0, cliente2)

    banco = Banco("Banco Mediolanum")
    banco.agregar_cuenta(cuenta1)
    banco.agregar_cuenta(cuenta2)

    for cuenta in banco.cuentas:
        print(cuenta.mostrar_informacion())
