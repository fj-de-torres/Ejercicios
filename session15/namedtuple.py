from collections import Counter, defaultdict, namedtuple
from random import randint
from os import system
""" Cuenta = namedtuple('Cuenta',['titular','saldo'])

cuenta_pedro = Cuenta('Pedro',1800)
cuenta_pablo = Cuenta(titular='Pablo', saldo=18000)
print("-"*50)
print(cuenta_pedro, cuenta_pedro.saldo) #Algo parecido a una clase

cuentas = [
            ('Pedro',1800),
            ('Maria',1500),
            ('Julia',1300),
            ('Ramon',800)
        ]
#Para tener las cuentas nominales:

cuentas_nominales = list(map(Cuenta._make, cuentas)) """
system("cls || clear")

lista_notas = list()
for _ in range(10):
    lista_notas.append(randint(0,5))

print(lista_notas)

Estudiante = namedtuple('Estudiante',['nombre','edad','nota'])
estudiantes = [
    ('Pedro',1800,nota),
            ('Maria',18,nota),
            ('Julia',19,nota),
            ('Ramon',24,nota)
            ('Pepón',30,nota)
            ('Filemón',40,nota)
            ]
lista_estudiantes = list(map(Estudiante._make,estudiantes))
print(lista_estudiantes)
