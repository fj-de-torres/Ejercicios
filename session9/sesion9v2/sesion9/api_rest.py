import requests
import os

def obtener_usuarios(path: str) -> list[dict]:
    response = requests.get(path) #end point
    data = response.json() #conversion a estructuras de datos python
    print(f"LAT USER 1: {data[0]['address']['geo']['lat']}")
    return data

def obtener_linea_usuario(data: dict) -> str:
    
    return f'{",".join((str(data['id']),data['username'],data['email'],data['website']))}\n'

def guardar_usuarios(path: str, data: list[dict]) -> bool:
    """Funcion que vuelca la informacion de usuarios a un fichero csv"""

    assert data is not None, "Data no puede ser nulo!"
    header = "id,username,email,website"

    try:
        with open(path, 'w') as f:
            usuarios_csv = list()
            for user in data:
                usuarios_csv.append(obtener_linea_usuario(user))
            else:
                usuarios_csv.insert(0,f"{header}\n")
                f.writelines(usuarios_csv)
    except Exception:
        return False
    else:
        return True        
    
        
            




"""
Bajar los usuarios y guardarlos en un fichero en formato csv (id, username, email, website)
"""
USERS_ENDPOINT = 'https://jsonplaceholder.typicode.com/users'

if __name__ == "__main__":
    
    #ingesta
    usuarios = obtener_usuarios(USERS_ENDPOINT)
    try:
        path = f'{os.path.dirname(__file__)}\\data\\usuarios.csv'
        if guardar_usuarios(path, usuarios):
            print("Data almacenada")
    except AssertionError:
        print("Datos de entrada incorrectos")
    except Exception:
        print("Error general")
    
    




