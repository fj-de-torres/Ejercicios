tupla = ('uno','dos','tres','cuatro','cinco','seis')

lista = list()

for item in tupla:
    lista.insert(len(lista),item)
lista = list(tupla)
#This doesn't work properly because the list is being iterated while it's changing internally:
# for i in lista:
#     del lista[0]

#I'd better use this option:
while lista:
    del lista[0]

#Or just the clear() method:

lista.clear()
print(lista)