
# Estructuras de datos básicas:

### Listas, tuplas, diccionarios, conjuntos: BÁSICAS

##### Lista:

```
lista = list()
```

- 
  #### CRUD (Create, Read, Update and Delete):


```
del lista[pos] #La más adecuada si me dan la posición

lista.remove(elemento_en_la_lista)
```


**Estas operaciones deberían estar, por lo general, _encapsuladas_. Esto es, en forma de funciones:**

```
def borrar_elemento(pos:int, lista:list)
    del lista[pos]
```

#### Diccionarios:

```
d1 = dict()
[('a',1),('b',2)]

d2 =    {
	'c':3,
	'd':5
}
```
#### CRUD:
```
d1['a']
d1.get('a')
if resultado is not None:
```

Equivalente a:

```
if resultado:
```
Este método de obtención de elementos del diccionario dará valor None si nos estamos refiriendo a un valor que no existe.

Obteniendo sus valores:
```
for _, valor in d2.items():
    print(valor)
```
#### Conjuntos:

Set con datos:
```
conjunto1 = {1,2,3,4,5,5,5,5,}
```
Equivale a:
```
{1,2,3,4,5}
```

Se pueden recorrer los conjuntos:
for item in conjunto 1:
```
    print(item)
```
Esto no se puede hacer:
```
conjunto[0]
```
Puesto que no es ordenado. Es decir, **no es indexable.** Es decir, esto **no es una secuencia.**
Capturemos este error (se considera una mala práctica capurar errores de algo que sé que no se puede hacer). Esto sería una mala práctica, como que no sé qué son los conjuntos.

##### Operaciones sobre conjuntos:

_Iterables y secuencias:_

```
conunto.add(7)
conjunto1.discard(10)
```
La función discard no da error si trato de eliminar un elemento del conjunto que no existe.

#### Tuplas:

**Una tupla, una vez definida, _no es modificable._**
```
tupla = {1,2,3,4,5,6}
l = {(1,2),(3,5)}
```
Puedo cambiar unas tuplas por otras puesto que las listas sí que son modificables:
```
tupla = (1,2,3,4,5,6)
l = [(1,2),(3,5)]
l[0] = (4,7)
print(l)
```
Se puede recorrer la tupla (y puedo indexar):
```
for t in tupla:
    print(t)
print(tupla[0])
```
Resulado:

> 1
> 2
> 3
> 4
> 5
> 6

```
tupla2 = tupla[2:0] + (10,11)
print(tupla2)
```
El resultado es:

> (3,4,5,6.10,11)

Existen las multiplicaciones:

```
tuple3 = tupla * 3
print(tuple3)
```

#### Funciones:

Los valores por defecto siempre van **a la derecha** de los no dados por defecto:

```
def calcular(p1:int, p2:int = 0):
    return p1 * p2

calcular(1,4)
calcular(1)
calcular(p2=4,p1=1)
resultado = calcular(p2=2,p1=1)
```
#### Las funciones _lambda_:

```
lambda : print('Lambda')
```
Aunque, al definir la _lambda_, lo más habitual es que pasemos parámetros (en este caso, pasarle los parámetros a imprimir):

```
proceso = lambda x: print('Lasmda' + x)
proceso('Delta')

def calcular_valores(p1:kint;p2:int; f):
    return f(p1,p2)
```
##### HOF (High Order Funcions):
```
resultado2 = calcular_valores(1,5,lambda x, y : x + y)
resultados = list(map(lambda x: x+1, [1,2,3,4,5]))
print(resultados)
```
##### Filter:
```
resultados_filtro = list(filter(lambda( x : x > 4, [3,4,5,6,7])))
print(resultados_filtro)
```
##### List comprehension:
Algo intermedio entre un for normal y las lambda.
Puedo aplicar condicionales a la hora de generar la lista de esta manera:
```
lista_comp = [n * 2 for n in range(1,15) if n % 2 == 0]
```
Esto equivale a hacer una combinación de un **_map_** y un **_filter_**.