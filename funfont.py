from colorama import Fore, Back, Style
from prettytable import PrettyTable
column = PrettyTable()
def add_columna(string1,string2)->str:
    column.add_column(header(string1),[string2])
    print(column)
        

def funfont(string:str)->str:
    new_string=""
    for char in string:
        #new_string += chr(ord(char) + 65248)
        if char != " ":
            new_string += chr(ord(char) + 65248)
        else:
            new_string += " "
    
    return Fore.LIGHTGREEN_EX + new_string + Style.RESET_ALL

def header(string:str)->str:
    return Fore.YELLOW + string + Fore.WHITE

def linea(char:str = "⸺",times:int = 50):
    print(Fore.LIGHTMAGENTA_EX + "⸠" + char*times + "﹁" + Style.RESET_ALL)

def linea_gruesa(char:str = "➕",times:int = 50):
    print("➕"+"➖"*times+"➕")

if __name__ == "__main__":
    from os import system
    system("cls || clear")
    print(funfont("Usage:"))
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
    add_columna("Header","cell1")
    add_columna("segundo header","resultado2")
    column = PrettyTable()
    add_columna("segundo header","resultado2")
    print(column)