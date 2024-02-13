def convertir_calificaciones(l_calificaciones: tuple) -> tuple:
    return tuple(list(map(lambda calificacion: float(calificacion), l_calificaciones)))

def preguntar_calificaciones():
    calificaciones = input("Calificaciones separadas por espacio:?")
    return tuple(calificaciones.split())

def preguntar_asignatura() -> dict:
    asignatura = input("Asignatura:?")
    calificaciones = preguntar_calificaciones()

    calificaciones_numerico = convertir_calificaciones(calificaciones)

    asignatura_calificaciones = {
        asignatura: calificaciones_numerico
    }

    return asignatura_calificaciones
    
def cargar_asignaturas(num_asignaturas: int) -> dict:
    asignaturas_local = dict() 
    for _ in range(num_asignaturas):
        par_asignatura_calificaciones = preguntar_asignatura()
        asignaturas_local.update(par_asignatura_calificaciones)

    return asignaturas_local
