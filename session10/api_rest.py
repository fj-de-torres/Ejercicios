## Versión del profesor:

### Bajar los usuarios y guardarlos en un fichero en formato csv (id, username, email, website)
import os
import requests

def obtener_usuarios(path:str) -> list[dict]:
    response = requests.get(path)  #end point
    data = response.json() #conversion a estructuras de datos python
    #print(f"LAT USER 1: {data[0]['address']['geo']['lat']}") #Accediendo más allá en el diccionario
    return data
    return data

def obtener_linea_usuario(data: dict) -> str:
    return f'{",".join((str(data["id"]),data["username"],data["email"],data["website"]))}\n'

#join necesita que todos los elementos a unir sea cadena. id es un número
"""Funcion que vuelca la informacion de usuarios a un fichero csv"""

def guardar_usuarios(path: str,data:list[dict]) -> bool:
    assert data is None, "Data no puede ser nulo"
    header = "id,username,email.website"
    try:
        with open(path,'w') as f:
            for usuarios_csv in data:
                usuarios_csv.append(obtener_linea_usuario(user))
            else:
                f.writelines(usuarios_csv.insert(0,f"{header}\n"))
                f.writelines(usuarios_csv)

                 #f'{",".join((user['id'],user['username'],user['email'],user['website']))}\n'
    except Exception:
        return False
    else:
        return True
""" 
    Si escribo un return vacío, el resultado que arroja la función es *None*
    assert: qué quiero que ocurra para que todo vaya bien.
    Destructuring: a, b = (1, 3) ==> a = 1, b = 3. ¿Tiene sentido en un diccionario?
    [(a,b),(c,d)]... Pero en el diccionario se tendrá una lista de listas ¿Nos conviene un destructuring?
    En este caso no nos conviene el destructuring. Vamos a hacer una tupla de users de los elementos que necesito
 """

USERS_ENDPOINT = 'https://jsonplaceholder.typicode.com/users'
if __name__=="__main__":
    #ingesta
    usuarios = obtener_usuarios(USERS_ENDPOINT)
    try:
        path = f'{os.path.dirname(__file__)}/data/usuarios.csv'
        if guardar_usuarios('./data/usuarios.csv', usuarios):
            print("Data almacenada")
    except AssertionError:
        print("Datos de entrada incorrectos")
    except Exception:
        print("Error general")
    
        



#Explicación del join:
"""     
    l = ['Hola','Adios']
    resultado = "*".join(l)
    print(resultado)
 """

#Variables dentro del string:
"""
 nombre = "Luis"

saludo = f"Hola {nombre}"
"""
#Esta f significa que podemos utilizar variables dentro del string
