# Accessing APIs:

```
import os
import requests
from colorama import Fore, Back, Style
```

For Windows users:

```
import pip._vendor.requests as requests
```

If requests is not already installed, we install it as: ***pip install requests***
Python default repositories:
   1. pypi.org
We can install as a module as well with:

***python -m pip install requests***

```
os.system("cls || clear")
url = 'https://jsonplaceholder.typicode.com/users/1'
```

Aún no es una respuesta json sino de cadenas:
response = requests.get(url)
data = response.json()
Esa *url* recibe el nombre de *endpoint*.

Otras cosas que se pueden hacer con una respuesta de una url:

```
print(response)
print(response.headers)
print(response.text)
```

### Bajar los usuarios y guardarlos en un fichero en formato csv (id, username, email, website):

```
"""This is going to be the header of the file."""
head = ['id' , 'username' , 'email' , 'website']

"""This is going to be the default file if no one is specified by the user:"""
default_file = "./data/user.csv" #Set as default path/file.csv

"""To let the user choose a file where to store the read data:"""
def fetch_url_from_user():
      file_to_open = input(Style.BRIGHT + "Please enter the url to fetch users from: " + Style.RESET_ALL)
      return file_to_open if file_to_open != ("" or None) else default_file

"""The option I choose at tme moment just for testing, is cvs_file as the default_file. Otherwise, cvs_file = fetch_url_from_user()"""
csv_file = default_file
#cvs_file = fetch_url_from_user()
def get_users (url:str):
    """
    Are they asking for the whole list or just single users? If it's a single user,
    the last character of the url string has to be a number:
    """
    multi_user = True
    if url[-1].isdigit():
          multi_user = False
    response = requests.get(url)
    data = response.json()
    return [data,multi_user]
    # print(data)
    # print(len(data))
def user_to_str(user:list) -> str:
    if user [1] == False:
        user_str = user[0][0] + "," + user[0][1] + "," + user[0][4] + "," + user[0][5] + "," + user[0][6] + "," + user[0][7]
    else:
        x = url[-1]
        user_str = user[x][0][0] + "," + user[x][0][1] + "," + user[x][0][4] + "," + user[x][0][5] + "," + user[x][0][6] + "," + user[x][0][7]

def create_csv_file(file_to_open:str):
    with open (file_to_open,'w') as file_csv:
        file_csv.write(f"{head}\n")
    #file_to_open = input("Enter name for csv file with relative path: ")
                
def append_data(json_data:str):
    first_line = None
    try: #if you don't mind
        file_to_append =open (csv_file,'r')
        if first_line == file_to_append.readlines()[0]:
            line_str = user_to_str(json_data)
        else:
            line_str = head + "\n" + user_to_str(json_data)
    except FileNotFoundError: #you'd better exist or you'll be replaced!
            create_csv_file() 


json_users = get_users('https://jsonplaceholder.typicode.com/users/1')
create_csv_file('data/user.csv')
append_data_(json_users)
```
