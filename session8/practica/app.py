import os
ruta_directorio = os.path.dirname(__file__)

def lectura_fichero (nombre_archivo:str) -> list:
    archivo = None
    read_data = list()
    try:
        with open(f"{ruta_directorio}/{nombre_archivo}",'r') as archivo:
            for linea in archivo:
                partes = linea.split(",")
                


