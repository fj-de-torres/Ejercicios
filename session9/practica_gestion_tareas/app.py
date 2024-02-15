import os

from gestion_ficheros.ficheros import leer_data, escribir_data
from gestion_ficheros.transformers import transformar_data
from gestion_tareas import anyadir_tarea

def entrada_valida(cadena:str):
    return type(cadena) == str

def main():
    #ingesta de datos
    ruta_directorio = f"{os.path.dirname(__file__)}\\data"
    tareas = transformar_data(leer_data(f'{ruta_directorio}\\tareas.txt'))
    #print(tareas)
    info_usuario = input("Nueva tarea (separa con , nombre tarea y prioridad (alta/media/baja)):?") 
    nueva_tarea = info_usuario if entrada_valida(info_usuario) else None
    tareas = anyadir_tarea(tuple(nueva_tarea.split(",")),tareas) if nueva_tarea else tareas 
    print("*"*50)
    print(tareas)
    #Si no ha sido una entrada correcta, lo que añado a tareas es otra vez tareas. O sea, que me quedo como estaba.
    #nueva_tarea and anyadir_tarea(nueva_tarea) or 
    #Lo bueno de añadir and es que si la entrada del usuario ha sido invádida, anyadir_tarea no se va a ejecutar y por lo tanto no vamos a añadir información. No hay riesgo de añadir información inválida o rara o de formato incorrecto

if __name__ == "__main__":
    main() #Llama al programa principal en vez de andar soltando código aquí