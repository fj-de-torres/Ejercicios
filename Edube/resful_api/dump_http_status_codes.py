from os import system
import requests
from colorama import Fore, Back, Style

def clear():
    system("cls || clear")

clear()
print(Fore.YELLOW + """Create a csv file with all the http status codes""" + Fore.WHITE)

with open("http_status_codes.csv","w") as file:
    for key, value in requests.codes.__dict__.items():
        file.write(f"{value}" + "," + f"{key}" + "\n")