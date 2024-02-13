from proceso_profesor import cargar_asignaturas
from calculos import obtener_promedio_asignaturas
import informes

if __name__ == "__main__":
    asignaturas = None
    asignaturas = cargar_asignaturas(2)
    #debug
    #print(asignaturas)

    #obtencion de promedios
    promedios = obtener_promedio_asignaturas(asignaturas)
    #debug
    #print(promedios)

    if promedios:
        informes.mostrar_promedios_por_asignatura(promedios)