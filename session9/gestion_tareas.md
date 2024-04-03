## Función que recibe una tarea y la añade a la lista de tareas ya existente

```
def anyadir_tarea(tarea: tuple, l_tareas: list[tuple]) -> list[tuple]:
```

### Gestión de la validación de parámetros con *asertions*

    assert l_tareas is not None, "¡Lista tareas es nulo!"
    assert tarea is not None, "¡Tarea es nula!"

l_tareas.insert(0,tarea)

Con insert puedo elegir en qué posición inserto el nuevo elemento en la lista. El que está en esa posición se desplaza a la siguiente. Aquí 0 es la primera posición. Pero podemos en este caso usar un append:

    l_tareas.append(tarea)
    return l_tareas
