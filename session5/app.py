import os
os.system ("cls || clear")
#from colorama import 
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
#A este, le podemos asocial el resto de los datos como lista, tuplas, diccinario....
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
def buscar_cliente():
    pass
def mostrar_cliente(d_clientes:dict):
    if d_clientes is not None:
        for dni, _ in d_clientes.items():
            print(dni)
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
    clave = '222H'
    clientes= eliminar_cliente(clave, clientes)