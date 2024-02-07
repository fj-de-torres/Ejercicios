#🅻🅸🆂🆃🅰🆂:
import os
os.system("cls || clear")
# Valores booleanos = [] #lista vacía

valores_booleanos = [True, True, False, True, True, False] #Lista de elementos booleanos

#Recorrer la lista:
numero_trues = 0
numero_falses = 0
for valor_booleano in valores_booleanos:
    if valor_booleano == True:
        numero_trues = numero_trues + 1
    elif valor_booleano == False:
        numero_falses = numero_falses + 1

print(f"Numero de trues: {numero_trues}", f"Número de falses: {numero_falses}")