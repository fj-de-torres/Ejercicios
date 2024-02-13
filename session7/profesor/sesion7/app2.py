from ficheros import escribir_data_v2, leer_data_v2

if __name__ == "__main__":
    
    escribir_data_v2('items.txt', 'Hola', 'Adios')
    data = leer_data_v2('items.txt')
    if data:
        print(f"DATA:{data}")
    