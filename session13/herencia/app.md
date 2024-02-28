# Herencia

## Simple:

##### Herencia simple multinivel:
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
b = A()
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
    def __init__(self, data_x: int) -> None:
        self.__data_x = data_x

class Y:
    def __init__(self, data_y: int) -> None:
        self.__data_y = data_y

class Z(X,Y):
    def __init__(self, data_x: int, data_y: int) -> None:
        X.__init__(self, data_x)
        Y.__init__(self, data_y)
```
El primer padre en el que se busca, es X, y luego en la Y si no encuentra el método en X; porque el orden de eleccion de los padres ha sido X,Y.
Recordemos que sólo se heredan las partes **no privadas**.

```
z = Z(10,20)
print(z._data_x, z._data_y)
```
Resultado:

> 10 20

## Method resolution order:

```
print(Z.__mro__)
```
Resultado:
```
(<class ' __main__,'>, <class '__main__.X'>, <class '__main__Y>, <class 'object'>)
```
Nos indica el orden en el que se busca en las clases.

## Excepciones: Gestion de errores / situaciones excepcionales:

```
class Impresora:

    def imprimir(self, contenido: str):
        print(contenido)
```
Si la impresora se queda sin papel, debería lanzar una excepción, que no necesariamente significa un error:

```
class PapelException(Exception):
    pass

class Impresora:

    def imprimir(self, contenido: str, papel: bool = True):
        print(contenido)
```
Estoy creando una clase hija de la clase que ya existe en python llamada *Exception*

```
epson = Impresora() --> instanciación sin un __init__()
epson.imprimir('Buenos días')
```
Haciendo uso de la clase anterior para generar una excepción personalizada:

```
class PapelException(Exception):pass

class Impresora:

    def imprimir(self, contenido: str, papel: bool = True):
        if papel:
            print(contenido)
        else:
            raise PapelException("Falta papel!")
```
```
epson = Impresora()
try:
    epson.imprimir('Buenos dias', False)
except PapelException as pex:
    print(pex)
```
Resultado:

> Falta papel

## Polimorfismo:

