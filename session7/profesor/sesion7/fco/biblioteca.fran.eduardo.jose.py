#Eduardo Gómez García, José Méndez Carnero y Francisco José de Torres Sánchez-Simón
"""
# *Enunciado: Biblioteca
Imagina que tienes un diccionario que almacena información sobre libros en una biblioteca. Cada clave del diccionario es el título del libro (una cadena de texto), y el valor es una tupla que contiene el nombre del autor y el año de publicación.
Tu tarea es escribir una función que reciba este diccionario y un año de publicación. La función debe retornar un nuevo diccionario con los libros  publicados después del año proporcionado. Para filtrar los libros, debes usar una función lambda dentro de tu solución.
Ayuda:
1. Repaso sobre diccionarios: Recuerda que puedes iterar sobre los ítems de un diccionario usando .items().
2. Uso de tuplas: Cada valor en el diccionario de libros es una tupla. 
Puedes acceder a sus elementos por índice, por ejemplo, tupla[0] para el nombre del autor y tupla[1] para el año de publicación.
3. Funciones lambda: Una función lambda en Python es una pequeña función anónima. Puedes usarla para crear funciones rápidas que no necesiten ser definidas con un nombre. Por ejemplo, lambda x: x * 2 es una función que duplica su entrada.
4. Filtrado con funciones lambda: Puedes combinar funciones lambda con la función filter() para filtrar elementos de una colección. Sin embargo, en este caso, como trabajamos con diccionarios, podrías usar una comprensión de diccionario con una condición que utilice la función lambda.
5. Comprensión de diccionarios: La comprensión de diccionarios te permite crear un nuevo diccionario a partir de iterar sobre un diccionario existente. La sintaxis general es {clave: valor for (clave, valor) en diccionario.items() if condición}.*
"""
import os
os.system("cls || clear")
libros = {
    "Cien años de Soledad" : ("Gabriel García Márquez", 1967),
    "1984" : ("George Orwell", 1949),
    "El Código Da Vinci" : ("Dan Brown", 2003),
    "El Principito": ("Antonio de Saint-Exupéry",1943),
    "El Quijote": ("Miguel_de_Cervantes", 1605),
}

def libros_publicados(libros: dict, filter_year:int) -> dict:
    diccionario_libros_encontrados = dict()
    lista_titulos_general = list(libros.keys())
    titulos = []
    for indice, data in enumerate(libros.values()):
        if data[1] >= filter_year:
            titulos.append(lista_titulos_general[indice])
    
    diccionario_libros_encontrados.update({filter_year : titulos})    
    return diccionario_libros_encontrados 
            



#print(list(libros.values()))
libros_pedidos = libros_publicados(libros,1900)
print(libros_pedidos)



#for indice, letra in enumerate(['a','b','c','d','e']):
#    print(indice, letra)