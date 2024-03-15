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