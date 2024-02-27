class Persona:

    @property
    def edad(self):
        return self.__edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    def __init__(self, nombre: str, edad: int) -> None:
        self.__nombre = nombre
        self.__edad = edad
    
    def __str__(self):
        return f"Nombre:{self.__nombre}, Edad:{self.__edad}"
    
    def __add__(self, persona):
        self.__edad = self.__edad + persona.edad
        self.__nombre = f"{self.__nombre} {persona.nombre}"
        return self

juan = Persona('Juan', 20)
maria = Persona('Maria', 21)

nueva_persona = juan + maria

print(nueva_persona.nombre, nueva_persona.edad, sep="**")
print("-"*20)
Resultado:

> print(nueva_persona)
> 140304156294400
> 140304156293776
> 140304156294400
> __________________________________________________
> Juan Maria**41
> __________________________________________________
> Nombre:Juan Maria, Edad:41

Otra manera para __adr__:

Instanciando una nueva Persona (como me pide el enunciado):

```
    def __add__(self, persona):
        p = Persona(f"{self.__nombre} {persona.nombre}", self.__edad + persona.edad)
        return p
```
el id de nueva_persona es diferente a cualquiera de los otros dos. No como ocurre en el caso anterior.
Resultado:

> 139677950508288
> 139677950507664
> 139677950507568
>
> __________________________________________________
> Juan Maria**41
> __________________________________________________
> Nombre:Juan Maria, Edad:41
