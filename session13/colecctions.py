from collections import Counter, defaultdict
from os import system

system("cls || clear")

list_notas = [7.5, 8.3,9.0,8.3,7.0,7.5]
#¿Cuántas veces ha ocurrido que un alumno ha llamado
contador_notas = Counter(list_notas)
print(contador_notas)
#Y ordena de mayor a menor nº de apaiciones
print("-"*50)
print(contador_notas[7.5])

#Con la indexación directa, si pido un elemento que no existe, me daría error.