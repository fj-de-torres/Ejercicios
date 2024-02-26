
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
```


