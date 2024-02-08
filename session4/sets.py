
# Conjuntos (sets): 
#- Listas de datos NO ordenadas.
#- No admiten duplicados.

conjunto1 = set() #acabo de crear un conjunto vacío
#No permite append porque append implica adición ordenada. Pero sí add:

conjunto1.add(1)
conjunto2 ={}

print(conjunto1)
conjunto1.add(1)
print (conjunto1)
conjunto1.add(2)
print (conjunto1)
conjunto2 = {1,2,3,4,5,6,7,7,7,7,7,7}
print(conjunto2)

conjunto1.update(conjunto2)
print(conjunto1) #Python sí mantiene el orden en los conjuntos cuando són solo números. Pero en cadenas, no.

conjunto3 = {1.2,5.6,2.3,5.1,5,2}
print(conjunto3)

#Borrado de elementos:

conjunto2.remove(1)
print(conjunto2)

#Si trato de borrar un elemento que no existe, da error
#Para evitar errores de elementos inexistentes: discard

conjunto2.discard(10)
print(conjunto2)

item = conjunto2.pop()
print(item)
item = conjunto2.pop() #Me retira el primer elemento, en vez del último, como en las listas.

#OPERACIONES SOBRE CONJUNTOS:
set1 = {1,2,3}
set2 = {2,3,5}
#UNIÓN:
set3 = set1.union(set2)
print(set3) #Ojo que lo que está en ambos sólo se toma una vez.

#INTERSECCIÓN:
set3 = set1.intersection(set2)
print(set3)

set3 = set1.difference(set2)
print(set3)

