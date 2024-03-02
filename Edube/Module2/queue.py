class QueueError(IndexError):  # Eligir la clase base para la nueva excepción.
    pass
    #  Escribe código aquí.
    


class Queue:
    def __init__(self):
        #
        # Escribe código aquí.
        self.__queue =[]

    def put(self, elem):
        #
        # Escribe código aquí.
        self.__queue.insert(-1,elem)

    def get(self):
        #
        # Escribe código aquí.
        if len(self.__queue) == 0:
            raise QueueError("Error en tu colita")
        return self.__queue.pop()


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError as er:
    #print("Error de Cola")
    print(er)
#https://sl.bing.net/iAV8Wj9xEgC