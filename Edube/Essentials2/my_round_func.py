from math import ceil, floor
from os import system
system("cls || clear")
def my_round(number: float)-> int:
    if ceil(number) - number > number - floor(number):
        return floor(number)
    else:
        return ceil(number)
    
print(my_round(2.3))
print(my_round(2.5))
print(my_round(2.6))