# Accessing APIs:
import os
import requests
#For Windows users:
""" 
import pip._vendor.requests as requests
 """

#If requests is not already installed, we install it as: ***pip install requests***
#Python default repositories:
#   1. pypi.org
#We can install as a module as well with:
os.system("cls || clear")
""" 
***python -m pip install requests***
"""
#Aún no es una respuesta json sino de cadenas:
def obtener_usuarios (url:str):
    response = requests.get(url)
    data = response.json()
    return data
    # print(data)
    # print(len(data))

#Otras cosas que se pueden hacer con una respuesta de una url:

"""
print(response)
print(response.headers)
print(response.text)
 """

### Bajar los usuarios y guardarlos en un fichero en formato csv (id, username, email, website):

def create_csv(file_to_open:str):
    head = ['id' , 'username' , 'email' , 'website']
    #file_to_open = input("Enter name for csv file with relative path: ")
    first_line = None
    with open (file_to_open,'r') as file_csv:
        first_line = file_csv.readlines()[0]

    if first_line != head:
        with open (file_to_open,'w') as file_csv:
            file_csv.write(f"{head}\n")

print(obtener_usuarios('https://jsonplaceholder.typicode.com/users/1'))
create_csv('data/user.csv')


