import os
from file_management import *
from colorama import Fore,Back,Style

os.system("cls || clear")

file_reading_message =Style.BRIGHT + "Tasks on your list at this point are: " + Style.NORMAL + "\n"

tareas = lectura_fichero("tareas.txt")
if len(tareas) == 0:
     tareas_list = Fore.RED + "None!" + Style.RESET_ALL
else:
     tareas_list = tareas
print(file_reading_message + f"{tareas_list}")


