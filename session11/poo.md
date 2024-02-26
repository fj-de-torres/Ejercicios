```
from gestion_alumnos.curso import Curso
from gestion_alumnos.academia import Academia
from gestion_alumnos.alumno import Alumno


if __name__ == "__main__":
    
    academia = Academia()
    
    academia.matricular_alumnos(1, Alumno(1,'Koldo','Lopez',1), Alumno(2,'Maria','Lopez',1))
    academia.matricular_alumnos(2, Alumno(1,'Marta','Perez',2), Alumno(2,'Luis','Antunez',2))
```
    
#### obtencion del segundo curso:

```
    segundo_curso = academia.obtener_curso(2)
    if segundo_curso:
        segundo_curso.listar_alumnos()

juan = Alumno(1,'Juan', '',1)
#Ahora puedo acceder a los datos de Juan:
juan.curso #(por ejemplo)
juan = Alumno(1,'Juan','',1)
print(juan.nombre) # getter
juan.nombre = 'Juanito' #setter

print(juan.nombre)
```
