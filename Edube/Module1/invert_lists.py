lista = [2,5,7,14,12,20]
print(lista)
half_len = int(len(lista)//2)
lista_0=list()
for i in range(0,half_len):
    variable_1 = lista[i]
    variable_2 = lista[i+1]
    lista[i],lista[len(lista)-1-i] = lista[len(lista)-1-i],lista[i]
print(lista)
print()
for i in lista:
    lista_0.insert(0,i)
print(lista_0)
print()
    