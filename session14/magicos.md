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

