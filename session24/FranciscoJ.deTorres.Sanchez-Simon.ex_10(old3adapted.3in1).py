#Francisco José de Torres Sánchez-Simón
#Aprovecho el ejercicio 3 de paises porque obtuve los datos desde un archivo json en internet, según una consulta que te hice en clase:

from os import system, getcwd, listdir, chdir
import requests
from colorama import Fore, Back, Style
from prettytable import PrettyTable

density_url = "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-population-density.json"
capital_url = "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-capital-city.json"
#https://github.com/samayo/country-json/blob/master/src/country-by-capital-city.json
def clear():
    system("cls || clear")
try:
    clear()
    capital_response = requests.get(capital_url)
    density_response = requests.get(density_url)

    capital_data = capital_response.json()
    #print(capital_data)

    density_data = density_response.json()

    #print(density_data)

    # personal_dic = dict()
    personal_list = []

    print("Longitud de capital_data es:",len(capital_data))
    print("Longitud de density_data es:",len(density_data))

    capitals_dict = {item['country']:item for item in capital_data}
    densities_dict = {item['country']:item for item in density_data}



    #print(capitals_dict)
    #print(densities_dict)

    for country, capital_item in capitals_dict.items():
        personal_dict = {}
        if country in densities_dict:
            personal_dict.update(capital_item)
            personal_dict.update(densities_dict[country])
            personal_list.append(personal_dict)

    #print(personal_list)


    header_list = []

    for key in personal_list[0].keys():
        header_list.append(Fore.YELLOW + f"{key}"+Fore.WHITE)
    #columna.add_autoindex("Country nº")
    #print(header_list)    
    columna = PrettyTable(header_list)
    count = 0
    for count,item in enumerate(personal_list):
        count 
        row = []
        for value in item.values():
            row.append(value)
        columna.add_row(row)

    def write_on_csv(message="Data written on file succesfully"):
        # current_path= getcwd()
        # chdir(f"{current_path}"+"/session24")
        try:
            with open("countries.csv","wt") as csv_file:
                csv_file.write("country,city,density\n")
                for dictionaries in personal_list:
                    data_tmp_list = []
                    for key in dictionaries.values():
                        data_tmp_list.append(str(key))
                    csv_file.write(",".join(data_tmp_list)+"\n")
            print(message)
        except:
            message = "Problem writting on file"
        return message
    print(columna)
    print(count)

#print(personal_list)

#Pequeñas pruebas porque no tenía claro el concepto:
# dic_1 = {'a':"hola",'b':"Adios"}
# dic_2 = {'c':"Hasta luego"}
# dic_1.update(dic_2)
# print(dic_1)

    write_on_csv("")
except KeyboardInterrupt:
    print(Fore.RED + "KeyboardInterruputs")