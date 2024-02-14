# Ficheros
import os
#Where the Hell am I?
ruta_directorio = os.path.dirname(__file__)
#More info: https://docs.python.org/3/library/pathlib.html
## Elemento que nos permite persistencia.

def escribir_data(nombre_fichero: str, *mensajes):
    with open(f'{ruta_directorio}/data/{nombre_fichero}', 'w') as f:
        for mensaje in mensajes:
            f.write(f"{mensaje}\n")
    
def leer_data(nombre_fichero: str) -> str:

    f = None
    data = None
    try:
        with open(f"{ruta_directorio}/data/{nombre_fichero}", 'r') as f:
            data = f.readlines() #Y esto devolverá una lísta de lo leído en cada línea

    except FileNotFoundError as fnfex:
        print(fnfex)
    
    return data


