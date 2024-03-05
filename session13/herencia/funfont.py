from colorama import Fore, Back, Style
from prettytable import PrettyTable
columna = PrettyTable()

def linea_gruesa(char:str = "➕",times:int = 50):
    print("➕"+"➖"*times+"➕")

def print_columna(string1,string2)->str:
    columna.add_column(header(string1),[string2])
    print(columna)
    linea_gruesa()
        

def funfont(string:str)->str:
    new_string=""
    for char in string:
        #new_string += chr(ord(char) + 65248)
        if char != " ":
            new_string += chr(ord(char) + 65248)
        elif char == " ":
            new_string += " "
    
    return Fore.LIGHTGREEN_EX + new_string + Style.RESET_ALL

def header(string:str)->str:
    return Fore.YELLOW + string + Fore.WHITE

def linea(char:str = "⸺",times:int = 50):
    print(Fore.LIGHTMAGENTA_EX + "⸠" + char*times + "﹁" + Style.RESET_ALL)


if __name__ == "__main__":
    from os import system
    system("cls || clear")
    print(funfont("Usage:"))
    #print(funfont("Take your power back!"))
    print("""
+------------------------------+-------------------------------+
| print(funfont("Hola")) gives | print(header("Header")) gives |
+------------------------------+-------------------------------+
|           Ｈｏｌａ           |            """,header("Header")+"""            |
+------------------------------+-------------------------------+""")
    print()
    print(funfont("linea(times=100):"))
    linea(times=100)
    linea_gruesa()
    print_columna("Header","cell1")
    print_columna("segundo header","resultado2")
    columna = PrettyTable()
    print_columna("segundo header","resultado2")
    print(columna)
    