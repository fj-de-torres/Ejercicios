from colorama import Fore, Back, Style
def funfont(*string:str)->str:
    new_string=""
    for char in string:
        if char.isalnum():
            new_string += chr(ord(char) + 65216)
        elif char == " ":
            new_string += " "
    return new_string

print(funfont("Tu"))
