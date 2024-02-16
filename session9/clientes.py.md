import os
header  = None

def cargar_clientes() -> list:
    global header
    path_data = f"{os.path.dirname(__file__)}/data/clientes.csv"
    with open('./data/clientes.csv','r') as f:
        #El propio ***f*** con el que abro el archivo también es un iterable
        """ for linea in f.readlines()[1:]:
        print(linea.strip()).split(',') """
        #Esto es que quiero todas las línes menos la primera (porque la primera es la cabecera, que no me interesa). Tengo que usar el readlines porque f no es una lista
        #Comprehension list equivalente:
        #[linea.strip()].split(',') for linea in f.readlines()[1:]]
        lineas = f.readlines()
        header = lineas[0] #Variable local
        return [linea.strip().split(',') for linea in lineas[1:]]
""" 
def guardar_clientes(l_clientes):
    path_data = f"{os.path.dirname(__file__)}/data/clientes.csv"
    with open(path_data, 'w') as f:
        clientes = list()
        for cliente in l_clientes:
            clientes.append(",".join(clientes))
        else: #Este else ocurre si acabamos el for de forma completa
            clientes.insert(0,header)
            f.writelines(clientes)
 """

def guardar_clientes(l_clientes):
    path_data = f"{os.path.dirname(__file__)}/data/clientes.csv"
    with open(path_data, 'w') as f:
        clientes = list()
        for cliente in l_clientes:
            clientes.append(f'{",".join(cliente)}\n')
        else:
            clientes.insert(0, header)
            f.writelines(clientes)

def main():
    clientes = cargar_clientes()
    guardar_clientes(clientes)

if __name__ == "__main__":
    main()