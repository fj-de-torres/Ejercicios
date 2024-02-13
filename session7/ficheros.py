# Ficheros
#Elemento que nos permite persistencia.

## Creación:
f = open('data/items.txt','w') #f sería el handler. Para referirme al fichero abierto
f.write("Hola Mundo") # Creará el fichero si lo abrimos en modo escritura si no existe.
#Si existe y escribo, sobreescribe lo que había. Para añadir en vez de sobre escribir, lo abro como append:
f.close()
f = open('data/items.txt','a')
f.write("Hola Python")
f.close()

def escribir_data(nombre_fichero: str,*mensajes):
    f = open(f'data/{nombre_fichero}','w')
    for mensaje in mensajes:
        f.write(f"{mensaje}\n")
    f.close()

def escribir_data_v2(nombre_fichero: str, *mensajes):
    with open(f'./data/{nombre_fichero}', 'w') as f:
        for mensaje in mensajes:
            f.write(f"{mensaje}\n")

## Lectura:
#Hay que asegurarse de que existe, si no, daría un error:
""" 
def leer_data(nombre_fichero:str) -> str:
    try:
        f = open(f"./data/{nombre_fiechero}",'r') # f es una variable local al bloque. Por eso no va a cerrar con f.close. Así que tengo que subir un nivel la declaración de la variable
        data = f.read()
    except FileNotFoundError as fnfex:
        print(fnfex)
    finally:
                f.close() #Siempre que acceda a un fiechero con open(), es necesario cerrarlo con close()
    return data
 """
def leer_data(nombre_fichero: str) -> str:

    f = None
    data = None
    try:
        f = open(f"./data/{nombre_fichero}", 'r')
        data = f.read()
    except FileNotFoundError as fnfex:
        print(fnfex)
    finally:
        if f: # <= Si existe f
            f.close()

    return data

def leer_data_v3(nombre_fichero: str) -> str:

    f = None
    data = None
    try:
        with open(f"./data/{nombre_fichero}", 'r') as f:
            data = f.read()
    except FileNotFoundError as fnfex:
        print(fnfex)

    return data

