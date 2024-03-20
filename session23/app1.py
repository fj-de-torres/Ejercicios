"""Modulo que contiene unas funciones operativas matematicas"""
import pydoc 
#Lo comento si no lo quiero hacer desde el código sino desde consola:
#python -m pydoc

def sumar(x: int, y: int) -> int:
    """
    Params:
        x e y son argumentos de tipo entero
    Returns:
        la suma de x e y
    
    """    
    return x + y

#pydoc.writedoc("app1")

def contar_vocales(palabra:str) ->int:
    """
    Dada una palabra, retorna el total de vocales que contiene
    :param palabra: str
    :return: int
    >>> contar_vocales("hola")
    2

    >>> contar_vocales("murcielago")
    5

    >>> contar_vocales("klmnbgtr")
    0
    """
    
    # """
    # Dada una palabra, retorna el total de vocales que contiene (formato normal)
    # """
    #Nueva clase de formato:

    total_vocales = 0
    for letra in palabra:
        #Si dentro del código hubiera algo que quizás no sea tan directo de entender, por estar basado en alguna hipótesis personal, etc, se comentaria aquí.
        if letra in "aeiou":
            total_vocales += 1
    return total_vocales

if __name__ == "__main__":
    import doctest
    doctest.testmod()