
x, y, z = 3, 5, 5

data1 = x == y # True / False

data2 = x != z 

data3 = y == z


data4 = x > y and y < z
data5 = z < x

data6 = x >= y
data7 = z <= x

data8 = 1 == 1 and 1 > 0
#print(data8)
data9 = 1 == 1 or 1 < 0


data10 = 23 > 2 or (1 > 0 and 45 > 90) or 45 > 78
#print(data10)


data11 = not((1 != 2 and 1 < 0) or 45 > 90)
#print(data11)


# bool, str, int, float, ...

a = bool(None)
if a:
    print(a)


nombre = "Francisco"
#b = nombre[len(nombre) - 1]
b = nombre[-3]
print(b)

alias = nombre[0:4] #slicing
print(f"Alias:{alias}")

nombre_completo = "Ricardo Jaume"
pos_caracter_blanco = nombre_completo.index(" ")
nombre_pila =  nombre_completo[:pos_caracter_blanco]
apellido = nombre_completo[pos_caracter_blanco + 1:]

print(f"{nombre_pila}")
print(f"{apellido}")


print(nombre_completo[-5:-10:-2])
"Ricardo Jaume"


nombre_completo[-3:-6:-1]


data20 = nombre_completo.lower()
data21 = nombre_completo.upper()

print(data20, data21)


data200 = "          Data200 Data300  Data400\n"
data200 = data200.strip()
print(data200)
data201 = "......!!          Data200 Data300  Data400\n"
data201 = data201.strip('. ?@#!').replace('Data','Datos')
print(data201)

#split
data = "100,200,300,400,500"
data_procesada = data.split(",")
print(type(data_procesada))

print(data_procesada[0])
print(data_procesada[-1])
print(data_procesada[:3])
print(len(data_procesada[:3]))


texto = "Hola, estamos en una sesion de hola Python"

c = texto.find("Hola", 4, 20)
print(c)

#d = texto.index("Java")
d = texto.find("Java")
print(d)

print(nombre_completo.endswith("e"))


print(texto.count("Hola"))


#recorrido por nombre completo
for caracter in nombre_completo:
    print(caracter)

