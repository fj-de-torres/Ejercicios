def anyadir_tarea(tarea: tuple, l_tareas: list[tuple]) -> list[tuple]:
    """Recibe una tarea y la añade a la lista de tareas ya existente"""
    #validacion de los parametros de entrada
    assert l_tareas is not None, "Lista tareas es nulo!"
    assert tarea is not None, "Tarea es nula!"

    l_tareas.append(tarea)

    return l_tareas


def entrada_valida(cadena: str):
    return type(cadena) == str




