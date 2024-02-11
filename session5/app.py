import os
os.system ("cls || clear")
from colorama import Fore, Back, Style
#Tratamiento de clientes:
#DNI, Nombre, Apellido, CP.

# ¿Una lista de diccionarios podría ser?
""" 
clientes = [{
    'dni' : '111H',
    'nombre' : 'Pedro',
    'apellido' : 'López',
    'cp' : '08009'
}]
 """

#Tendré que hacer cosas como buscar cliente, eliminar cliente, etc.
#Haremos un contendedor principal como diccionario donde la clave de acceso va a ser el DNI de cada cliente.
#A este, le podemos asociar el resto de los datos como lista, tuplas, diccinario....
""" 
cliente = {
    '111H': {
        'dni':'111H',
        'nombre':'Pedro',
        'cp' : '08009'
    }
}
 """

def crear_cliente(data:dict) -> dict:
    id_cliente = data['dni']
    cliente = { id_cliente: data}
    return cliente
def eliminar_cliente(clave: str, diccio: dict):
    if clave in diccio:
        diccio.pop(clave)
    return diccio

def buscar_cliente(dni_cliente:str, d_clientes:dict) -> dict:
    if dni_cliente not in d_clientes: return #Esto devuelve un None si el DNI no existe. Salgo de la función
    return d_clientes[d_clientes]

def buscar_cliente(dni_cliente: str, d_clientes: dict) -> dict:
    return d_clientes.get(dni_cliente)
"""     
    if dni_cliente not in d_clientes: return #None
    return d_clientes[dni_cliente]
 """
    
          # print (_) #dará el resto; o sea, el diccioario de cada cliente
# Aclaración
# dni, *_ = [(1,2,3,4),(8,9,7,6), (1,2,3,4,5)]
# print(dni)

clientes = dict()

if __name__ == "__main__":
    data_cliente1 = {
        'dni':'111H',
        'nombre': 'Juan',
        'apellido': 'Lopez',
        'cp': '08009'
    }
    data_cliente2 = {
        'dni':'222H',
        'nombre': 'Maria',
        'apellido': 'Lopez',
        'cp': '08009'
    }
    data_cliente3 = {
        'dni':'333H',
        'nombre': 'Belen',
        'apellido': 'Fernandez',
        'cp': '28090'
    }
    clientes.update(crear_cliente(data_cliente1))
    clientes.update(crear_cliente(data_cliente2))
    clientes.update(crear_cliente(data_cliente3))

    
    # print(f"Clientes al inicio: {clientes}")
    # print(f"Clientes eliminado 222H: {clientes}")
    clave = '333H'
    #clientes= eliminar_cliente(clave, clientes)

    #Preguntar al usuario el dni y buscar dicho cliente
    cliente = buscar_cliente(input('DNI a buscar:'),clientes)
    if cliente:
        print(list(cliente.items())[1:])
        print(dict(list(cliente.items())[1:])) #Aquí vuelve a ser diccionario.

    else:
        print("No existe")