#Este es el nombre que, habitualmente, recibe el módulo principal
from colorama import Fore, Back, Style
if __name__ == "__main__":
    print("Programa principal en ejecución")

"""
- Las variables no pueden empezar con números.
- No pueden empezar con símbolos especiales.
- Lower snake case:

nombre_y_apellido = "Juan López"

Se le llama snake case por esa unión a través de guiones bajos. ¡No usar guiones altos!
Da error.

- No existen las contantes. Pero aquellas variables que quiera dejar constantes, las
defino con mayúsculas (Upper snake case):
PI = 3.1416
a PI se le puede asignar otro valor en cualquier parte del código.
"""
'''
ESto también es un comentario de bloque
'''
'''
Dado (pedir al usuario / input -pregunta-) un nombre y apellido, el programa ha de mostrar el número de caracteres tanto del nombre como del apellido.
'''
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')
nombre = input(Fore.GREEN + "Díme tu nombre: \n" + Style.RESET_ALL)
#print(Style.RESET_ALL)
apellido = input(Fore.CYAN + "Díme tu apellido: \n" + Style.RESET_ALL)
#print(Style.RESET_ALL)
longitud_nombre = len(nombre)
longitud_apellido= len(apellido)

#mensaje = "El número total de caracteres del "
#Con esta función 'format' no hace falta convertir a cadena de caracteres los números
#que van a ser imprimidos junto a la cadena de carracteres:
print (Style.BRIGHT + Fore.YELLOW + "El número de caracteres del nombre es: " + Fore.WHITE + "{}".format(longitud_nombre) + Fore.YELLOW + " y la del apellido es " + Fore.WHITE + "{}" .format(longitud_apellido))
print(Style.RESET_ALL)

