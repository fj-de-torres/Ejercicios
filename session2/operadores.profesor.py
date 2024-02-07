# addition

x, y, z = 10, 23, 5 # one liner

a = x + y + z
print(f"a={a}")

# substract
b = x - y - z
print(f"b={b}")

# multiplication
c = x * y * z
print(f"c={c}")

# division
d = x / y # real, float
print(f"d={round(d, 2)}")
e = x // z # entera
print(f"e={e}")

# modulus
f = 15 % 2
print(f"f={f}")

# exponential
g = x ** y
print(f"g={g}")


# orden de ejecucion de operaciones
j = (3+1) + 4**2 * 2 #40 () => ** => * => +
print(f"j={j}")

m = 4 * 5 + 6 - 3 #23
print(f"m={m}")

"""
Preguntar al usuario por la operacion a realizar de entre +, -, *, /
Preguntar al usuario por los operadores op1, op2
Mostrar el resultado por consola segun datos facilitados
"""
# datos de entrada
operador = input("Operador? (+, -, *, /):")
#sanitizacion TODO
# pertenencia a grupo/coleccion 
if operador in "+-*/":
    #sanitizar los operandos
    operando1 = input("Operando1?:")
    if operando1.isdigit():
        operando1 = int(operando1)
    
    operando2 = input("Operando2?:")
    if operando2.isdigit():
        operando2 = int(operando2)
        
    if type(operando1) == int and type(operando2) == int:
        #operativa de seleccion de operacion
        resultado = None

        """ bloque poco eficiente / complejo
        if operador == '+':
            resultado = operando1 + operando2
        else:
            if operador == '-':
                resultado = operando1 - operando2
            else:
                if operador == '*':
                    resultado = operando1 * operando2
                else:
                    if operador == '/':
                        resultado = round(operando1 / operando2,2)
        """
        if operador == '+':
            resultado = operando1 + operando2
        elif operador == '-':
            resultado = operando1 - operando2
        elif operador == '*':
            resultado = operando1 * operando2    
        elif operador == '/':
            resultado = round(operando1 / operando2,2)
        


        #mostrado de resultados
        if resultado == None:
            print("No se ha podido realizar la operacion")
        else:
            print(f"Resultado:{resultado}")
    else:
        print("Alguno de los operandos no es mumerico")

else:
    print("Operador no permitido")












