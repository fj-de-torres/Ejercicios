from os import system
from colorama import Style, Fore
system("cls || clear")
# mini = None
# maxi = None
def read_int(mini:int, maxi:int) -> int:
    try:
        numero = input(f"Ingresa un número entre el {mini}, y el {maxi}: ")
        numero = int(numero)
        if numero < mini or numero > maxi:
            raise OverflowError
        else:
            return numero
    except OverflowError:
        print(Style.BRIGHT + "Error de mierda:",Style.RESET_ALL + "el valor no está dentro del rango permitido")
        exit()

    except ValueError:
        print(Style.BRIGHT + 'Horror:', Style.RESET_ALL + 'entrada incorrecta')
        exit()
    except:
        print("WhateverError on line somewhere")

v = read_int(-10, 100)
if v % 5 == 0 and v % 10 !=0 :
    print(Style.BRIGHT + Fore.LIGHTRED_EX + f"{v}:",Style.NORMAL + "Por el culo te la hinco")
else:
    print(Fore.YELLOW + "El número es:",Style.BRIGHT + f"{v}")
