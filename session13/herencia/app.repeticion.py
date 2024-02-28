from os import system
system("cls || clear")

class A:
    def __init__(self) -> None:
        self._data1 = 10
    def test(self):
        print('test_a')

    def test_publico(self):
        return "test_publico_a"
    
class B(A):
    def test_publico(self):
        return "test_publico_b"

class C(B):
    def test_publico(self):
        return "test_publico_c"
    
from colorama import Fore, Back, Style
def linea(char:str = "⸺",times:int = 50):
    print(Fore.LIGHTMAGENTA_EX + "⸠" + char*times + "﹁" + Style.RESET_ALL)

b = B()
b._data1
print(b._data1)

c = C()
linea()
print(c._data1)
# linea("—")
# print(" "*52+"︱")
# print("＿"+"｣")

# from tabulate import tabulate
# print(tabulate([["value1", "value2"], ["value3", "value4"]], ["column 1", "column 2"], tablefmt="grid"))

from prettytable import PrettyTable

results = PrettyTable()
#results.add_autoindex()
results.add_column(Fore.YELLOW + "print(c._data1)" + Fore.GREEN,[Fore.CYAN + str(c._data1) + Fore.WHITE])
results.add_column(Fore.YELLOW + "print(b.test_publico())" + Fore.WHITE,[b.test_publico()])
results.add_column(Fore.YELLOW + "print(c.test_publico())" + Fore.WHITE,[c.test_publico()])
print(results)
#print(b.test_publico())