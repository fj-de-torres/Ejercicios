'''
Preguntar al usuario por la operación a realizar de entre +, -, *, /
Preguntar al usuario por los operandos op1, op2
Mostrar el resultado por consola según datos facilitados
'''
operando1 = float(input ("Introduzca el primer número:\n"))
operando2 = float(input ("Introduzca el segundo número:\n"))
operador = input("Elegir una operación entre +, -, *, / (¡sólo un carácter!)\n")
mensaje ="El resultado es: "
if operador == "+":
    solution = operando1 + operando2

if operador == "-":
    solution = operando1 - operando2

if operador == "*":
    solution = operando1 * operando2

if operador == "/":
    solution = operando1 / operando2

print (mensaje + "{}".format(solution))

    #print("Operación no reconocida. Fin del programa")

