

def cargar_clientes() -> list:
    with open('./data/clientes.csv)') as f:
        #El propio ***f*** con el que abro el archivo también es un iterable
        for linea in f.readlines()[1:]:
            print(linea.strip()).split(',')
            #Esto es que quiero todas las línes menos la primera (porque la primera es la cabecera, que no me interesa). Tengo que usar el readlines porque f no es una lista
            #Comprehension list equivalente:
            #[linea.strip()].split(',') for linea in f.readlines()[1:]]

def guardar_clientes(l_clientes):
    with open('./data/clientes.csv') as f:
        for cliente in l_clientes:
            

def main():
    clientes = cargar_clientes()