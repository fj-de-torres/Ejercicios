print("Hola Python")
if 5 == 5:
    print("ok")
else:
    print("No ok")
#tipos de datos:
nota = 6.7
data = 19
nombre = "Amador"
nombre2 = 'Amador'
nombreEstudiante = "Raimundo"
# print(type(data))
# print(type(nota))
# print(type(nombre),type(nombre2))
# print (type(nota == 5))
# print (type(nombreEstudiante))
# print (nota == 5)
#Funciones embebidas o built-in:
longitud_nombre = len(nombre) #snake notation
a, b, c = 1, 4, 7
print (longitud_nombre)
print (a,b,c)

print ("Este elemento tiene una longitud de " + str(longitud_nombre))
#Lo puedo volver a transformar a int:
print (type(float(str(longitud_nombre))))

#Los prints son statements. Porque son ejecuciones peron no devuelven valores
n_items= len("Hola") #Expresión. Esto sí que devuelve un valor.

# cadena_numero = int("hola") -> Imposible conversión.
#Preguntar al usuario:
pregunta = "¿Cuántos años tienes?"
respuesta = int(input(pregunta))
# print ("Tienes " + respuesta) Lo visto hasta ahora. Otra manera:
print(f"Tienes... ¡{respuesta} años!") # f de form (se verá más adelante)
print("Tienes {} años.".format(respuesta)) #Es la forma extendida (real) de lo anterior.
#print ("Tienes {} {} {} años.".format(respuesta, a ,b)) #En general.
if respuesta > 20: #Da error si respuesta no lo he convertido a numérico.
    print("Acceso activado")
else:
    print("Entrada prohibida")