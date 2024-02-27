from dataclasses import dataclass

@dataclass
class Examen:
    tema: str
    nota: float



class Profesor:

    def __init__(self, nombre, asignatura) -> None:
        self._nombre = nombre
        self.__asignatura = asignatura

    def corregir_examen(self, examen: Examen)
