# Estructura WHILE
```
import os
os.system("cls || clear")
```
```
while condición_booleana:
    Proceso 
```
###### Ejemplo:

```
contador = 1
total = 0
while contador <= 3 or total <= 10 :
    print(f"contador: {contador}",end=" ")
    print(f"total: {total}")
    total += contador
    contador += 1 # ==> contador = contador + 1
for i in range(10):
    print("-",end="-")
print()
```
Para este segundo ejemplo, he de resetear las variables iniciales:
```
contador = 1
total = 0
while contador <= 3 and total <= 10 :
    print(f"contador: {contador}",end=" ")
    print(f"total: {total}")
    total += contador
    contador += 1 # ==> contador = contador + 1
```
```
i = 0
lista = [1,2,3,4,5]
while i < 10:
    print(f"i: {i}") # Con f en print, me convierte directamente el entero en cadena para poder linkar al resto de la cadena del print.
    if lista[i] > 4:
        #break # Detiene la iteración para definitivamente
        continue #No sigo con el resto de la iteración, pero vuelvo a empezar con la siguiente.
    i += 1 #Una manera de hacer que el bucle no sea infinito; puesto que la lista llega hasta 5 y hemos puesto como condición que sea < 10. Esto siempre se va a cumplir.
```

*(Arreglar esto para que el bucle pare cuando se cumpla la condición del while. Obligatorio usar el "continue". También hacer algo equivalente la versión for.):*
```
i = -1
lista = [1,2,3,4,5]
while i < 10 and i < len(lista):
    i += 1
    print(f"i: {i}")
    if lista[i] > 4:
        #break
        continue
```

