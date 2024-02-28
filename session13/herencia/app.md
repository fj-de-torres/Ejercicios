# Herencia

## Simple:

Herencia simple multinivel:
```
class A:
    def __init__(self) -> None:
        self.__data1 = 10

class B(A):
    pass

class C(B):
    pass
```
Se ha de repartir la responsabilidad, desde más general (class A), hasta más específica.

```
b = B()
b.__data1
```
No hay acceso.
Pero un solo _ significa *protected*:
```
class A:
    
    def __init__(self) -> None:
        self._data1 = 10 #protected
```
No hacen falta establecer *getters* y *setters* porque estamos en la misma "familia":
```
b = B()
print(b._data1)
```
Resultado:

> 10
```
c = C()
print(c._data1)
```
Resultado:
> 10

Se aplica también a métodos:
```
class A:
    
    def __init__(self) -> None:
        self._data1 = 10 #protected
    
    def _test_a(self):
        print('test_a')
```


## Múltiple:

class X:
    pass
class Y:
    pass

class Z(X,Y):
    pass

Recordemos que sólo se heredan las partes **no privadas**.