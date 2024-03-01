
#Manera habitual:

lista1 = list(range(4))
print(len(lista1))

sumatorio = 0
#Todos los nºs se cargarán en memoria para poder ser sumados:
for numero in lista1:
    sumatorio += numero

#Se puede evitar con los generadores:
    
def obtener_datos_lazy():
    for numero in lista1:
        yield numero 

generador = obtener_datos_lazy()
try:
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
except StopIteration:
    print("Sin mas datos")

print("_" * 50)
print(next(generador)) #Por cada next, obtengo un nº nuevo de la lista
print(next(generador))
print(next(generador))
#Cada next recuerda dónde me he quedado en la secuencia.
print("-"*70)
for n in generador:
    print(n)
#El final de next lanza una excepción llamada StopIteration
    
def generar_datos():
    yield 'A'
    yield from [1,2,3]

generadorv2 = generar_datos()
print(generadorv2.__next__())
print(generadorv2.__next__())
print(generadorv2.__next__())
print(generadorv2.__next__())
print(generadorv2.__next__())

print([i*2 for i in  [1,2,3,4,5,6]])

#Equivalente a lo anterior con generadores:

data = (i*2 for i in [1,2,3,4,5,6])

for item in (i*2 for i in  [1,2,3,4,5,6]):
    print(item)
#No se ha cargado todo en memoria. Sólo los elementos a los que voy accediendo.
print(next(data)) #Da un StopIteration porque los datos a los que se acceden se pierden.
