from os import system
from colorama import Fore, Back, Style
def clear():
    system("cls || clear")

class Special:
    TODAY = "Paella"

s = Special.TODAY #Para acceder al atributo HOY

clear()
menu_diario = input("¿Qué hay de menú hoy?\n\n")


match menu_diario:
    case Special.TODAY:
        print("¡Hoy hay paella!")
    case 'pizza':	
        print("Hoy hay pizza")
    case 'hamburguesa':
        print("Hoy hay hamburguesa")
    case 'ensalada' | 'sopa':
        print("Hoy hay ensalada o sopa")
    case helado if 'vainilla' in helado:
        print("Hoy hay helado de vainilla")
    case helado if helado in ['chocolate', 'fresa', 'vainilla']:
        print("Hoy hay helado de chocolate, fresa y vanilla")
    # case x if x > 10: #Por introducir otro ejemplo aunque no tenga nada que ver con el ejemplo.
    #     pass
    case 'parallevar':
        print('Hoy hay para llevar')
    case 'nada':
        print(Fore.RED + "Hoy no hay una m*****" + Fore.WHITE)
        print()
    case _: #== case exhaustivo: contempla resto de opciones.
        print("Hoy no hay paella")

class Pizza:
    def __init__(self, topping, second_toping = None):
        self.first = topping
        self.second = second_toping

pizza = Pizza('pepperoni', 'cheese')

match pizza:
    case Pizza(first='pepperoni', second='cheese'):
        print("¡Hoy hay pizza de pepperoni y queso!")
    case Pizza(first='pepperoni', second='onion'):
        print("¡Hoy hay pizza de pepperoni y cebolla!")
    case Pizza(first='pepperoni'):
        print("¡Hoy hay pizza de pepperoni!")
    case Pizza(first='hawaiana'):
        print("¡Hoy hay pizza hawaiana!")
    case _:
        print("No hay pizza hoy")

clear()
## Matchear una tupla:
order = ['tall','venti', 'no whip', 'mocha latte', 'for here']

match order:
    case ('tall', *drink, 'for here'):
        drink = ' '.join(drink)
        print(drink)
    case _:
        print("No se encontro la orden")

## Matchear una lista:
order = ['venti', 'no whip', 'mocha latte', 'for here']

match order:
    case ('tall', *drink, 'for here'):
        drink = ' '.join(drink)
        print(drink)
    case ['venti', *drink, 'for here']:
        drink = ' '.join(drink)
        print(drink)
    case _:
        print("No se encontro la orden")

## Matching de diccionario:
order = {
    'size': 'tall',
    'notes': 'no whip',
    'drink': 'mocha latte',
    'serve': 'for here'
}

match order:
    case {'size': 'tall', 'serve': 'for here', **resto}:
        drink = f"{resto['drink']} {resto['notes']}"
        print(drink)
    case _:
        print("No se encontro la orden")