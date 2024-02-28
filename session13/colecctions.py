from collections import Counter, defaultdict, namedtuple
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
print("-"*50)

data = defaultdict(lambda : 0)

print(data['a'])

data ['a'] = 20

print("-"*50)

print(data['a'])

data['a'] = [1,2]
print("-"*50)
print(data['a'])

t = (1,2,3)

t[0] #,etc Que no sabemos, semánticamente, qué es.

Cuenta = namedtuple('Cuenta',['titular','saldo'])

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

cuentas_nominales = list(map(Cuenta._make, cuentas))

print("-"*50)
print(cuentas_nominales[-1].titular, cuentas_nominales[-1].saldo)
#Es decir, se hace esto: cuenta_pablo = Cuenta(titular='Pablo', saldo=18000), pero automáticamente.

from collections import deque
amigos = deque(('Rafa','María', 'Ernesto'))
amigos.append('Marcelo')
print("-"*50)
print(amigos)
amigos.appendleft('Alicia')
print("-"*50)
print(amigos)
amigos.pop()
print(amigos)
print("-"*50)
print(amigos)
amigos.popleft()
print("-"*50)
print(amigos)
print(amigos.__getattribute__