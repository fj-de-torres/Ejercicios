import os, sys

"""
os.system("cls || clear")
print("Todo correcto")
print(__name__) """
#print(module.counter)
from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))
for p in sys.path:
    print(p)
