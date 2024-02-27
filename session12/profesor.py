from examen import Examen

class Profesor:

    def __init__(self, nombre, asignatura) -> None:
        self._nombre = nombre
        self.__asignatura = asignatura

    def corregir_examenes(self, *examenes: tuple) -> list[Examen]:
        examanes_corregidos = list()
        #version oficial
        for examen in examenes:
            examanes_corregidos.append(self.__corregir_examen(examen))
        return examanes_corregidos
    
        #alternativa
        #return [self.__corregir_examen(examen) for examen in examenes]    
        
    def __corregir_examen(self, examen: Examen) -> Examen:
        import random
        examen.nota = round(random.random() * 10, 2) 
        return examen