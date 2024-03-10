import os

from gestion_ficheros.ficheros import leer_data, escribir_data
from transformers import transformar_data
from gestion_tareas import anyadir_tarea, entrada_valida



def main():
    #ingesta de datos
    ruta_directorio = f"{os.path.dirname(__file__)}\\data"
    tareas = transformar_data(leer_data(f'{ruta_directorio}\\tareas.txt'))
    print(tareas)
    info_usuario = input("Nueva tarea (separa con , nombre tarea y prioridad (alta/media/baja)):?") 
    nueva_tarea = info_usuario if entrada_valida(info_usuario) else None
    tareas = anyadir_tarea(tuple(nueva_tarea.split(",")), tareas) if nueva_tarea else tareas
    
    print("*" * 50)
    print(tareas)


if __name__ == "__main__":
    main()