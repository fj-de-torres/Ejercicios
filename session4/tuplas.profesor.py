#tupla: coleccion da datos INMUTABLE

tupla1 = (1,2,3)

tupla2 = tupla1[:]
print(tupla2)

#print(id(tupla1))
#print(id(tupla2))


tupla3 = tupla2[0:2]
print(id(tupla3))
print(id(tupla2))

for item in tupla2:
    print(item)

tupla5 = 1,2,3,4,5

#print(type(tupla5))



def procesar_data() -> tuple:
    return 1,2,3

n = 1,
print(type(n))

lista_tuplas = [(1,2),(4,6),('Juan', 9), (True, False)]


