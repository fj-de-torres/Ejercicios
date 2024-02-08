import os
from colorama import Fore, Back, Style

os.system("clear || cls")
odd_nums = []
even_nums = []

""" def num_request():
    num = input ("Please, write a number. To finish, press 's' key: ")
    if num % 2 == 0:
        even_num [-1] = num
    else:
        odd_num [-1] = num

user_entry = num_request()
 """
user_entry = input ("Please, enter a list of numbers separated by comas: ")
print(user_entry)

user_converted_list = user_entry.split(",")
print(user_converted_list)

for list_num in user_converted_list:
    if list_num % 2 == 0:
        even_nums += even_nums
    else:
        odd_nums += odd_nums
print(f"The sum of the even numbers is: {even_nums}, and the sum of the odd numbers is {odd_nums}")

