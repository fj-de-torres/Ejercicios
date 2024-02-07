# valores_booleanos = [] #lista vacia
valores_booleanos = [True, True, False, True, True, False] 

numero_trues = 0
numero_falses = 0
# numero_trues, numero_falses = 0, 0

""" for valor_booleano in valores_booleanos:
    if valor_booleano == True:
        numero_trues = numero_trues + 1
    elif valor_booleano == False:
        numero_falses = numero_falses + 1
 """
for valor_booleano in valores_booleanos:
    numero_trues = numero_trues + 1 if valor_booleano == True else numero_trues   
    numero_falses = numero_falses + 1 if valor_booleano == False else numero_falses 
    print(numero_trues, numero_falses)  

print(f"Numero de trues:{numero_trues}", f"Numero de falses:{numero_falses}", sep=" --- ")


#programacion = ["python", "Java", "Kotlin", "Typescript", "C#"]

def crear_data():
    program = list()
    #anyadir items  a la lista
    program.append("Python")
    program.append("JAVA")
    program.append("Kotlin")
    program.append("TS")
    program.append("C#")

    return program


#cargar datos
programacion = crear_data() #invocacion

"""
Pedir un lenguaje al usuario
evitando que se produzca en la lista programacion
duplicidades
"""

#definicion de una funcion
def listar_lenguajes(lista_lenguajes):
    for lenguaje in lista_lenguajes:
        print(lenguaje)  

def normalizar_datos(lista_lenguajes):
    #convertir todos los lenguajes a minuscula
    lista_lenguajes_normalizada = list() #variable local
    for lenguaje in lista_lenguajes:
        lista_lenguajes_normalizada.append(lenguaje.lower())  

    return lista_lenguajes_normalizada 


listar_lenguajes(programacion) #invocacion

programacion_normalizada = normalizar_datos(programacion) #invocacion y retorno

listar_lenguajes(programacion_normalizada)

lenguaje = input("Lenguaje?:")
if programacion_normalizada != None:
    if type(programacion_normalizada) == list:
        if lenguaje != None and lenguaje != "":
            programacion_normalizada.append(lenguaje) if lenguaje.lower() not in programacion_normalizada else None # None equivale a nop (no operation) 
            #lenguaje not in programacion and programacion.append(lenguaje) 
            


#despues
listar_lenguajes(programacion_normalizada)        




