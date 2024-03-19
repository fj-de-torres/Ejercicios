
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

# for index, element in enumerate(capital_data):
#     print(density_data[index]["density"])
#     #print(element)

#print(personal_dic)
print("Longitud de capital_data es:",len(capital_data))
print("Longitud de density_data es:",len(density_data))

try:
    for index,_ in enumerate(capital_data):
        if capital_data[index]["country"] == density_data[index]["country"]:
            capital_data[index].update(density_data[index].items())
            #print(capital_data[index]["country"])
except IndexError:
    print(f"{capital_data[index]['country']} deleted from system")
    del capital_data[index]
finally:
    print(capital_data)
    print(len(capital_data))

#with open("countries.txt",wt) as file:




# dic_1 = {'a':"hola",'b':"Adios"}
# dic_2 = {'c':"Hasta luego"}
# dic_1.update(dic_2)
# print(dic_1)

