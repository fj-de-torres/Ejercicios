cantidad = 12

if cantidad == 7 + 5:
    print ("OK")

#Asignación en plena comparación:
if (cantidad := 7 + 5) == 12:
    print("OK")

print(cantidad)

#O incluso una función dentro:

def procesar (a,b):
    return a + b #Es decir, puede ser el resultado de algo complejo

if (cantidad := procesar(7,5)) == 12:
    print("OK")
print(cantidad)