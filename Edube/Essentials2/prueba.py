import os
from colorama import Fore, Back, Style
def clear():
    os.system("cls || clear")
clear()
where_am_i = os.path.dirname(__file__)
if 'Ejercicios' in where_am_i:
    while os.path.basename(os.getcwd()) != 'Ejercicios':
        print(os.getcwd().count('/'))
        os.chdir('..')
path = os.getcwd()

print(Fore.YELLOW + path + Fore.WHITE)
