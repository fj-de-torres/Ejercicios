# Objetos en Pyhton *(Objects in Python)*:

#Moveré las clases a módulos. Es decir, archivos distintos.
#Las clases se crean con la palabra reservada class. La convención es que sus nombre empienzan en mayúsculas:

class Escuela:
    #Constructor
    def __init__(self, nombre:str, director:str):
        self.nombre = nombre #Esta es la propiedad que da nombre a esta clase.
        self.director = director

class Curso:
    def __init__(self,nombre:str)
        self.nombre = nombre

class Alumno:
    pass








if __name__=="__main__":
    pass
    #Crear una escuela:
    pue = Escuela("PUE","Fernando") #Acabo de instanciar el objeto PUE a través de la clase escuela.
    print(pue.nombre)
    print(pue.director)
    python_essentials_1 = Curso("PCAP1")
    python_essentials_2 = Curso("PCAP2")

    #Crear los cursos de esa escuela y asociarlos a la misma:
    #Crear los alumnos de os cursos de la escuela
    #Asocial los alumnos a las asignaturas