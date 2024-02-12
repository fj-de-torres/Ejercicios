#How to handle exceptions:
import os
from colorama import Fore, Back, Style
os.system("cls || clear")

diccionario  = dict(a=1, b=2)

try:
    resultado = 14 / 0
except ZeroDivisionError: #Recogemos los errores desde el más particular (si los conocemos), al más general
    print (Fore.RED + "¡El divisor no puede ser cero!" + Style.RESET_ALL)
except Exception as ex:
    print(Fore.LIGHTRED_EX + "Ha habido un horror:😱 "+ Style.RESET_ALL + Style.BRIGHT + f"{ex}")

try:
    resultado = 14 / "b"
except Exception as ex:
    print(Fore.LIGHTRED_EX + "Ha habido un horror:😱 "+ Style.RESET_ALL + Style.BRIGHT + f"{ex}" + Style.RESET_ALL)

#Luego, podemos poner:
    
try:
    resultado = 14 / "b"
except TypeError as tex:
    print(Style.BRIGHT + f"{tex}")

#Puedo englobar las excepciones:
try:
    resultado = 14 / "b"
    print(resultado)
except (ZeroDivisionError, TypeError): #OjO: han de estar entre paréntesis
    print("El error es de tipo numerico")

try:
    #resultado = 14 / 0
    #print(resultado)
    data = diccionario["c"]

except (ZeroDivisionError, TypeError):
    print("El error es de tipo numerico")
except Exception as ex:
    print(f"Ha habido un error: {ex}")

try:
    #resultado = 14 / 0
    #print(resultado)
    data = diccionario["c"]

except (ZeroDivisionError, TypeError):
    print("El error es de tipo numerico")
except KeyError as kex:
    print(f"Clave inexistente:{kex}")
except Exception as ex:
    print(f"Ha habido un error: {ex}")

# def convertir_a_entero(data:str) -> int:
#     # try:
#         return int(data)
#     # except:
# resultado_entero = convertir_a_entero("p")
# print(resultado_entero)
# #Mirando el error arrojado lo añado a except:

def convertir_a_entero(data:str) -> int:
    resultado = None
    try:
        return int(data)
    except ValueError: #Capturo la excepción y así no peta el programa. Me devolverá None y ya sé que ha habido un error
        pass #No hace nada en caso de error porque ya he asignado por defecto el valor None si hay error
    return resultado

resultado_entero = convertir_a_entero("P")
#print(resultado_entero)
print(resultado_entero if resultado_entero else "Problema al convertir 😤")

diccionario = {
    "111H": "Juan",
    "222H": "Paloma"
}

try:
    del diccionario
    diccionario["111H"] = "Miguel"
except Exception:
    print("Buah 😤")

#diccionario["111H"] = "Miguel" Sólo lo hacemos para capturar el error. Una vez capturado:
    
try:
    diccionario["111H"] = "Miguel"
except NameError:
    print("Ese diccionario no existe 😤")
except Exception:
    print ("Error general")
else:
    print("Se ha completado satisfactoriammente la operación") #Esto sólo se ejecuta si el try no dio error.
    #Esto podría ser últil cada vez que modifiquemos una base de datos, pues es importante saber si las transacciones se completan (por citar un ejemplo).
finally:
    print("Operación terminada") #Esto se ejecuta tanto cuando hay error como cuando no (try que funcione)