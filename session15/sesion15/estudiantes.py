from collections import namedtuple


Estudiante = namedtuple('Estudiante', 'nombre edad nota')

juan = Estudiante('Juan', 20, 8.5)
maria = Estudiante('Maria', 21, 6.75)
laura = Estudiante('Laura', 22, 7.5)

class Estudiantes(list):
    def calcular_promedio(self):
        return sum([est.nota for est in self]) / len(self)

estudiantes = Estudiantes([juan, maria, laura])

for estudiante in estudiantes:
    print(estudiante.nombre)

promedio_notas = estudiantes.calcular_promedio()
print("Promedio:", round(promedio_notas,2))