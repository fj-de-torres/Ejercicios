import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

def encode_obj(obj):
    if isinstance(obj, Person):
        return {"type": "Person", "name": obj.name, "age": obj.age}
    elif isinstance(obj, Pet):
        return {"type": "Pet", "name": obj.name, "species": obj.species}
    elif isinstance(obj,Persona):
        return {"type": "Persona","nombre" : obj.nombre, "edad" : obj.edad, "macho_alfa" : obj.macho_alfa}
    else:
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

alice = Person('Alice', 30)
fluffy = Pet('Fluffy', 'Cat')

print(json.dumps(alice, default=encode_obj))  # Outputs: {"type": "Person", "name": "Alice", "age": 30}
print(json.dumps(fluffy, default=encode_obj))  # Outputs: {"type": "Pet", "name": "Fluffy", "species": "Cat"}
class Persona:
    def __init__(self,nombre:str, edad:int, macho_alfa:bool = False) -> None:
        self.nombre = nombre
        self.edad = edad
        self.macho_alfa = True

pedro = Persona("Pedro",49,True)

print(json.dumps(pedro,default=encode_obj))