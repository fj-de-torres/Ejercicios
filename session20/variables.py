nombre = "Jaime"

def saludar():
    nombre = 'Juan'
    print("Hola, " + nombre)

saludar() #La variable local tiene prferencia.
#¿Manera de usar la global:
print(nombre)

def saludar():
    global nombre
    nombre = 'Juan'
    print("Hola,", nombre)

saludar()

print(nombre)

def order():
    eggs = 12
    
    def cook():
        nonlocal eggs # esto significa que utilizo la *global* dentro del ámbito de la función padre. Es decir, quiero eggs = 12.
        eggs = 0
    cook()
    print(eggs)

order()