

if __name__ == "__main__":
    print("Programa pricipal en ejecucion")

    # lo que no se puede hacer (definicion) con las variables
    """
    No pueden emepezar con numero
    No simbolos especiales
    nombre-y-apellido
    nombre! = ""
    SEGUNDOS.POR.MINUTO = 10
    """
    # lower snake case
    nombre_y_apellido = "Juan Lopez"

    # ctes
    PI = 3.1415
    SEGUNDOS_POR_MINUTO = 10

    '''
    Dado (pedir al usuario / input(preguta)) un nombre y apellido, 
    el programa mostrara el num. 
    de caracteres tanto del nombre com del apellido
    '''
    # peticion de datos al usuario
    nombre = input("Nombre?:")
    apellido = input("Apellido?:")

    # peticion de datos de numero de caraxcteres de nombre y apellido
    print(f"El num. de caracteres de tu nombre es {len(nombre)} y el de tu apellido es {len(apellido)}")

     

