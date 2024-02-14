import os
from gestion_alumnos import matricular, modificar, obtener_alumnos, dar_de_baja
from ficheros import leer_data, escribir_data
import transformers as trans
#from gestion_alumnos import matricular, modificar
import gestion_alumnos

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
#print(trans.transformar_data(nombre_alumnos))   
    

    alumnos = trans.transformar_data(nombre_alumnos)

    print(f"ANTES de MAT:{alumnos}")
    matricular(('Fabio','Scanferla'),alumnos)
    print(f"DESPUES de MAT: {alumnos}")
    alumnos = modificar(('Luis','Albert)'),('Luis','Alberto'), alumnos)

    alumnos = dar_de_baja(('Marta', 'Gomez'), alumnos)

    print(obtener_alumnos(alumnos))

    #dump de datos de alumnos sobr un fichero llamado alumnos_out.txt
    """ 
    def alumnos_data_dump (l_alumnos:list,ruta_fichero:str) -> str:

        escribir_data(ruta_fichero,obtener_alumnos(l_alumnos))
    alumnos_data_dump(dump.txt,)
 """
## Solución del profesor:
    alumnos_dump = obtener_alumnos(alumnos)
    escribir_data('alunnos_out.txt',alumnos_dump)

