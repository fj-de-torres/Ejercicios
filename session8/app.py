import os
from ficheros import leer_data
os.system("cls || clear")
def mostrar_alumnos(l_alumnos: list):
    for alumno in l_alumnos:
        print(alumno)

if __name__ == "__main__":
    nombre_alumnos = leer_data('alumnos.txt')
    
    mostrar_alumnos(nombre_alumnos)
    