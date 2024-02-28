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
```
c.test_a()
c = C()
print(c._data1)
#c.test_a() incorrecto porque test_a es privado
```
Resultado:

> No haccesible

Si hago:
```
#herencia simple multinivel
class A:
    
    def __init__(self) -> None:
        self._data1 = 10 #protected
    
    def __test_a(self):
        print('test_a')
    
    def test_publico(self):
        return "test_publico_a"

class B(A):
    def test_publico(self):
        return "test_publico_b"

class C(B):
    def test_publico(self):
        return "test_publico_c"
```
Si desde B se hace una búsqueda, como la hay, será la que utilice. Si no, se va al padre:

Resultado:

> 10
> test_publico_b
> 10
> test_publico_c
>

Ahora tomamos de la clase hija + la clase padre:
```
lass A:
    
    def __init__(self) -> None:
        self._data1 = 10 #protected
    
    def __test_a(self):
        print('test_a')
    
    def test_publico(self):
        return "test_publico_a"

class B(A):
    def test_publico(self):
        return "test_publico_b" + super().test_publico()

class C(B):
    def test_publico(self):
        return "test_publico_c"
```
```
b = B()
print(b._data1)
print(b.test_publico())

c = C()
print(c._data1)
#c.test_a() incorrecto porque test_a es privado
print(c.test_publico())
```
Resultado:

> 10
> test_publico_btest_publico_a
> 10
> test_publico_c
>

```
class A:
    
    def __init__(self) -> None:
        self._data1 = 10 #protected
    
    def __test_a(self):
        print('test_a')
    
    def test_publico(self):
        return "test_publico_a"

class B(A):
    def test_publico(self):
        return "test_publico_b" + super().test_publico()

class C(B):
    def test_publico(self):
        return "test_publico_c" + super().test_publico()
```
```
b = B()
print(b._data1)
print(b.test_publico())

c = C()
print(c._data1)
#c.test_a() incorrecto porque test_a es privado
print(c.test_publico())
```
Resultado:

> 10 E:\cursoPythonPCAP-PCPP1> 
> test_publico_btest_publico_a
> 10
> test_publico_ctest_publico_btest_publico_a

Desde la clase B puedo también, directamente, instanciar la clase A cuando instancie la B:

```
class B(A):
    
    def __init__(self, valor: int, valor2: int) -> None:
        super().__init__(valor)
```      
Aquí se instancia directamente, sin self. Es de los pocos casos (en *valor*).
```
        self.__data2 = valor2
    
    def test_publico(self):
        return "test_publico_b" + super().test_publico()

class C(B):
    def test_publico(self):
        return "test_publico_c" + super().test_publico()
    
    def metodo_c(self):
        return super().metodo_a()
```
```
b = B(10)
print(b._data1)
print(b.test_publico())
```

## Múltiple:

```
class X:
    pass
class Y:
    pass

class Z(X,Y):
    pass
```

Recordemos que sólo se heredan las partes **no privadas**.