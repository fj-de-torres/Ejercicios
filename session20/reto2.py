def find_lowest(lista_temps:list):
    return min(lista_temps)

def find_highest(lista_temps:list)->int:
    return max(lista_temps)

if __name__ == "__main__":
    temps = [85, 76, 79, 72, 81]
    lowest = find_lowest(temps)
    highest = find_highest(temps)

    print(lowest)

    print(highest)

#Correción del profesor:

def find_lowest(temperatures:list) -> list:
    #return min(temperatures)
    #Otra:
    #temperatures.sort()
    #Para que sea descentente: temperatures.sort(reverse=True)
    #lowest = temperatures[0]
    #Otra:
    sorted_temps = sorted(temperatures)
    return sorted_temps[0]