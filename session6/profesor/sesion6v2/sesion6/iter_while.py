
contador = 1
total = 0


while contador <= 3 or total <= 10:
    print(f"Contador:{contador}")
    print(f"Total:{total}")
    total += contador
    contador += 1

print("-" * 50)

contador = 1
total = 0


while contador <= 3 and total <= 10:
    print(f"Contador:{contador}")
    print(f"Total:{total}")
    total += contador
    contador += 1


i = 0
lista = [1,2,3,4,5]
while i < 10 and i < len(lista):
    
    if lista[i] > 4:
        print(f"i:{i}")
        #break
        continue
    
    i += 1
