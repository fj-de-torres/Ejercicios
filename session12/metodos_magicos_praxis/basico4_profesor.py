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
        #self.__edad = self.__edad + persona.edad
        #self.__nombre = f"{self.__nombre} {persona.nombre}"
        #return self
        p = Persona(f"{self.__nombre} {persona.nombre}", self.__edad + persona.edad)
        return p
    

juan = Persona('Juan', 20)
maria = Persona('Maria', 21)

print(id(juan))
print(id(maria))
nueva_persona = juan + maria
print(id(nueva_persona))
print("_" * 50)
print(nueva_persona.nombre, nueva_persona.edad, sep="**")
print("_" * 50)
print(nueva_persona)
