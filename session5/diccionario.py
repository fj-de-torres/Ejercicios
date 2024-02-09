import os
os.system( "cls || clear")
#   DICCIONARIOS:

# Estructura compuesta de pares de clave:valor

diccio1 = dict(a=1, b=2, c=3)
# Como:
diccio1 = {
    "a":1,
    "b":2,
    "c":3
} # La clave (a,b,c), no tiene por qué ser un string. Puede ser cualquiera de los valores que existen en Python
diccio2 ={} #Otra manera de definir el diccionario, pero vacío.
diccio2 = {
    "a": 1,
    "b":2,
    "c":3,
}
#Acceso a los valores de del diccionario: a través de la clave.
print(diccio1["a"])
mensaje = diccio["f"] if "f" in diccio1 else "Esa clave no existe" #Key error cuando no existe la clave a través de la que tratamos de acceder al diccionario.
print(mensaje)

#No es una estructura ordenada porque yo puedo acceder directamente al valor que quiera nombrando su clave.

diccio1["d"] = 20 # Esto es un acceso de escritura. Estoy añadiendo
print(diccio1)
diccio1["a"] = 10 #Value update

#¿cómo procesar por loles?
new_data = {
    'h': 90,
    'm': 100,
}
diccio1.update(new_data) # Los elementos de new_data me sirver para amplicar diccio1:
print(diccio1)

#¿Cómo se recorre un diccionario?

for item in diccio1:
    print(item) #Sólo va a imprimr las claves

for item in diccio1.items():
    print(item)

for clave, valor in diccio1.items():
    print(f"Clave: {clave} Valor: {valor}")

    x,y,z = diccio2.items()
    print(x,y,z)

valores = list(diccio2.values())
print(valores)
print(type(valores))
print ("-----")
claves = list(diccio2.keys())
print(type(claves))
print(claves)

#Eliminar items:
item_eliminado = diccio2.pop("a") #elima el que elijo y me lo da como parámetro.
print(diccio2)

item_eliminado  = diccio2.popitem() #Me elimina el último valor y lo obtendo como parámetro (como en las listas)
#Vaciado del diccionario:
diccio2.clear()
print(diccio2)
del diccio2 # Lo elimina de la memoria:

#print(diccio2)

#Obtención o lectura:
valor_item = diccio1.get("a")
print(valor_item)

valor_item = diccio1.get("v",-999) # Con get, si pido algo que no existe, me duvuelve None. O puedo asignar un valor por defecto a lo que no exista. En este caso, el -999.

print(valor_item)

#dic1 = dict(a=1)

#Creación de una posible papelera:

mi_diccionario = {
    'a': 100,
    'b': 200,
    'c': 300
}

papelera = dict()
par_eliminado = mi_diccionario.popitem()
papelera.update(dict([par_eliminado]) # Convierto a dict porque lo que obtengo (par clave - valor) es una tupla. No puedo añadir tuplas a diccionarios, sino diccionarios a diccionarios. Por lo que lo convierto primero.
                
papelera.update(dict([diccio1.popitem()]))

nuevo_diccionario = dict([("a",6), ("c", 4)])
papelera.update(nuevo_diccionario)

print(papelera)
#.remove elimina el elemento elegido y duelve como resultado lo que queda. Sería una manera de devolver todos los datos del cliente (en app.py) salvo el dni, que es lo que eliminamos con 'remove'