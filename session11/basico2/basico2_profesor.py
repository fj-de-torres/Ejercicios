from cuenta_bancaria import Cuenta_Bancaria
from os import system
system("cls || clear")
if __name__== "__main__":

    try:
        cuenta = Cuenta_Bancaria(400.0,'Juan Palomo')
        cuenta.realizar_deposito(100.0)
        print("Saldo actual tras el ingreso de 100€ es:",cuenta.obtener_saldo(),"€")

        cuenta.realizar_retiro(300.0)

        print("Saldo actual es de", cuenta.obtener_saldo(),"€")

        cuenta.realizar_retiro(500.0)

    except Exception as ex:
        print(ex)
    finally:
        print("Operación realizada")