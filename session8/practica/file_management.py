import os
#Gets the current directory:
ruta_directorio = os.path.dirname(__file__)

#Defines the subdirectory path to work in:
subdir_path = os.path.join (ruta_directorio, 'data')

#Checks if the working subdirectory does not exist:
if not os.path.exists(subdir_path):
     os.makedirs(subdir_path)
file_path = os.path.join(subdir_path, 'tasks.txt')

def lectura_fichero (nombre_archivo:str) -> list:
    archivo = None
    tareas = list()
    try:
        with open(f"{file_path}/{nombre_archivo}",'r') as archivo:
            for linea in archivo:
                partes = linea.split(",")
                if len(partes) == 2: #
                    tareas.append(partes[0],partes[1])
    except FileNotFoundError:
            #respuesta = "y"
            print(f"File not found. I will create this new one: {file_path}/{nombre_archivo}")
            archivo = open(f"{ruta_directorio}/data/",'w')
            # respuesta = input("Is that ok? (y/n)")
            # if respuesta != "y":
            #      lectura_fichero
    finally:
         if archivo:
              archivo.close()
    return tareas

