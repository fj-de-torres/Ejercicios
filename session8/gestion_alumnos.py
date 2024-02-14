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
    buscar_indice
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
#CRUD -> Create, Read, Update, Delete

def matricular(alumno: tuple, l_alumnos: list):
    """ sirve para añadir un nuevo alumno al curso""" #docstring
    if l_alumnos is not None and alumno is not None:
        l_alumnos.append(alumno)
    return l_alumnos


def buscar_indice(alumno: tuple, l_alumnos: list) -> int:
    posicion_alumno = None
    for index, al in enumerate(l_alumnos):
        if al == alumno:
            posicion_alumno = index  
    return posicion_alumno

def modificar(alumno: tuple, alumno_modificado: tuple, l_alumnos: list):
    posicion = buscar_indice(alumno, l_alumnos)
    if posicion is not None:
        l_alumnos[posicion] = alumno_modificado    
    
    return l_alumnos

def dar_de_baja(alumno: tuple, l_alumnos: list):
    index = buscar_indice(alumno,l_alumnos)
    alumno_borrado = l_alumnos.drop(index)
    return l_alumnos

def mostrar(alumno: tuple, l_alumnos: list) -> tuple:
    index = buscar_indice(alumno,l_alumnos)
    alumno_a_mostrar = l_alumnos[index]
    print(alumno_a_mostrar)
    return alumno_a_mostrar

