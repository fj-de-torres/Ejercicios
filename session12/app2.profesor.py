from dataclasses import dataclass

@dataclass
class Examen:
    tema: str
    nota: float = 0.0



class Profesor:

    def __init__(self, nombre, asignatura) -> None:
        self._nombre = nombre
        self.__asignatura = asignatura

    def corregir_examenes(self, *examenes: tuple) -> list[Examen]:
        examanes_corregidos = list()
        #version oficial
        for examen in examenes:
            examanes_corregidos.append(self.corregir_examen(examen))
        return examanes_corregidos
    
        #alternativa
        return [self.corregir_examen(examen) for examen in examenes]    
        
        

    def corregir_examen(self, examen: Examen) -> Examen:
        import random
        examen.nota = round(random.random() * 10, 2) 
        return examen
    

examen_mates = Examen('Matematica')
profe_juan = Profesor('Juan', 'Mates')

examen_mates_corregido = profe_juan.corregir_examen(examen_mates)
print(examen_mates_corregido.nota)

"""
1) El profesor podrá corregir varios examenes
2) Modularizar el app
"""
