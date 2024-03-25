import os

current_path = os.getcwd()

os.chdir(f"{current_path}" + "/Edube/Essentials2")

paths= ["tree/c/other_courses/python","tree/cpp/other_courses/c","tree/cpp/other_courses/python","tree/python/other_courses/c","tree/python/other_courses/cpp"]

def clear():
    os.system("cls || clear")

clear()
try:
    count = 0
    for i in paths:
        os.makedirs(i)
        count += 1
except FileExistsError:
    pass
finally:
    print(f"{count} new directory estructures created")

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


def find(path:str, dir:str)->list:
    #paths_list = []
    os.chdir(path)
    #path = os.getcwd()
    dir_list = os.listdir()
    
    for item in dir_list:
        if dir in dir_list:
            path += "/" + item
            dir_list.remove(dir)

        else:
            if os.path.isdir(item):
                find(item,dir)
        
    print(path)  


find(path = "./tree",dir = "python")




