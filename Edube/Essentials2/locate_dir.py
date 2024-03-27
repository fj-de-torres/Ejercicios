# import os

# current_path = os.getcwd()

# os.chdir(current_path + "/Edube/Essentials2")

# paths= ["tree/c/other_courses/python","tree/cpp/other_courses/c","tree/cpp/other_courses/python","tree/python/other_courses/c","tree/python/other_courses/cpp"]

# def clear():
#     os.system("cls || clear")

# clear()
# try:
#     count = 0
#     for i in paths:
#         os.makedirs(i)
#         count += 1
# except FileExistsError:
#     pass
# finally:
#     print(f"{count} new directory estructures created")

#Hago un listado de elementos que hay en el directorio.
#¿Está *dir* en la lista?
    #Sí:
        #La añado al path: path += "/" + item.
        #Quito el *dir* de la lista
        # Para cada item:
            #Si es directorio, entro en él.
            #Vuelvo a lanzar la función *find*
    #No:
        #Para cada item:
            #Si es directorio, entro en él.
            #Vuelvo a lanzar la función *find*
# def clear():
#      os.system("cls || clear")

# def find(path:str, dir:str)->list:
#     current_path = os.getcwd()
#     path.strip('\./')
#     path = current_path + "/" + path
#     os.chdir(path)
#     #path = os.getcwd()
#     dir_list = sorted(os.listdir(),key=str.casefold)

#     for i in dir_list:
#         if not os.path.isdir(i): dir_list.remove(i)
#     counter = 0
#     if len(dir_list) != 0:
#         for item in dir_list:
#             if item == dir:
#                 result_path = os.getcwd() + "/" + item
#                 print(result_path)
#                 counter += 1
#             find(item,dir)
#     else:
#         for i in range(counter):
#             os.chdir('..')

# clear()
# find("tree","python")
## Result given by copilot:

import os

def clear():
    os.system("cls || clear")

def find(path:str, dir:str)->list:
    dir_list = sorted(os.listdir(path), key=str.casefold)
    for i in dir_list:
        full_path = os.path.join(path, i)
        if os.path.isdir(full_path):
            if i == dir:
                print(full_path)
            find(full_path, dir)
 
clear()
find("tree","python")

#TODO: Look for with semantra explanations to os.walk and os.path.join




