#🅻🅸🆂🆃🅰🆂:

import os
os.system("cls || clear")
# Valores booleanos = [] #lista vacía

valores_booleanos = [True, True, False, True, True, False] #Lista de elementos booleanos

#Recorrer la lista:
numero_trues = 0
numero_falses = 0
for valor_booleano in valores_booleanos:
    if valor_booleano == True:
        numero_trues = numero_trues + 1
    elif valor_booleano == False:
        numero_falses = numero_falses + 1

print(f"Numero de trues: {numero_trues}", f"Número de falses: {numero_falses}", sep = " --- ")
numero_trues = 0
numero_falses = 0
#Solución Concisa:
for list_element in valores_booleanos:
    numero_trues += 1 if list_element == True else 0
    numero_falses += 1 if list_element == False else 0

print(f"Numero de trues: {numero_trues}", f"Número de falses: {numero_falses}",sep = " <---> ")

program = ["python","Java","kotlin","Typescript","C#"]
#O también puedo crear una lista vacía y ya la llenaré luego:
programación = []
#Añadir items a la lista:
def crear_data():
    program = list()
    #anyadir items  a la lista
    program.append("Python")
    program.append("Java")
    program.append("Kotlin")
    program.append("TS")
    program.append("C#")

    return program
programacion = crear_data() #Invocación para crear la lista programación

def eliminar_duplicados(lista_lenguajes):
    lista_sin_duplicados = []
    for lenguaje in lista_lenguajes:
        if lenguaje in lista_sin_duplicados: continue #sal de lo que queda del for y inicial y pasa a la siguiente iteración.
    lista_sin_duplicados.append(lenguaje)
    return lista_sin_duplicados

def eliminar_duplicados2(lista_lenguajes):
    if lenguaje not in lista_lenguajes: 
        lista_lenguajes.append(lenguaje)
        return lista_lenguajes

'''
Lenguajes a añadir:
- Evitamos duplicados.
- Pedir un lenguaje al usuario evitando que se produzca en la lista de programacion, duplicidades
- Ask the user for a language name preventing duplicities inside the "programacion" list
'''
# Comprobación:
#Antes:
#𝗗𝗼𝗻'𝘁 𝗿𝗲𝗽𝗲𝗮𝘁 𝘆𝗼𝘂𝗿𝘀𝗲𝗹𝗳!
#𝔻𝕖𝕗𝕚𝕟𝕚𝕔𝕚ó𝕟 𝕕𝕖 𝕦𝕟𝕒 𝕗𝕦𝕟𝕔𝕚ó𝕟:
def listar_lenguajes(whateverlist):
    for lenguaje in whateverlist:
        print(lenguaje)
    print("--------")

def normalizar_datos(lista_lenguajes):
    #Convertir todos los lenguajes a minúscula
    lista_lenguajes_normalizada = list()
    for lenguaje in lista_lenguajes:
        lista_lenguajes_normalizada.append(lenguaje.lower)
    return lista_lenguajes_normalizada

#listar_lenguajes(programacion) #invocación
programacion= crear_data()
programacion_normalizada = eliminar_duplicados(normalizar_datos(programacion))

#listar_lenguajes(programacion_normalizada)
#programacion_normalizada_sin_duplicados
lenguaje = input ("Añada otro lenguaje: ")
# if programacion != None and type(programacion) == list and lenguaje != None and lenguaje != "":
#     for list_item in programacion:
#         if list_item.lower() == lenguaje.lower():
#                 programacion.append(lenguaje)
#     print("Sorry, that language is already in the list")
# else:
#     print("Please, do not insert empty strings!")
if programacion != None:
    if type(programacion) == list:
        if lenguaje != None and lenguaje != "":
            programacion_normalizada.append(lenguaje) if lenguaje.lower() not in programacion_normalizada else None
            # lenguaje not in programacion and programacion.append(lenguaje)
# Comprobación:
#Después:
listar_lenguajes(programacion)
