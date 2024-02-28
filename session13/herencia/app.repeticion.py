from os import system
system("cls || clear")

class A:
    def __init__(self) -> None:
        self._data1 = 10

class B:
    pass

class C:
    ...

b = A()
b._data1
print(b._data1)