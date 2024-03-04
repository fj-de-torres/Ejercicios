# Strings:
## slicing, reverse slicing, index, find, strip, upper, lower, strip, replace, startswith, endswith:

import os
os.system('cls||clear')

#Recordar que puedo hacer:
x, y, z = 3, 5, 5

data1 = x == y # True / False

persona_con_hijos = False

data2 = x != z

data3 = y == z

data4 = x > y and y < z
data5 = z < x
data6 = z <= x

data7 = 1 == 1 and 1 > 0
data8 = 1 == 1 or 1 < 0

data10 = 23 > 2 or (1 > 0 and 45 > 90) or 45 > 78
print (f"data10 = {data10}")

data11 = not((1 != 2 and 1 < 0) or 45 > 90)

print (f"data11 = {data11}\n")

## Tipos de datos:
# bool, str, int, float...
#### Hay diferentes operativas para los distintos tipos de datos.

a = bool("")
print(a) # False
a = bool(0)
#print(a) # False
if not a:
    print(a)
a = bool(2)
print(a) #Todo es evaluado a True salvo las cadenas vacías, 0, None...

## STRINGS:
nombre = "Francisco"
b = nombre[len(nombre) - 1]
print(b)
b = nombre[-2]
print(b)
### Substring: tomo parte de la cadena:
alias = nombre[0:4] #slicing de una cadena
print(f"Alias de Francisco: {alias}")
nombre_completo = "Ricardo Jaume"
pos_caracter_blanco = nombre_completo.index(" ")
nombre_pila = nombre_completo[0:pos_caracter_blanco]
apellido = nombre_completo[pos_caracter_blanco + 1:]

print(f"Nombre de pila: {nombre_pila}. Apellido: {apellido}")

nombre_completo[-3:-6:-1] #-1 fuerza saltos de izquierda a derecha. Ese tercer valor en general, representa el nº de saltos desde un principio (-3) a un fin (-6)

data20 = nombre_completo.lower() #Todo en minúscula
data21 = nombre_completo.upper() #Todo en mayúscula

print(data20, data21)
data200 = "     Data200 Data300     Data400  \n"
data200 = data200.strip()
print(data200)
data200 = "...!!    Data200 Data300 Data400\n"
data200 = data200.strip('. ?@#!').replace('Data','Datos')
print(data200)
#También hay lstrip (sóle eliminar a la izda) y rstrip (sólo eliminar a la dcha.)
#Split:
data = "100,200,300,400,500"
data_procesada = data.split(",")
print(data_procesada)
print(type(data_procesada))
#primer dato de data_procesada:
print(data_procesada[0])
#Último elemento de data procesada:
print(data_procesada[-1])
#Longitud de los tres primeros elementos:
print(len(data_procesada[:3]))

texto = "Hola, estamos en una sesión de Hola python"

c = texto.find("Hola")
d = texto.find("Hola",4)
e = texto.find("Hola",4,20) #No aparece esa subcadena en el tramo deseado
print(c,d,e)
#### Con index, si la cadena buscada no existe, nos da error que termina el programa
print(nombre_completo.startswith("R"))
print(nombre_completo.startswith("F"))
print(nombre_completo.endswith("e"))

print(texto.count("Hola"))

for caracter in nombre_completo:
    print(caracter)