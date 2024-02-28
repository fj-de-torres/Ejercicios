from os import system
from funfont import *
system("cls || clear")

class A:
    def __init__(self,valor:int = 10) -> None:
        self._data1 = valor #protected!!
    def test(self):
        print('test_a')

    def test_publico(self):
        return "test_publico_a"
    def metodo_a(self):
        return 10
    
class B(A):
    def __init__(self,valor1:int,valor2:int):
        super().__init__(valor1)
        self._valor2 = valor2

    def test_publico(self):
        return "test_publico_b" + Fore.LIGHTMAGENTA_EX + " + " + Fore.WHITE + super().test_publico()

class C(B):

    def __init__(self, valor1: int, valor2: int):
        super().__init__(valor1, valor2)

    def test_publico(self):
        return "test_publico_c" + Fore.LIGHTMAGENTA_EX + " + " + Fore.WHITE + super().test_publico()
    def metodo_c(self):
        return super().metodo_a()
    

from colorama import Fore, Back, Style
def linea(char:str = "⸺",times:int = 50):
    print(Fore.LIGHTMAGENTA_EX + "⸠" + char*times + "﹁" + Style.RESET_ALL)

b = B(3,5)
b._data1
print(b._data1)

c = C(11,12)
linea(times=100)
print(c._data1)
# linea("—")
# print(" "*52+"︱")
# print("＿"+"｣")

# from tabulate import tabulate
# print(tabulate([["value1", "value2"], ["value3", "value4"]], ["column 1", "column 2"], tablefmt="grid"))
a =A(20)
from prettytable import PrettyTable

results = PrettyTable()
#results.add_autoindex()
results.add_column(Fore.YELLOW + "print(c._data1)" + Fore.GREEN,[Fore.CYAN + str(c._data1) + Fore.WHITE])
results.add_column(Fore.YELLOW + "print(b.test_publico())" + Fore.WHITE,[b.test_publico()])
results.add_column(Fore.YELLOW + "print(c.test_publico())" + Fore.WHITE,[c.test_publico()])
print(results)
#print(b.test_publico())
results2 = PrettyTable()
results2.add_column(Fore.YELLOW + "print(b._data1)" + Fore.WHITE,[b._data1])
results2.add_column(Fore.YELLOW + "print(b.test_publico)" + Fore.WHITE,[b.test_publico()])
results2.add_column(Fore.YELLOW + "a._data1" + Fore.WHITE,[a._data1])
results2.add_column(Fore.YELLOW + "print(b.test_publico())" + Fore.WHITE, [b.test_publico()])
linea(times=100)
print(Fore.LIGHTGREEN_EX + "Ｏｒ．．． ｗｉｔｈ Ｐｒｅｔｔｙｔａｂｌｅ：" + Fore.WHITE)
print(results2)
linea(times=10)
system("clear")

#print(columna)
