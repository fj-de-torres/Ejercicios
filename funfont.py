from colorama import Fore, Back, Style
def funfont(string:str)->str:
    new_string=""
    for char in string:
        #new_string += chr(ord(char) + 65248)
        if char != " ":
            new_string += chr(ord(char) + 65248)
        else:
            new_string += " "
    
    return Fore.LIGHTGREEN_EX + new_string + Style.RESET_ALL

if __name__ == "__main__":
    from os import system
    system("cls || clear")
    print(funfont(input("Escribe una frase a convertir (¡sin tildes!): ")))
