class Alumno:
    def __init__(self,nombre:str, edad: int, num_estudiante:int):
        self.nombre = nombre
        self.edad = edad
        self.num_estudiante = num_estudiante
        self.asignaturas = list()

    #def matricular_asignatura(asignatura: Asignatura):
    def matricular_asignaturas(self, *asignaturas):
        #self.asignaturas.extend(list(asignaturas))
        self.asignaturas.extend([*asignaturas]) #[(a,b)]

