import os
from colorama import Fore, Back, Style
def clear():
    os.system("cls || clear")

where_am_i = os.path.dirname(__file__)
if 'Ejercicios' in where_am_i:
    while os.path.basename(os.getcwd()) != 'Ejercicios':
        os.chdir('..')
path = os.getcwd()
clear()
print(Fore.YELLOW + path + Fore.WHITE)
