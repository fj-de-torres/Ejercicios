import os
from colorama import Fore, Back, Style #I'd like to use text colours.
os.system("cls || clear") #Clear terminal every time I run this program.

"""
𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝗼 𝗱𝗲 𝗧𝗲𝗺𝗽𝗲𝗿𝗮𝘁𝘂𝗿𝗮𝘀
Imagina que estás desarrollando un programa para una estación
meteorológica. Este programa necesita registrar las temperaturas máxima y
mínima de cada día de la semana. Al final de la semana, el programa debe
ser capaz de mostrar la temperatura máxima y mínima registrada durante
la semana, además de calcular la temperatura promedio.
"""
#Function to enter data:
def insert_daily_temp (min_temp,max_temp):
    list_daily_min_max = [None,None]
    min_temp = input("Please, enter MINIMUM temperature registered today: ")
    if min_temp.isdigit() or (min_temp.lstrip(0) == "-" and min_temp(1:).isdigit()):
        max_temp = input("Please, enter MAXIMUM termperature registered today: ")
        list_daily_min_max = [min_temp,max_temp]
        if min_temp > max_temp:
            print("You entered them in the wrong order. No problem, I'll reverse them for you!")
            list_daily_min_max.sort(reverse=True)
            print(list_daily_min_max)
        min_temp = list_daily_min_max[0]
        max_temp = list_daily_min_max[1]
        return min_temp, max_temp

tuple_daily = insert_daily_temp(min,max)
#print( tuple_daily)