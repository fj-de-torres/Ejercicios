#HOF
def calcular(a,b, func):
    return func(a,b)

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b


print(calcular(10,4, sumar))
print(calcular(10,4, restar))

print("_" * 50)

def convertir_valores(data):
    def procesar_1():
        return 1
    def procesar_2():
        return 0
    
    return procesar_1() + procesar_2()


def procesar_siempre(f):
    def interna(*args, **kwargs):
        print(f'Inicio proceso {args[0]}')
        resultado = f(*args, **kwargs)
        print(f'Fin de proceso {args[0]}')
        return resultado

    return interna

@procesar_siempre
def flujo_empresarial(n: int):
    return f"Se esta ejecutando el flujo {n} empresarial!"

@procesar_siempre
def otro_flujo_empresarial():
    print("Se esta ejecutando otro mega flujo empresarial!")

print(flujo_empresarial(10,a=1))
#otro_flujo_empresarial()
    






