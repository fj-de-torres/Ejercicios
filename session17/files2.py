from pathlib import Path
import os
from sys import path
where_am_i = os.path.dirname(__file__)
if 'Ejercicios' in where_am_i:
    while os.path.basename(os.getcwd()) != 'Ejercicios':
        os.chdir('..')
current_path = os.getcwd()

#current_directory = os.path.basename(current_path)
path.append(current_path)
os.chdir(where_am_i)
from funfont import *
import shutil
def clear():
    os.system("cls || clear")
clear()
p = Path('data1.txt')
print(type(p))
path = p.parent.absolute()
print(path)
print("bastante",p.is_file())
print("bastante",p.is_dir())

p = Path('.')

for entrada in p.glob('*'):
    print(entrada)
    print('File:' if entrada.is_file() else 'Dir:',entrada)

base = Path('ejemplo_data')
base.mkdir(exist_ok=True)

path_b = base / 'A' / 'B' #Sumo objetos path
path_b.mkdir(parents=True, exist_ok=True)

for fichero in ('data1.txt', 'data2.txt'):
    with open(path_b / fichero, 'w') as stream:
        stream.write(f'Python ficheros {fichero}\n')

path_d = base / 'A' / 'D'

#movemos el contenido de 

#shutil.move(path_b,path_d)

data1 = path_d / 'data1.txt'
#data1.rename(path_d / 'data1_renombrado.txt')

print(data1.absolute())
print(data1.name)
print(data1.parent.absolute())

#La figura the Python que permiten usar *with*, se llama 'context manager':
#x no permite machacar el contenido. Si no existe, lo crea, pero si ya está creado, no sobreescribirá y dará error:

with open('write.txt','w') as file:
    file.write('Hola mundo')

# with open('write.txt','x') as file:
#     file.write('Hola a todo el mundo')
    
import platform
clear()
print(platform.architecture())
print(platform.version())