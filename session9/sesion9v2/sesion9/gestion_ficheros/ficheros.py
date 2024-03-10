import os

#ruta_directorio = os.path.dirname(__file__)

def sanitizar_cadena(cadena: str) -> str: #devolvemos cadena de entrada limpia
    return cadena.strip()

def sanitizar_data(data: list) -> list:
    data_limpia = list()
    for cadena in data:
        data_limpia.append(sanitizar_cadena(cadena))
    else:
        return data_limpia


def escribir_data(path: str, *mensajes):
    #with open(f'./data/{nombre_fichero}', 'w') as f:
    with open(path, 'w') as f:    
        for mensaje in mensajes:
            f.write(f"{mensaje}\n")
    
def leer_data(path: str) -> list:

    f = None
    data = None
    try:
        #with open(f"./data/{nombre_fichero}", 'r') as f:
        with open(path, 'r') as f:    
            data = sanitizar_data(f.readlines())

    except FileNotFoundError as fnfex:
        print(fnfex)
    
    return data



