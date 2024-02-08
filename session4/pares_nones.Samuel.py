# PAR E IMPAR
import os
os.system("cls || clear")

def tratar_numero(lista_numeros, elemento):
    lista_numeros.append(elemento)
    return lista_numeros, sum(lista_numeros)


# 0. Programa principal
if __name__ == "__main__":
    pass

    # 1. Introducir datos
    mensaje = input("Por favor, ingresa la lista de números:  ")

    # 2. Transformar string grande a lista de strings (separador = ",")
    lista_nums = mensaje.split(",")

    # 3. Creacion listas, variables y contadores
    lista_pares = []
    lista_impares = []

    suma_pares = 0
    suma_impares = 0
    
    cant_pares = 0 # Inicializar contador pares 
    cant_impares = 0 # Inicializar contador números 

    for elemento_original in lista_nums:
        
        # 3.1 Quitar signo negativo para que isdigit() lo reconozca. Si es otra cosa no interesa y no se tiene en cuenta.
        elemento_sin_signo = elemento_original.lstrip("-")
        

        # 3.2 Elemento actual == número => aumentar contador
        if elemento_sin_signo.isdigit():
            
            elemento = int(elemento_original) # Cambio de str a int para operaciones

            if elemento % 2 == 0:
                cant_pares = cant_pares + 1
                #suma_pares = suma_pares + elemento
                #lista_pares.append(elemento) # Guardar elemento par
                lista_pares, suma_pares = tratar_numero(lista_pares, elemento)
                #COMP_VISUAL: print(f"Par: {elemento}")
            else:
                cant_impares = cant_impares + 1
                #suma_impares = suma_impares + elemento
                #lista_impares.append(elemento) # Guardar elemento impar
                lista_impares, suma_impares = tratar_numero(lista_impares, elemento)
                #COMP_VISUAL: print(f"Impar: {elemento}")  


    # 4. Sacar por pantalla resultado
    print(f"En el mensaje <{mensaje}> hay estos pares ({lista_pares}) y estos impares ({lista_impares}).")
    print(f"Los pares suman {suma_pares} y los impares suman {suma_impares}")
