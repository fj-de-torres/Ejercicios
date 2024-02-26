# POO:
##### dominio: gestion academica
```
from gestion_alumnos.crud import *

class Curso:
    
    def __init__(self, numero, tutor): -> None:
        self.alumnos = list()
        self.numero = numero
        self.tutor = tutor

    def realizar_examen(l_alumnos:list[Alumno]):
        for alumno in l_alumnos:
            alumno.examinar()
```


```
class Alumno:
    #datos (atributos)
    def __init__(self, indent:str, nombre:str, apellido:str, curso: int):
        self.identificador =indent #(no utilizo id porque esa es una palabra reservada)
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.notas = []
```
##### comportamiento (responsabilidad):
```
    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"
    def estudiar(self):
        print("Estudiando...")

    def examinar(self):
        print("Examinanddo...")
#### Método mágico:
```
        def __str__(self):
            return f"{self.nombre} {self.apellido}"
        #O bien:
            obtener_nombre_completo(self)
print()
```

##### RD - Lista de alumnos:
```
juan = Alumno(1, 'Juan', 'Perez',1) #instaciar
clase = [juan, Alumno(2,'Maria','Pelaez',1)]
```
##### CRUD:

```
def matricular(indent:int, nombre: str, apellido:str, curso:str, l_alumnos:list):
    l_alumnos.append(Alumno(indent,nombre, apellido, curso))

matricular (3,'Koldo','Lopez',1,clase)

mostrar_alumnos(curso)

print("_"* 40)

matricular(1, 'Maria','Lopex',1, curso)

print(clase)
```
Me creo una carpeta "package". Si en esta carpepta pongo un archivo llamado: __init__.py, esta carpeta se convierte en un package. Dentro de ella, pondré módulo.

### Nueva versión:

```

if __name__ == "__main__":
    
    academia = Academia()
    curso = Curso(1, 'Luis Garcia')

    academia.matricular_alumnos(curso, Alumno(1,'Koldo','Lopez',1), Alumno(2,'Maria','Lopez',1))
    
    mostrar_alumnos(curso)
    print("_" * 40)
    matricular(1,'Maria','Lopez',1, curso)
    mostrar_alumnos(curso)

    curso.realizar_examen()
```
