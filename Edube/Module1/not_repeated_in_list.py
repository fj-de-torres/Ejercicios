my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temp_list = []
# Escribe tu código aquí.
for i in my_list:
    if i not in temp_list: temp_list.append(i)
    
print("La lista con elementos únicos:",temp_list)
print(my_list)
