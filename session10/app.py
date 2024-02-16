# Objetos en Pyhton *(Objects in Python)*:
import os
os.system("cls || clear")
#Moveré las clases a módulos. Es decir, archivos distintos.
#Las clases se crean con la palabra reservada class. La convención es que sus nombre empienzan en mayúsculas:

class Asignatura:
    def __init__(self, nombre:str, nota_corte: float):
        self.nombre = nombre
        self.nota_corte = nota_corte

    def esta_aprobada(self, nota_alumno: float) -> bool:
        return nota_alumno >= self.nota_corte   

class Alumno:
    def __init__(self,nombre:str, edad: int, num_estudiante:int):
        self.nombre = nombre
        self.edad = edad
        self.num_estudiante = num_estudiante
        self.asignaturas = list()

class Curso:
    def __init__(self,nombre:str):
        self.nombre = nombre
        self.alumnos = list()
    #Si usamos append, entonces vamos a agregar una lista dentro de otra lista. Es decir, nuestra lista inicial de alumnos sería una lista, y luego el append nos añadiría los datos como una lista entera dentro de la que ya teníamos.
    """
    def matricular(self, alumno:Alumno):
        if alumno is None: return
        self.alumnos.append(alumno)
    """
    def matricular(self, *alumnos):
        if alumnos is None: return
        self.alumnos.extend(list(alumnos))
        #self.alumnos.extend = [alumno for alumno in alumnos] *alternativa 2*
        #self.alumnos = self.alumnos + [alumno for alumno in alumnos] *Alternativa 3*
        #self.alumnos = self.alumnos + list(alumnos) *Alternativa 4*
        
    def listar_alumnos(self):
        print("-" * 25, self.nombre, "-" * 25)
        for alumno in self.alumnos:
            print(alumno.nombre)
    
class Escuela:
    #Constructor
    def __init__(self, nombre:str, director:str):
        self.nombre = nombre #Esta es la propiedad que da nombre a esta clase.
        self.director = director
        self.cursos = list()

    def anyadir_curso(self, curso:Curso):
        self.cursos.append(curso) #Con self accedo a curso d dentro de la escuela, puesto que curso es otra clase.
    def listar_alumnos(self):
        #Llamada delegada. La escuela no lo puede hacer directamente porque no tiene el acceso pero se lo pregunto a la clase curso, que tendrá que tenerlo definido:
        for curso in self.cursos:
            curso.listar_alumnos()
#Las funciones pasan a llamarse *métodos* dentro de una clase
        




if __name__=="__main__":
    pass
    #Crear una escuela:
    pue = Escuela("PUE","Fernando") #Acabo de instanciar el objeto PUE a través de la clase escuela.

    """ 
    print(pue.nombre)
    print(pue.director)
 """

    #Crear los cursos de esa escuela y asociarlos a la misma:
    python_essentials_1 = Curso("PCAP1")
    python_essentials_2 = Curso("PCAP2")
    pue.anyadir_curso(python_essentials_1)
    pue.anyadir_curso(python_essentials_2)
    #Crear los alumnos de os cursos de la escuela:
    juan = Alumno('Juan Palomo', 23, 123)
    maria = Alumno ('Maria Pelaez', 22, 1234)
    luis = Alumno('Luis Aute', 21, 12345)
    alicia = Alumno('Alicia Perez', 21, 123456)
    jaime = Alumno('Jaime Urrutia',24,1234567)


""" 
    python_essentials_1.matricular(juan)
    python_essentials_1.matricular(maria)
    python_essentials_1.matricular(luis)
 """
python_essentials_1.matricular(juan, maria, luis)
    #Asocial los alumnos a las asignaturas

#Listado de alumnos:
pue.listar_alumnos()

python_essentials_2.matricular(alicia,jaime)

pue.listar_alumnos()

