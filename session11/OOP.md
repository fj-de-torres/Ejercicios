# POO:
##### dominio: gestion academica


```
class Alumno:
    #datos (atributos)
    def __init__(self, indent:str, nombre:str, apellido:str, curso: int):
        self.identificador =indent #(no utilizo id porque esa es una palabra reservada)
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.notas = []
    #comportamiento (responsabilidad)
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
print(clase)
```
