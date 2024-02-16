
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

    def matricular_asignaturas(self, *asignaturas:tuple):
        for alumno in self.alumnos:
            alumno.matricular_asignaturas(*asignaturas)

    def listar_alumnos(self):
        print("-" * 25, self.nombre, "-" * 25)
        for alumno in self.alumnos:
            #print(alumno.nombre, ",".join(alumno.asignaturas), sep=":")
            #print(alumno.nombre, ",".join([str(asignatura) for asignatura in alumno.asignaturas]), sep=":")
            print(alumno.nombre, ",".join([asignatura.nombre for asignatura in alumno.asignaturas]), sep=":")
