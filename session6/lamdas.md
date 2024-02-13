# Lamda: funciones anónimas

```
def sumar(x:int, y:int) -> int:
return x + y
```
```
def cacular_algo_complejo():
return 10
```
```
lambda x, y : x + y # Equivale a lo anterior, pero de momento es una función anónima. No tiene nombre:
```
```
sumar_lambda = lambda x, y : x + y #No puedo tipar las variables x: int, y:int, etc.r1 = sumar_lambda(10,3)
r2 = sumar(10,3)print(r1 == r2)
sumar_lamda2 = lambda x, y : calcular_algo_complejo()
```

De esta manera, podría definir funciones lambda de más de una línea de código, puesto que en su única línea de código estoy invocando una función que sí que tiene más de una línea.

##### Otro ejemplo:

```
def calcular(x:int, y: int, d:dict):
proceso1 = lambda a, b :a * x + b * yres = proceso1(10,1)
```

#### Funcionalidades lambda:

Defino esta función para "descomplicar" las condiciones que impondré al *filter lambda*

```
def mayor_siete(alumno:tuple):
nota = alumno[1]
return nota > 7.0
```

##### filtrado -> filtrado: alumnos que han obtenido una nota > 7. Me devuelve una colección que cumple las condiciones del filtrado.

```
alumnos = [('maite',6.0), ('alicia', 8.0), ('luis', 7.5), ('juan',7.0)]
alumnos_mas_siete = list(filter(lambda alumno: alumno[-1] > 7.0, alumnos)) #Quiero la segunda posición, luego, lo mismo me vale [1] que [-1]
```

> Es decir, estoy aplicando una condicíon en forma de lambda. Es lo que antes se haría con un bucle for y un if.
> Tenemos que convertir a list porque el resultado del filter es un elemento *filter* que no nos sirve. Necesitamos una lista que sea el resultado de filtrar en otra *lista*

```
print(type(alumnos_mas_siete))
print(alumnos_mas_siete)
```

La condición del filtro la puedo complicar:

```
alumnos_mas_siete = list(filter(lambda alumno: alumno[1] > 7.0 and alumno[1] < 8.0 , alumnos))
print(alumnos_mas_siete)
```

Descomplico lo anterior si he definido una función a parte (mayor_siete) que será parte de la condición del filtro de la función *lambda*:

```
alumnos_mas_siete = list(filter(lambda alumno: mayor_siete(alumno) , alumnos))
print(type(alumnos_mas_siete))
print(alumnos_mas_siete)
```

#### map -> transformación: un arreglo a la función alumnos con nota x * .5 (arreglo un resultado)

Vamos a sumarle un .5 a la nota de todos los alumnos (ej: nos hemos equivocados con sus notas y les sumaremos medio punto):

```
alumnos_nota_corregida = map (lambda alumno: (alumno[0],alumno[1] + .5), alumnos) 
#Todos estos paréntesis no son opcionales. Significa que estoy creando una nueva tupla.

```

```
print(type(alumnos_nota_corregida))
print(alumnos_nota_corregida) # -> esto me da una posición de moria, no la lista que pretendo tener. Así que convierto el map a lista.
```

Las tuplas no son modificables, que es lo que estoy obteniendo; pero es que estoy creando una tupla nueva:

```
alumnos_nota_corregida = list(map (lambda alumno: (alumno[0],alumno[1] + .5), alumnos))
```

Supongamos esta función al estilo clasico:

```
def sumar_medio_punto(alumno: tuple) -> tuple:
  alumno_modificado = (alumno[0], alumno[1] + 0.5)
  return alumno_modificado
```

Aquí estoy usando la función anterior para definir la condición para el map:

```
alumnos_nota_corregida = list(map(sumar_medio_punto , alumnos))
print(type(alumnos_nota_corregida))
print(alumnos_nota_corregida)

```
