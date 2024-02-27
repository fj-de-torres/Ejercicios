# Clases especiales:
### Data class: clases que aportan sólo datos.
Con del decorador @dataclass. Viene el de hacer:
```
from dataclasses import dataclass
```
```
@dataclasss
class Examen:
    tema: str
    nota: float = 0.0 # se puede poner un valor por defecto a demás de establecer el tipo de dato
```
Se puede poner un valor por defecto a demás de establecer el tipo de dato
Los atributos deben ser públicos en los *@dataclass*
```
class Profesor:

    def __init__(self, nombre, asignatura) -> None:
        self._nombre = nombre
        self.__asignatura = asignatura

    def corregir_examen(self, examen: Examen) -> Examen:
        import random
        examen.nota  random.random()*10
        return examen

```
```
examen_mates = Examen('Matematica')
profe_juan = Profesor('Juan', 'Mates')

examen_mates_corregido = profe_juan.corregir_examen(examen_mates)
print(examen_mates_corregido.nota)
```
Resultado:
> 7.74
