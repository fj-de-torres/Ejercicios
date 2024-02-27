from dataclasses import dataclass

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


    