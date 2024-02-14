#CRUD -> Create, Read, Update, Delete

#Deberíamos tener una función buscar_alumno:
def buscar(alumno:tuple, l_alumnos:list) -> tuple:
    posicion_alumno = None #(parto por defecto del echo de que no esté)
    for index, al in enumerate(l_alumnos):
        if al == alumno:
            posicion_alumno = index
    return posicion_alumno

def matricular(alumno: tuple, l_alumnos: list):
    """ Sirve para añadir un nuevo alumno al curso """ #A est se le llama "docstring"
    if l_alumnos is not None and alumno is not None:
        l_alumnos.append(alumno)
    return l_alumnos

def dar_de_baja(alumno: tuple, l_alumnos: list):
    pass
    # if alumno in l_alumnos
    #     alumno_borrado = 

def mostrar(l_alumnos: list):
    pass
""" Versión con apuntes que no funciona porque algo ahí está mal:
def modificar(alumno: tuple,alumno_modificado:tuple, l_alumnos: list):
    #Primero buscar la tupla (y luego modificarlo):
    for index, al in enumerate(l_alumnos):
        if al == alumno:
            #break #salgo porque ya lo he encontrado
            l_alumnos[index] =alumno_modificado
        return l_alumnos
  """   

""" 
def modificar(alumno: tuple, alumno_modificado: tuple, l_alumnos: list):
    for index, al in enumerate(l_alumnos):
        if al == alumno:
            l_alumnos[index] = alumno_modificado
    return l_alumnos
 """

