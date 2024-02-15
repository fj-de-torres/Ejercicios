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
    response = requests.get()
    data = response.json()
    # print(data)
    # print(len(data))

#Otras cosas que se pueden hacer con una respuesta de una url:

"""
print(response)
print(response.headers)
print(response.text)
 """

### Bajar los usuarios y guardarlos en un fichero en formato csv (id, username, email, website):

obtener_usuarios('https://jsonplaceholder.typicode.com/users/1')