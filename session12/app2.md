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
> *7.74*

#### Hacer:

> 1. El profesor podrá corregir varios exámenes.
> 2. Modularizar la app

1. Primera aproximación:

```
class Profesor:

    def __init__(self, nombre, asignatura) -> None:
        self._nombre = nombre
        self.__asignatura = asignatura
    def corregir_examenes(*examenes: tuple) -> list[Examen]: # Por lo tanto, es una SECUENCIA ITERABLE.
        #Es decir, una lista de objetos tipo examen.
        examanes_corregidos = list()
        for examen in examenes:
            examanes_corregidos.append(self.corregir_examen(examen))
        
        return examanes_corregidos
    def __corregir_examen(self, examen: Examen) -> Examen:
        import random
        examen.nota = random.random() * 10 
        return examen
```
def __corregir_examen se ha vuelto privado gracias al doble _. Es decir, los métodos también pueden hacerse "no accesibles"
2. Segunda versión:
Con list comprehension
```
def corregir_examenes(self, *examenes: tuple) -> list[Examen]:
        examanes_corregidos = list()
        #version oficial
        for examen in examenes:
            examanes_corregidos.append(self.corregir_examen(examen))
        return examanes_corregidos
    
        #alternativa
        return [self.corregir_examen(examen) for examen in examenes]    
```
3. Una tercera forma sería con un ***map***

Ejemplos:

```
examen_mates = Examen('Matematica')
examen_literatura = Examen('Literatura')
examen_ingles = Examen('English')

profe_juan = Profesor('Juan', 'Mates')


examenes_corregidos = profe_juan.corregir_examenes(examen_mates, examen_ingles)

for examen in examenes_corregidos:
    print(examen.tema, examen.nota, sep=":")
```
Resultado:

> Matematica:3.65
> English:9.01

Para crear dinámicamente las asignaturas a corregir:
```
@dataclass
class Examen:
    tema: str
    nota: float = 0.0

    @classmethod
    def crear_examen(cls, tema:str):
        return cls(tema)
```

```
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
```

Resultado:

> Matematica_1:7.16
> Literatura_2:3.65
