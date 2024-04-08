
lista1 = list(range(4))
print(len(lista1))

sumatorio = 0
for numero in lista1:
    sumatorio += numero

def obtener_datos_lazy(l:list):
    for numero in l:
        yield numero


generador = obtener_datos_lazy(lista1)
try:
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
except StopIteration:
    print("Sin mas datos")

print("_" * 50)

#for n in generador:
#    print(n)

#StopIteration



def generar_datos():
    yield 'A'
    yield from [1,2,3]
    


generadorv2 = generar_datos()
print(generadorv2.__next__())
print(generadorv2.__next__())
print(generadorv2.__next__())
print(generadorv2.__next__())
#print(generadorv2.__next__())


print([i*2 for i in  [1,2,3,4,5,6]])
data = (i*2 for i in  [1,2,3,4,5,6])

for item in data:
    print(item)

print(next(data))