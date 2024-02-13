def calcular_promedio_asignatura(asignaturas:dict) -> list:
    lista_promedios = list() #Quiero crear una lista de tuplas como resultado
    for asignatura, calificaciones in asignaturas.items():
        promedio_asignatura = calcular_promedio_por_asignatura(calificaciones)
        lista_promedios.append(asignatura,promedio_asignatura)
    return lista_promedios

def calcular_promedio(lista:list) -> float: #No especifico en el nombre que sea lista de asignaturas porque me puede venir bien esta función para el promedio de cualquier otra cosa.
    return sum(lista) / len(lista)