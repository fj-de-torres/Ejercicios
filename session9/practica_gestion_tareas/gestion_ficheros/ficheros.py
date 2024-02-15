# Fichero
import os
#Where the Hell am I?
ruta_directorio = os.path.dirname(__file__)
#More info: https://docs.python.org/3/library/pathlib.html
## Elemento que nos permite persistencia.

def sanitizar_cadena(cadena:str) -> str: #Devolvemos la cadena limpia
    return cadena.strip() #De momento quito todo a izda y derecha (rstrip() si sólo quiero a la derecha)

def sanitizar_data (data: list) -> list:
    data_limpia = list()
    for cadena in data:
        data_limpia.append(sanitizar_cadena(cadena))
    else: #Este 'else' sólo se ejecuta si el for se ha ejecutado completamente (si ha conseguido ejecutar el recorrido completo del FOR). Con que se ejecute un break dentro del for, el 'else' ya no se ejecutaría. Me estoy asegurando de que el for se esté ejecutando correctamente.
        return data_limpia


def escribir_data(nombre_fichero: str, *mensajes):
    with open(f'{ruta_directorio}/data/{nombre_fichero}', 'w') as f:
        for mensaje in mensajes:
            f.write(f"{mensaje}\n")
    
def leer_data(nombre_fichero: str) -> str:

    f = None
    data = None
    try:
        archivo = open(f"{ruta_directorio}/data/{nombre_fichero}", 'r')
        data = sanitizar_data(f.readlines()) #Y esto devolverá una lísta de lo leído en cada línea

    except FileNotFoundError as fnfex:
        print(fnfex)
    
    return data


