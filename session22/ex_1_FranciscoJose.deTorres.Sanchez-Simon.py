def cadena2lista(input_str:str)->list:
    return input_str.strip(".-").split(" ")

def lista2cadena(input_list:list) -> str:
    return ",".join(input_list)

def sust_cadena(input_str:str, input_list:list)-> str:
    for palabra in input_list:
        input_str = input_str.replace(palabra,"")
    return input_str


una_cadena = "-Érase una vez..."

una_lista = cadena2lista(una_cadena)

cadena_mod = lista2cadena(una_lista)

print(cadena_mod)
print(una_lista)

cadena_final = sust_cadena(una_cadena,una_lista)

print(cadena_final)


