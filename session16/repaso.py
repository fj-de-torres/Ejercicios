from colorama import Fore, Back, Style
from os import system
def func_a():
    dividendo = input("Ingrese el dividendo: "+ Style.BRIGHT)
    divisor = input(Style.NORMAL + "Ingrese el divisor: " + Style.BRIGHT)
    resultado = func_b(float(dividendo),float(divisor))
    print(Style.NORMAL + Fore.LIGHTBLUE_EX + f"El resultado de dividir {dividendo} entre {divisor} es: " + Fore.WHITE +  f"{resultado}")
    print(Fore.GREEN + "-"*100 + Fore.WHITE)

def func_b(dividendo:float,divisor:float) ->float: #Funciones que llaman a fuciones (HOF). Aquí añadiríamos otra funcionalidad a la función c.
    return func_c(dividendo,divisor)

def func_c(dividendo:float, divisor:float) -> float:
    return dividendo / divisor

if __name__ == "__main__":
    system("cls || clear")
    continuar = True
    while continuar:
        try:
            func_a()
            continuar = input("Desea continuar? (s/n): ").lower() == "s"
        except ZeroDivisionError as zex:
            print(Fore.RED + f"{zex}".capitalize() + ", mother fucker!!" + Fore.WHITE)
            continuar = False
        except ValueError as vex:
            print(vex)
            continuar = False
        else:
            pass
        finally:
            if continuar:
                print(Style.BRIGHT + "Iteramos sobre la operacion" + Style.RESET_ALL)
            else:
                print("_"*100)
                print()
                print(Fore.YELLOW + "Gracias por usar esta calculadora" + Fore.WHITE)