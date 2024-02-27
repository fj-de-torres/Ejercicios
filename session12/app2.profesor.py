from dataclasses import dataclass

@dataclass
class Examen:
    tema: str
    nota: float = 0.0

    @classmethod
    def crear_examen(cls, tema:str):
        return cls(tema)



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
    

"""
examen_mates = Examen('Matematica')
examen_literatura = Examen('Literatura')
examen_ingles = Examen('English')

profe_juan = Profesor('Juan', 'Mates')


examenes_corregidos = profe_juan.corregir_examenes(examen_mates, examen_literatura)

for index, examen in enumerate(examenes_corregidos, start=1):
    print(f"{examen.tema}_{index}" , examen.nota, sep=":")

"""
asignaturas = ["mates", "literatura"]
PREFIX = "examen_"

profe_juan = Profesor('Juan', 'Mates')
lista = list()
for asig in asignaturas:
    lista.append(Examen.crear_examen(asig))
else:
    examenes_corregidos = profe_juan.corregir_examenes(*lista)
    for examen in examenes_corregidos:
        print(examen.tema , examen.nota, sep=":")
    




"""
1) El profesor podrá corregir varios examenes
2) Modularizar el app
"""



    