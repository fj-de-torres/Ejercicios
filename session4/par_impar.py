import os
from colorama import Fore, Back, Style

odd_num = []
even_num = []
def num_request(num):
    num = input ("Please, write a number. To finish, press 's' key: ")
    if num % 2 == 0:
        even_num [-1] = num
    else:
        odd_num [-1] = num