import os
from ficheros import leer_data
import transformers as trans

def mostrar_alumnos(l_alumnos: str) -> list:
    lista_alumnos = list()
    for alumno in l_alumnos:
        #print(alumno)
        lista_alumnos.append(tuple(alumno.split()))
    return lista_alumnos
    # Tratar de hacerlo con un comprehension list


if __name__ == "__main__":
    os.system("cls || clear")
    nombre_alumnos = leer_data('alumnos.txt')
    mostrar_alumnos(nombre_alumnos)

##### Crear una lista de tuplas, cada una formadas por el nombre y el apellido:

    print(mostrar_alumnos(nombre_alumnos))

## Solución del profesor:
#Esto ha de estar en el programa principal
#crear una lista de tuplas formadas por el nombre y el apellido
#['a b', 'c d', 'e f'] -> [('a','b'),('c','d'),('e','f')]
print(trans.transformar_data(nombre_alumnos))   

    