'''
Preguntar al usuario por la operación a realizar de entre +, -, *, /
Preguntar al usuario por los operandos op1, op2
Mostrar el resultado por consola según datos facilitados
'''
import os
os.system('cls||clear')
operador = input("¿Operador? (+, -, *, /)")
#Sanitizar la entrada del usuario es tratar de filtrar posibles valores no válidos que él pueda introducir.

#Aquí ejecutaría el código para ir viendo si la cosa va bien en vez de esperar a haberlo escrito todo para no acumular posibles errores.
resultado = None #¡Ojo!: no asignar cero, porque eso podría querer decir que el resultado de una operación que no ha funcionado bien, ha dado como resultado, cero
#Sanitización: TODO
# Concepto de pertenencia a grupo o colección (con la palabra reservada in):
if operador in "+-*/":

    #Sanitizar los operandos:
    operando1 = input("¿Operando 1? ")
    if operando1.isdigit():
        operando1 = int(operando1)
    
    operando2 = input("¿Operando 2? ")
    if operando2.isdigit():
        operando2 = int(operando2)

    if type(operando1) == int and type(operando2) == int:
    #Operativa de selección de operación:

        """ if operador == "+":
            resultado = operando1 + operando2
        else:
            if operador == "-":
                resultado = operando1 - operando2
            else:
                if operador == "*":
                    resultado = operando1 * operando2
                else:
                    if operador == "/":
                        resultado = round(operando1 / operando2,2) """
        if operador == '+':
            resultado = operando1 + operando2
        elif operador == '-':
            resultado = operando1 - operando2
        elif operador == '*':
            resultado = operando1 * operando2
        elif operador == '/':
            resultado = (round(operando1 / operando2),2)
    else:
        print("Algún operando no es válido")
    #Mostrado del resultado:
                
    if resultado == None:
        print ("No se ha podido realizar la operación")
    else:
        print(f"Resultado: {resultado}")
else:
    print("Operador inválido")

