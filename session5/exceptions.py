#How to handle exceptions:
import os
from colorama import Fore, Back, Style
os.system("cls || clear")
try:
    resultado = 14 / 0
except ZeroDivisionError: #Recogemos los errores desde el más particular (si los conocemos), al más general
    print (Fore.RED + "¡El divisor no puede ser cero!" + Style.RESET_ALL)
except Exception as ex:
    print(Fore.LIGHTRED_EX + "Ha habido un horror: "+ Style.RESET_ALL + Style.BRIGHT + f"{ex}")

try:
    resultado = 14 / "b"
except Exception as ex:
    print(Fore.LIGHTRED_EX + "Ha habido un horror: "+ Style.RESET_ALL + Style.BRIGHT + f"{ex}" + Style.RESET_ALL)

#Luego, podemos poner:
    
try:
    resultado = 14 / "b"
except TypeError as tex:
    print(Style.BRIGHT + f"{tex}")

#Puedo englobar las excepciones:
try:
    resultado = 14 / "b"
    print(resultado)
except (ZeroDivisionError, TypeError):
    print("El error es de tipo numerico")
