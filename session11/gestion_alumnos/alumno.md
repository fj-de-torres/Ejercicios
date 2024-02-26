# Clase alumno:

```
class Alumno:
    #datos (atributos, estado)
    def __init__(self, indent: str, nombre: str, apellido: str, curso: int ):
        self.__identificador = indent
        self.__nombre = nombre
        self.__apellido = apellido
        self.__curso = curso
        self.__notas = []
```

## getters y setters:
#### Métodos que nos permiten acceder a las propiedades (atributos):

```
    @property    
    #Como propiedad, la nombro sin paréntesis, es decir, NO como un método.
    #GETTER:
    def nombre(self) -> str:
        return self.__nombre
 ```
#### SETTER: puedo así modificar esos atributos que he definido como ocultos):
###### No puede haber un SETTER sin un GETTER:

```
    @nombre.setter
    def nombre(self,nuevo_nombre:str):
        self.__nombre = nuevo_nombre
    #comportamiento (responsabilidad)
    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"    
    
    def estudiar(self):
        print("Estudiando...")

    def examinar(self):
        print("Examinando...")
    
    #metodo magico
    def __str__(self):
        return f"{self.__nombre} {self.__apellido}"
```

        
