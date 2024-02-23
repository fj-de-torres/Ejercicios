from time import sleep
def division():
    try:
        x = int(input("Ingresa un numero: "))
        y = 1 / x
        print(y)
    except ZeroDivisionError:
        print("No puedes dividir entre cero, lo siento.")
    except ValueError:
        print("Debes ingresar un valor entero.")
    except KeyboardInterrupt:
        print("¡Vamos, no me jodas!")
        sleep(1)
        division()
    except:
        print("Oh cielos, algo salió mal...")
division()
print("FIN.")
