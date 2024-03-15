from collections.abc import Collection, Iterator
from abc import abstractmethod

#Colas en python:
class CustomerQueue(Collection):#ESto solo puedo hacerlo si la colección de la que heredo es abstracta.

    @abstractmethod
    def add_customer(self, customer): pass

    @property
    @abstractmethod
    def first(self): pass

class CafeQueue(CustomerQueue):

    def __init__(self):
        self._queue = []
        self._orders = {}
        self._togo = {}

    def __iter__(self):
        return Iterator_CafeQueue(self)

    def __len__(self):
        return len(self._queue)
#Nuevo método mágico: nombre in __contains__
    def __contains__(self, customer):
        return (customer in self._queue)

    def add_customer(self, customer, *orders, to_go=True):
        self._queue.append(customer)
        self._orders[customer] = tuple(orders)
        self._togo[customer] = to_go

    @property
    def first(self):
        return self._queue[0]
    
#Todo el sistema de iterador queda delegado en esta clase:
class Iterator_CafeQueue(Iterator):
    #ESto solapa al __iter__ y al __next__ de la clase que la usará:
    def __init__(self, iterable):
        self._iterable = iterable
        self._position = 0

    def __next__(self):
        if self._position >= len(self._iterable):
            raise StopIteration

        customer = self._iterable._queue[self._position]
        orders = self._iterable._orders[customer]
        togo = self._iterable._togo[customer]

        self._position += 1

        return (customer, orders, togo)

    def __iter__(self):
        return self

def serve_customers(queue):
    if not isinstance(queue, CustomerQueue):
        raise TypeError("serve_next() requires a customer queue.")

    if not len(queue):
        print("Queue is empty.")
        return

    def brew(order):
        print(f"(Making {order}...)")

    for customer, orders, to_go in queue: #destructuring aquí
        for order in orders: brew(order)
        if to_go:
            print(f"Order for {customer}!")
        else:
            print(f"(Takes order to {customer})")

if __name__ == "__name__":
    queue = CafeQueue()
    queue.add_customer('Raquel', 'double macchiato', to_go=False)
    queue.add_customer('Naomi', 'large mocha, skim')
    queue.add_customer('Anmol', 'mango lassi')

    print(f"The first person in line is {queue.first}.")
    serve_customers(queue)
    #No está funcionado pero al profesor sí le salen outputs.