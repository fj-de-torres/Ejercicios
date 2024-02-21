blocks = int(input("Ingresa el número de bloques: "))
# Escribe tu código aquí.
suma = 0
height = 0
while suma <= blocks:
    print (height)
    suma = suma + height
    print(suma)
    if suma <= blocks: height += 1
    else: 
        height -= 1
        break
    print (height)
    print ("-"*10)
    
print("La altura de la pirámide:", height)