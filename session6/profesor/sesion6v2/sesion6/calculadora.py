def sumar(x: int, y: int) -> int:
    return x + y

def sumar_v2(*numeros, otro_param:str='*') -> int: #varargs
    print(otro_param * 60)
    return sum(numeros)


def restar(x: int, y: int) -> int:
    return x - y
