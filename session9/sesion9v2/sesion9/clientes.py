import os

header = None

def cargar_clientes() -> list:
    global header
    path_data = f"{os.path.dirname(__file__)}\\data\\clientes.csv"
    with open(path_data) as f:
        """
        for linea in f.readlines()[1:]:
            print(linea.strip().split(','))
        """
        lineas = f.readlines()
        header = lineas[0] #local
        return [linea.strip().split(',') for linea in lineas[1:]]


def guardar_clientes(l_clientes):
    path_data = f"{os.path.dirname(__file__)}\\data\\clientes.csv"
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