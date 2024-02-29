# Herencia directa:

```
l = list()

class Data(list):
    def ca
```
PUedo hacer:
```
data = Data([1,2,3,4,5])
```
como:
```
l2 = [1,2,3,4]
print(data[0])
```
Resultado:
> 1
```
for numero in data:
    print(numero)
```
Creo una nueva clase de listas heredada de list() porque puedo aportar algo nuevo:
```
class Data(list):
    def calcular_promedio(self):
        return sum(self) / len(self)
```
```
promedio = data.calcular_promedio()
print("Promedio:", promedio)
```
Resultado:

> 1
> 1
> 2
> 3
> 4
> 5
> Promedio: 3.0

Esto en otros lenguajes se llaman *funciones extendidas*
