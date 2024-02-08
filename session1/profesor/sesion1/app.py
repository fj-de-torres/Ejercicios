data = print("Hola Python") #statement no hay devolucion
print("Data:" + str(data))
n_items = len("Hola") # expression

# bloque de codigo
# estructura condicional

# crear una variable o declaracion de una variable y asignacion de un valor
nota = 4 #entero
a, b, c = 1, 4, 7

print(b)

if nota == 5: # ?? True (expresion booleana)
    print("estas aprobado") # indentacion
else: # sino
    print("seguir preguntando")   # indentacion
    nota = "6.7" # string o cadena

print("Fuera del bloque else")


#tipos de datos
data = 19 # int
print(type(data))

nota = 5
print(type(nota)) # float

nombre = "Amador" # str
print(type(nombre))

nombre = 'Amador' # str
print(type(nombre))

#expresion booleana
# notacion: snake
has_sacado_un_cinco = (nota == 5)
#print(type(nota == 5)) # bool
print(has_sacado_un_cinco) # False / True

# funciones embebidas o built-in
longitud_nombre = len(nombre)
print("Este nombre tiene una longitud de " + str(longitud_nombre)) # 6


# cadena_numero = int("hola") imposible conversion
# print(type(cadena_numero))

#preguntar al usuario
pregunta = "Cuantos anyos tienes?"
respuesta = int(input(pregunta))

print(f"Tienes {respuesta} anyos.")
#print("Tienes {} anyos.".format(respuesta))

if respuesta > 20:
    print("Acceso activado")
else:
    print("Entrada prohibida")
