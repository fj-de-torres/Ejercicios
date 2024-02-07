#𝕱𝖗𝖆𝖓𝖈𝖎𝖘𝖈𝖔 𝕵. 𝖉𝖊 𝕿𝖔𝖗𝖗𝖊𝖘
# Apuntes de clase
#IF TERNARIO:
import os
os.system('cls||clear')

numero = int(input("¿Número? "))

if numero % 2 == 0:
    print ("Es par")
else:
    print("Es impar")

mensaje = "Es impar" if numero % 2 != 0 else "Es par"
print (mensaje)
# Más conciso aún:

print ("Es impar" if numero % 2 != 0 else "Es par")

a = 2 if numero % 2 != 0 else 1
print (f"a: {a}")