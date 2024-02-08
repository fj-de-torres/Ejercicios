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
def check_isdigit(item:str):
    item = str(item).replace(".","")
    #print(item)
    result = True if item.isdecimal() or (item.startswith("-") and item[1:].isdecimal()) else False
    #result = True if item.isdecimal() else False
    return result        

#Function to enter data:
def insert_daily_temp ():
    def request_until_is_number(item_type: str): #I won't stop until the user enters correct input!
        item = None
        while item == None:
            item = input(f"Please, enter {item_type} temperature registered today: ")
            if check_isdigit(item):
                item = float(item)
            else:
                item = None
                print(Fore.LIGHTRED_EX + "That's not a number. Please try again" + Style.RESET_ALL)
                continue
        return item
    
    min_temp = request_until_is_number("MINIMUM")
    max_temp = request_until_is_number("MAXIMUM")
    list_daily_min_max = [min_temp,max_temp]    

    if min_temp > max_temp:
        print(Style.BRIGHT + Fore.YELLOW + "You entered them in the wrong order. No problem, I'll reverse them for you!" + Style.RESET_ALL)
        # list_daily_min_max.sort(reverse=True)
        # print(list_daily_min_max) <= No sé por qué demonios no hay un reverse de los datos a pesar de hacer esto
        min_temp = list_daily_min_max[1]
        max_temp = list_daily_min_max[0]
    return (min_temp, max_temp)
week_days = ["Mon","Tues","Wed","Thu","Fri"]
tuple_daily = []
for day in list(range(len(week_days))):
    tuple_daily [day] = insert_daily_temp()
print(tuple_daily)
""" 
tuple_daily = insert_daily_temp(min,max)
#print( tuple_daily)
semana = ["Lunes","Martes"]
temperarutas_semana = list()
for _ in range(len(semana)): # _ no me interesa el valor de la variable en cada una de las iteraciones. Sólo iterar
 """