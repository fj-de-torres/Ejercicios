# Introspección en python:
## getattr y setattr

```
class Pizza:
    def __init__(self,info:dict):
        for clave, valor in info.items():
            setattr(self, clave, valor)
```
info es la información que me permitirá crear el objeto dinámicamente. En principio será un diccionario.
Creo una instancia de pizza con unos valores concretos que yo le pase.

```
data =  {
    "nombre": "Cuatro estaciones",
    "precio": 20.0,
    "tamanyo": "Extra",
    "ingredientes": ['Atun','Tomate','Queso']
}
```
cuatro_estaciones = Pizza(data)

print(cuatro_estaciones.ingredientes, cuatro_estaciones.precio)

Resultado:

> ['Atun', 'Tomate', 'Queso'] 20.0

Y dada una determinada instancia, ¿Puedo obtener sus atributos?

```
for attr in ['nombre', 'precio','cocinero']:
    print(getattr(cuatro_estaciones, attr, 'No data'))
```
Resultado:

> ['Atun', 'Tomate', 'Queso'] 20.0
> Cuatro estaciones
> 20.0
> No data

Hay un método para evitar tener que establecer ese 'No data': *.hasattr*

```
atributos_a_borrar = ['precio', 'tamanyo']
for attr in atributos_a_borrar:
    if hasattr(cuatro_estaciones, attr):
        delattr(cuatro_estaciones, attr)

```
```
print(cuatro_estaciones.nombre)
print(cuatro_estaciones.precio)
```
Resultado:

> Cuatro estaciones
> Traceback (most recent call last):
>   File "e:\cursoPythonPCAP-PCPP1\sesion14\introspeccion.py", line 29, in <module>
>     print(cuatro_estaciones.precio)
>           ^^^^^^^^^^^^^^^^^^^^^^^^
> AttributeError: 'Pizza' object has no attribute 'precio'

#### Preguntar si una instancia es de una cierta clase:

```
class A:
    pass

class B:
    pass

a = A()
b = B()

print(isinstance(a, B))
```
Resultado:
> False

```
print(isinstance(a, A))
print(isinstance('a', int))
```
Resultado:
> True
> False

¿Eres diccionario o tupla?

```
print(isinstance([], (dict, tuple)))
```
Resultado:
> False
> False

##### ¿Qué pasaría si hubiera una relación de herencia entre ambas clases?

```
class A:
    pass

class B(A):
    pass

a = A()
b = B()

print(isinstance(a, A))
print(isinstance(b, A))
```
Resultado:

```
print(issubclass(B, A))
```
Resultado:
> True

Supongamos:
```
class A:
    pass

class B(A):
    pass

a = A()
b = B()

b = a

print(isinstance(a, A))
print(isinstance(b, B))

#print(issubclass(B, A))
```
Resultado:
> True
> True

