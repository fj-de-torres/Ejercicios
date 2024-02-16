from curso import Curso
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
        
