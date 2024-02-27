from dataclasses import dataclass
import random

@dataclass
class Examen:
    tema: str
    nota: float = 0.0



class Profesor:

    def __init__(self, nombre, asignatura) -> None:
        self._nombre = nombre
        self.__asignatura = asignatura

    def corregir_examen(self, examen: Examen) -> Examen:
        import random
        examen.nota = random.random() * 10 
        return examen
    

examen_mates = Examen('Matematica')
profe_juan = Profesor('Juan', 'Mates')

examen_mates_corregido = profe_juan.corregir_examen(examen_mates)
print(examen_mates_corregido.nota)

"""
1) El profesor podrá corregir varios examenes
2) Modularizar el app
"""
if __name__ == "__main__":
    asignaturas = ['Matematicas','Lengua','Física','Quinmica','Geografia','Historia','Ingles','Frances','Aleman','Catalan']
    profesores = ['Juan','Pedro','Pablo']
    def examenes_a_corregir(num:int = 3,asignaturas:int = asignaturas) -> list:
        return random.sample(asignaturas,k= num)
    
    def profesor(profesores:list = profesores)
        return random.choice(profesores)
    
    numero_examenes = int("Give me number of subects to grade: ")
    profe = profesor(profesores)
    asignaturas_a_corregir = examenes_a_corregir(asignaturas, numero_examenes = 4)
    for _ in asignaturas_a_corregir:
        pass