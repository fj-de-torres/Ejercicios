import os
from colorama import Fore, Back, Style
def clear():
    os.system("cls || clear")
clear()
"""This sets the working path at Ejercicios moving up from where this file is located. It then prints out the working path where we are."""
where_am_i = os.path.dirname(__file__)
if 'Ejercicios' in where_am_i:
    while os.path.basename(os.getcwd()) != 'Ejercicios':
        print(os.getcwd().count('/'))
        os.chdir('..')
path = os.getcwd()

print(Fore.YELLOW + path + Fore.WHITE)
"""This prints out all the occurences of every single element of a given tuple. As an example, 'thistuple'."""
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
pos_list = list()
x = thistuple.count(8)
print(f"{x = }")
print(f"{thistuple.index(8) = }")

def num_occurences(item,tup:tuple)->int:
    
    occurences = tup.count(item)
    if occurences >= 1:
        pos = -1
        try:
            for times in range(occurences):
                
                pos = tup.index(item,pos+1)
                pos_list.append(pos)
                #tup = tup[pos + 1:]
                #num_occurences(item,tup)
            result = pos_list
        except ValueError as er:
            print(er)
    else:
        result = "Not found"

    return result
this_list = list(thistuple)
this_list.sort()

this_set = set(this_list)
for i in this_set:
    pos_list = []
    print(i,num_occurences(i,thistuple))

class EnhancedTuple(tuple):
    def __init__(self) -> None:
        super().__init__()

    def occurences(self):
        pass

my_tuple = EnhancedTuple(8,3,5)
