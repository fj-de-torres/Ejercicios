# Clases especiales:
## Data class: clasess que aportan sólo datos.
Con del decorador @dataclass. Viene el de hacer:
```
from dataclasses import dataclass
```
```
@dataclasss
class Examen:
    tema: str
    nota: float
```
```
class Profesor:

    def __init__(self, nombre, asignatura) -> None:
        self._nombre = nombre
        self.__asignatura = asignatura

    def corregir_examen(self, examen: Examen)
```
    