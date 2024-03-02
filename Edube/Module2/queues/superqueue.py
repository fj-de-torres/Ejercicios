from os import system
from sys import path
path.append("/home/francisco/Documents/Learning/PUE/Python/Ejercicios/")
from funfont import *
from colorama import Fore,Back, Style

class QueueError(IndexError):
    def __init__(self, message = "Queue operation failed") -> None:
        self.message = message
        super().__init__(self.message)

class QueueEmptyError(IndexError):
        def __init__(self, message = "Error: queue is empty") -> None:
            super().__init__(self.message)
class Queue:
    def __init__(self) -> None:
        self.queue_list = []
    
    def put(self,item):
        self.queue_list.insert(0,item)

    def get(self):
        if len(self.queue_list) == 0:
            raise QueueError(Fore.YELLOW + f"Error: you cannot pop items form an empty list" + Fore.WHITE)
        return self.queue_list.pop()

    def __str__(self) -> str:
        return f"{self.queue_list}"

class SuperQueue(Queue):
    def __init__(self) -> None:
        super().__init__()
    
    def isempty(self)-> bool:
       return len(self.queue_list) == 0

system("cls || clear")

que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    print_columna("que",que)
    print("que.__dict__",que.__dict__)
    if not que.isempty():
        print(que.get())
    else:
        print_columna("Mensaje final","Cola vacía")

# queue = Queue()
# [ queue.put(i) for i in range(1,11)]

# print(type(queue))
# print(queue)