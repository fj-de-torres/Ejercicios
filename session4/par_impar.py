import os
from colorama import Fore, Back, Style

os.system("clear || cls")
""" def num_request():
    num = input ("Please, write a number. To finish, press 's' key: ")
    if num % 2 == 0:
        even_num [-1] = num
    else:
        odd_num [-1] = num

user_entry = num_request()
 """
odd_nums = 0
even_nums = 0
no_numerics = []
even_list =[]
odd_list = []
user_entry = input ("Please, enter a list of numbers separated by comas: ")
#print(user_entry)
print()
user_2list = user_entry.split(",")

#print(user_2list)

for list_item in user_2list:
    if list_item.isdigit() or (list_item.startswith("-") and list_item[1:].isdigit()):
        list_item =int(list_item)
        if list_item % 2 == 0:
            even_nums += list_item
            even_list.append(list_item)
        else:
            odd_nums += list_item
            odd_list.append(list_item)
    else:
        no_numerics.append(str(list_item))
        #print(no_numerics)

print(Fore.RED + Style.BRIGHT + "Attention: " + Style.NORMAL + f"Non numeric strings: " + Fore.LIGHTRED_EX + f"{no_numerics}" + Fore.RED + ", have been discarded within this list" + Style.RESET_ALL,end = "\n\n") if len(no_numerics) >= 1 else None

print("The sum of the " + Style.BRIGHT + Fore.LIGHTCYAN_EX + f"even numbers " + Style.NORMAL + Fore.WHITE + f"({even_list}) is:" + Style.BRIGHT + Fore.LIGHTCYAN_EX + f" {even_nums}" + Style.NORMAL + Fore.WHITE + ", and the sum of the " + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "odd numbers (" + Style.NORMAL + Fore.WHITE + f"{odd_list})" +  Fore.WHITE + " is " + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + f"{odd_nums}")
print()

