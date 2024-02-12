def sumar(x: int, y: int) -> int:
    return x + y

def restar (x:int, y:int) -> int:
    return x - y

def sumar_v2(*numeros) -> int: # Poniendo ese * delante de numeros, se trata como tupla. Permite un nº indeterminado de parámetros de entrada.
#En otros lenguajes, esto es a lo que se le llama un *VarArgs*
    return sum(numeros) #sum es una función de Python que es un sumatorio

def sumar_v3(*numeros, otro_param:str='-') -> int: #varargs
    return sum(numeros)
