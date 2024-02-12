diccionario_general = {"Javier":"","Paco":"","Francisco":""}

def introducir_asignaturas():
    fin_asignaturas = ""

    for alumno in diccionario_general.keys():
        
        while fin_asignaturas != "s":
            asignatura, nota = (input("Introduce la asignatura "), input("Introduce la nota: "))
            fin_asignaturas = input("Introduce 's' para salir: ")
            
        
    return asignatura, nota

def introducir_calificaciones():
    pass
    #las calificaciones son tuplas de alumno - calificación
    
introducir_asignaturas()


# lista de asignaturas
# resultado_diccionario = { "alumno" : ("asignatura" : nota)}