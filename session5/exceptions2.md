
try:
    index = 10
    valores = [1,2,3,4,5,6]
    if index > len(valores) - 1:
        raise IndexError(f"Has superado el limite de indice posible") #El error lo lanzamos nosotros porque, mediante código, hemos considerado la opción.
except IndexError:
    print("INdice sobrepasado")
except Exception:
    print("Error general")
else:
    print("Acceso correcto")
finally:
    print("Operacion finalizada")
    valores = None #Ejemplo en el que decido borrar el contenido de la lista una vez obtenido el valor