def obtener_promedio_asignaturas(asignaturas: dict) -> list:
    lista_promedios = list() # lista de tuplas
    for asignatura, calificaciones in asignaturas.items():
        promedio_asignatura = calcular_promedio(calificaciones)
        lista_promedios.append((asignatura, promedio_asignatura))
    
    return lista_promedios

def calcular_promedio(lista: list) -> float:
    return round(sum(lista) / len(lista),2)