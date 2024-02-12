


def preguntar_calificaciones():
    #pass #Voy a ver a vista de pájaro todo lo que necesito antes de entrar en detalles
    calificaciones = input("Calificaciones separadas por espacios: ")
    return calificaciones.split() #Split sin un dato dentro significa que el separador es " ".

def preguntar_asignaturas():
    asignatura = input("¿Asignagura:? ")
    calificaiones = preguntar_calificaciones()

    asignatura_calificaciones = {
        asignatura: calificaciones
    }
    return asignatura_calificaciones

def cargar_asignaturas() -> dict:
    asignaturas_local = dict()
    par_asignaura_calificaiones = preguntar_asignaturas()
    asignaturas_local.update(par_asignaura_calificaiones)