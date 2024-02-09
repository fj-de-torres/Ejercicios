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
min_weekdays = list()
max_weekdays = list()
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
    min_weekdays.append(min_temp)
    max_weekdays.append(max_temp)
    if min_temp > max_temp:
        print(Style.BRIGHT + Fore.YELLOW + "You entered them in the wrong order. No problem, I'll reverse them for you!" + Style.RESET_ALL)
        # list_daily_min_max.sort(reverse=True)
        # print(list_daily_min_max) <= No sé por qué demonios no hay un reverse de los datos a pesar de hacer esto
        min_temp = list_daily_min_max[1]
        max_temp = list_daily_min_max[0]
    return (min_temp, max_temp)
week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
temp_weekdays= list()
for day in range(len(week_days)):
    print("Enter values for " + Style.BRIGHT + f"{week_days[day]}" + Style.RESET_ALL)
    temp_weekdays.append(insert_daily_temp())
os.system ("cls || clear")
print(Style.BRIGHT + "Week temperatures are (in Celsius):")
count = 0
min_sum = 0
max_sum = 0
min_average = None
max_average = None
for day in week_days:
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX + day + Style.RESET_ALL)
    print("Min:","Max:",sep="  ")
    print(temp_weekdays[count])
    min_sum += temp_weekdays[count][0]
    max_sum += temp_weekdays[count][1]
    count += 1
min_average = round(min_sum / 5,4)
max_average = round(max_sum / 5,4)
min_week = min(min_weekdays)
max_week = max(max_weekdays)
print(Fore.LIGHTBLUE_EX + "Mininum temperature of the week: "+ Style.RESET_ALL + Style.BRIGHT + f"{min_week}" + Style.RESET_ALL)
print(Fore.LIGHTRED_EX + "Maximum temperature of the week: "+ Style.RESET_ALL + Style.BRIGHT + f"{max_week}" + Style.RESET_ALL)
print(Fore.YELLOW + "Min Average: " + Style.RESET_ALL + Style.BRIGHT + f"{min_average}" + Style.RESET_ALL)
print(Fore.YELLOW + "Max average: " + Style.RESET_ALL + Style.BRIGHT + f"{max_average}" + Style.RESET_ALL)
""" 
tuple_daily = insert_daily_temp(min,max)
#print( tuple_daily)
semana = ["Lunes","Martes"]
temperarutas_semana = list()
for _ in range(len(semana)): # _ no me interesa el valor de la variable en cada una de las iteraciones. Sólo iterar
 """