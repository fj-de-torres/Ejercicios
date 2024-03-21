import os

current_path = os.getcwd()

os.chdir(f"{current_path}" + "/Edube/Essentials2")

paths= ["tree/c/other_courses/python","tree/cpp/other_courses/c","tree/cpp/other_courses/python","tree/python/other_courses/c","tree/python/other_courses/cpp"]

try:
    count = 0
    for i in paths:
        os.makedirs(i)
        count += 1
except FileExistsError:
    pass
finally:
    print(f"{count} new directory estructures created")

def isdir(dir:str)->None:
    try:
        os.chdir()
    except NotADirectoryError:
        pass
    else:
        True
        os.chdir("../")

def find(path:str,dir:str)->str:
    paths =""
    current_dir_list = os.listdir()
    if dir in current_dir_list:
        path += os.getcwd()
    else:
        for items in current_dir_list:
            if isdir(items):
                find(os.getcwd,dir)
    return paths
print()




