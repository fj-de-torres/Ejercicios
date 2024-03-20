# DocStrings:
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
    >>> sumar(2,0)
    2
    >>> sumar(2,3)
    5
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

    >>> contar_vocales("murciélago")
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
        if letra in "aáeéiíoóuúü":
            total_vocales += 1
    return total_vocales
def sumar_lista_numeros(l:list) -> int:
    """
    Takes a list of integer numbers as an imput and returns the sum of all of them.
    Params:
        A list of interger numbers
    Returns:
        An integer that is the sum of all the numbers inside the list
    >>> sumar_lista_numeros([2,3,4])
    9
    """
    try:
        new_l = []
        for i in l:
            new_l.append(int(i))
    except ValueError:
        print(f"Element {i} found not to be convertible to integer")

    return sum(new_l)

#help(sumar_lista_numeros)
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #print(sumar_lista_numeros([2,3,4]))