#Francisco J. de Torres
"""
Dada la variable mensaje, escribir un programa que te diga cuántos
números hay en el mismo mensaje = "Carlos,10,56,Maria,90,-1,Procesar,101,Logica"
Pistas: split
"""
#programa principal:
import os
os.system('cls||clear')

if __name__=="_main__":
    pass #esta palabra no hace nada pero sirve para no dejar vacía la línea de debajo del if
mensaje = "Carlos,10,56,Maria,90,-1,Procesar,101,Logica"
nuevo_mensaje = mensaje.split(",")
#print(nuevo_mensaje,"\n")
count = 0
for i in nuevo_mensaje:

    if i.isdigit() or ( i.startswith("-") and i[1:].isdigit()): 
        #Si el nº es dígito (por ser valor positivo) o comienza por "-" y además (en ese segundo caso), lo que resta de él, es dígito (es decir, estamos ante un nº negativo); entonces al contador se le suma uno más.
        count = count + 1

print(f"Hay {count} números")
print(nuevo_mensaje)