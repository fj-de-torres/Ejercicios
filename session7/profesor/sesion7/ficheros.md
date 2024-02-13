
def escribir_data(nombre_fichero: str, *mensajes):
    f = open(f'./data/{nombre_fichero}', 'w')
    for mensaje in mensajes:
        f.write(f"{mensaje}\n")
    
    f.close()


def escribir_data_v2(nombre_fichero: str, *mensajes):
    with open(f'./data/{nombre_fichero}', 'w') as f:
        for mensaje in mensajes:
            f.write(f"{mensaje}\n")
    
def leer_data(nombre_fichero: str) -> str:

    f = None
    data = None
    try:
        f = open(f"./data/{nombre_fichero}", 'r')
        data = f.read()
    except Exception as fnfex:
        print(fnfex)
    finally:
        if f:
            f.close()

    return data

def leer_data_v2(nombre_fichero: str) -> str:

    f = None
    data = None
    try:
        with open(f"./data/{nombre_fichero}", 'r') as f:
            data = f.read()

    except FileNotFoundError as fnfex:
        print(fnfex)
    
    return data



