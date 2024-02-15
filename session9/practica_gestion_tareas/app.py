from gestion_ficheros.ficheros import leer_data, escribir_data
def main():
    #Ingesta de datos
    tareas = leer_data('tareas.txt')
    print(tareas)

if __name__== "__main__":
    main() #Llama al programa principal en vez de andar soltando código aquí