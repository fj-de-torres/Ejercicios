import threading

def proceso1():
    for i in range(10):
        print("Proceso 1")


def proceso2():
    for i in range(10):
        print("Proceso 2")

def proceso3():
    for i in range(10):
        print("Proceso 3")

#Procesos lineales:
        
#proceso1()
#proceso2()
#proceso3()
t1 = threading.Thread(target=proceso1)
t2 = threading.Thread(target=proceso2)
t3 = threading.Thread(target=proceso3)
#No se puede start más de una vez.

t1.start()
t2.start()
t3.start()

#Al programa principal: no finalices hasta que no finalicen los threats
t1.join()
t2.join()
t3.join()

print("Final de programa") #Aquí termina el programa pero los hijos siguen en ejecución

#Así forzamos la secuencialidad del los hilos:

t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
t3.join()

print("Final de programa")
