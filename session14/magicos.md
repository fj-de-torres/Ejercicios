# Métodos mágicos *(Magic Methods of Hell)*:
```
class Student:

    @property
    def grades(self):
        return self.__math + self.__history + self.__writing
```
A lo anterior se le llama *propiedad virtual*, puesto que en el property no aparece ninguna de las variables en el def, de las definidas en el __init__

```
    def __init__(self, math, history, writing):
        self.__math = math
        self.__history = history
        self.__writing = writing
```
Este método mágico me va a decir si dos instancias son iguales, aunque yo defino qué es la igualdad para mí.
Todos los objetos (variables de entrada), son tipo *object*
```
    def __eq__(self,__value:object) -> bool:
        return self.grades == estudiante.grades
```
Lo probamos:

```
juan = Student(40,60,20)
maria = Student(40,60,30)
print (juan == maria)
```
Y esa comparación *==*, activa el *método mágico* __eq__:

Resultado:
> False

Pero si igualo las notas:

```
juan = Student(40, 60, 20)
maria = Student(40, 60, 20)

print(juan == maria)
```
Resultado:
> True

Otros métodos mágicos de comparación:

```
def __gt__(self, estudiante: object):
        pass

    def __le__(self, estudiante: object):
        pass
    
    def __ne__(self, estudiante: object) -> bool:
        pass
```
```
import dataclasses

@dataclasses.dataclass
class Coche:
    matricula: str


class Parking:
    
    @property
    def coches(self):
        return self.__coches

    @coches.setter
    def coches(self, lista_coches):
        self.__coches = lista_coches

    def __init__(self) -> None:
        self.__coches = None


parking_saba = Parking()
```
Me gustaría que parking, aunque no sea una lista como tal, que pudiera ser una lista o colección al que se le puedan añadir o quitar elementos
De mommento, lo que puedo hacer para eso, es, pasarle una lista al setter:

```
parking_saba.coches = [Coche('A12'),Coche('A13'),Coche('A14')]
```
¿Puedo hacer esto?
```
for coche in parking_saba:
    print(coche)
```
No funciona. El resultado sería:

> Traceback (most recent call last):
>   File "e:\cursoPythonPCAP-PCPP1\sesion14\magicos.py", line 65, in <module>
>     for coche in parking_saba:
> TypeError: 'Parking' object is not iterable

Introducimos los métodos mágicos.
```
    def __setitem__(self, pos, item):
        self.__coches[pos] = item

    def __getitem__(self, pos):
        return self.__coches[pos]
```
Aún sabiendo que parking_saba no es un objeto iterable, como tal, si hago:
```
print(parking_saba[0])
parking_saba[0] = Coche('B50')
```
Resultado:

> Coche(matricula='B50')
> Coche(matricula='B50')
>

Eso era el getitem.
Setitem:
```
for coche in parking_saba:
    print(coche)
```
Resultado:

> Coche(matricula='A12')
> Coche(matricula='B50')
> Coche(matricula='B50')
> Coche(matricula='A13')
> Coche(matricula='A14')