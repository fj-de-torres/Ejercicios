def lectura_fichero (nombre_archivo:str) -> list:
    archivo = None
    tareas = list()
    try:
        with open(f"{ruta_directorio}/{nombre_archivo}",'r') as archivo:
            for linea in archivo:
                partes = linea.split(",")
                if len(partes) == 2: #
                    tareas.append(partes[0],partes[1])
    except FileNotFoundError:
            respuesta = "y"
            print(f"File not found. I will create this new one: {ruta_directorio}/{nombre_archivo}")
            archivo = open(r"{ruta_directorio}",'w')
            # respuesta = input("Is that ok? (y/n)")
            # if respuesta != "y":
            #      lectura_fichero
    finally:
         if archivo:
              archivo.close()
    return tareas