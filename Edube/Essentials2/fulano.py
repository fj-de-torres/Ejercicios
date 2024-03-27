import os
from sys import path
where_am_i = os.path.dirname(__file__)
if 'Ejercicios' in where_am_i:
    while os.path.basename(os.getcwd()) != 'Ejercicios':
        os.chdir('..')
current_path = os.getcwd()

#current_directory = os.path.basename(current_path)
path.append(current_path)
os.chdir(where_am_i)
from funfont import *
os.system("cls || clear")
"""Practicing errors"""
try:
    fulano = open("./Edube/Essentials2/timer.py",'rt',encoding="utf-8")
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
