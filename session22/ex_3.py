
from os import system
import requests
from colorama import Fore, Back, Style

density_url = "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-population-density.json"
capital_url = "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-capital-city.json"
#https://github.com/samayo/country-json/blob/master/src/country-by-capital-city.json
def clear():
    system("cls || clear")

clear()
capital_response = requests.get(capital_url)
density_response = requests.get(density_url)

capital_data = capital_response.json()
#print(capital_data)

density_data = density_response.json()

#print(density_data)

personal_dic = dict()

for element in capital_data:
    for element
    #print(element)

print(personal_dic)

# dic_1 = {'a':"hola",'b':"Adios"}
# dic_2 = {'c':"Hasta luego"}
# dic_1.update(dic_2)
# print(dic_1)

