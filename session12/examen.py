from dataclasses import dataclass

@dataclass
class Examen:
    tema: str
    nota: float = 0.0

    @classmethod
    def crear_examen(cls, tema:str):
        return cls(tema)