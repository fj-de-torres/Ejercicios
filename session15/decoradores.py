#High Order Function (HOF):
#Una función recibe como parámetro, otra función:
from os import system
from colorama import Fore, Back, Style
system("cls. || clear")
def confirm():
    key = input("Press enter: ")
    if key:
        print(Fore.YELLOW + f"going on with key '{key}'" + Fore.WHITE)
    else:
        print(Fore.YELLOW + "Continuing..." + Fore. WHITE)
    print(Fore.YELLOW + "-"*100 + Fore.WHITE)

def calcular(a,b, func):
    return func(a,b)

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b


print(calcular(10,4, sumar))
print(calcular(10,4, restar))
print("-"*70)
#Supongamos ahora(nested functions):
def convertir_valores(data):
    def procesar_1():
        return 1
    def procesar_2():
        return 0
    
    return procesar_1() + procesar_2()
#Esta es la función que decora
def procesar_siempre(fn):
    def interna():
        print('Inicio proceso')
        fn()
        print('Fin de proceso')

    return interna

@procesar_siempre
def flujo_empresarial():
    print("Se esta ejecutando un mega flujo empresarial!")

flujo_empresarial()
confirm()
@procesar_siempre
def otro_flujo_empresarial():
    print("Se esta ejecutando otro mega flujo empresarial!")

confirm()

flujo_empresarial()
otro_flujo_empresarial()

def procesar_siempre_v2(fn):
    def interna():
        print('Inicio FLUJO')
        fn()
        print('Fin de FLUJO')

    return interna

@procesar_siempre_v2
@procesar_siempre
def flujo_empresarial():
    print("Se esta ejecutando un mega flujo empresarial!")

@procesar_siempre
def otro_flujo_empresarial():
    print("Se esta ejecutando otro mega flujo empresarial!")
confirm()
flujo_empresarial()
otro_flujo_empresarial()

#Cuando la función a decorar tiene parámetros:

def procesar_siempre(f):
    def interna(*args, **kwargs):
        print('Inicio proceso')
        f(*args, **kwargs)
        print('Fin de proceso')

    return interna

@procesar_siempre
def flujo_empresarial(n: int):
    print(f"Se esta ejecutando el flujo {n} empresarial!")

@procesar_siempre
def otro_flujo_empresarial():
    print("Se esta ejecutando otro mega flujo empresarial!")

flujo_empresarial(10)
#otro_flujo_empresarial()

#Si además la función a decorar retorna argumentos:

def procesar_siempre(f):
    def interna(*args, **kwargs):
        print('Inicio proceso')
        resultado = f(*args, **kwargs)
        print('Fin de proceso')
        return resultado

    return interna

@procesar_siempre
def flujo_empresarial(n: int):
    return f"Se esta ejecutando el flujo {n} empresarial!"

@procesar_siempre
def otro_flujo_empresarial():
    print("Se esta ejecutando otro mega flujo empresarial!")

confirm()

print(flujo_empresarial(10))
#otro_flujo_empresarial()