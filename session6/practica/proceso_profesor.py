
def convertir_calificaciones(l_calificaciones: tuple) -> tuple:
    return tuple(list(map(lambda calificacion: float(calificacion, l_calificaciones))))

def preguntar_calificaciones():
    #pass #Voy a ver a vista de pájaro todo lo que necesito antes de entrar en detalles
    calificaciones = input("Calificaciones separadas por espacios: ")
    return calificaciones.split() #Split sin un dato dentro significa que el separador es " ".
    #return tuple(calificaciones.split()) -> me puede interesar definir el tipo de dato que devuelvo
 
def preguntar_asignaturas():
    asignatura = input("¿Asignagura:? ")
    calificaciones = preguntar_calificaciones()

    calificaciones_numerico = convertir_calificaciones(calificaciones)

    asignatura_calificaciones = {
        asignatura: calificaciones_numerico()
    }
    return asignatura_calificaciones

def cargar_asignaturas(num_asignaturas: int) -> dict:
    for _ in range(num_asignaturas):
        asignaturas_local = dict()
        par_asignaura_calificaciones = preguntar_asignaturas()
        asignaturas_local.update(par_asignaura_calificaciones(calificaciones))

    return asignaturas_local