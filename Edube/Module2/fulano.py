from os import system
from sys import path
path.append("/home/francisco/Documents/Learning/PUE/Python/Ejercicios/")
from funfont import *
system("cls || clear")
try:
    fulano = open("./Edube/Module2/timer.py",'rt',encoding="utf-8")
    print(header(fulano.read()))
    fulano.close()
except IOError as exc:
    print("Vaya mierda:",end=" ")
    print(Fore.LIGHTMAGENTA_EX +f"{exc}" + Fore.WHITE)
    #print("Error nº",exc.errno)
except Exception as exc:
    print("Fulano no está ni se le espera")
else:
    print()
    print(funfont("Fulano se despide"))
finally:
    print()
    print(Style.BRIGHT + header("¡Nunca olvides a Mengano!") + Style.RESET_ALL)
