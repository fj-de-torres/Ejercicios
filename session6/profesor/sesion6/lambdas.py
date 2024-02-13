
def sumar(x: int, y: int) -> int:
    return x + y


def calcular_algo_complejo():
    return 10

#lambda - funciones anonimas
sumar_lambda = lambda x, y : calcular_algo_complejo() 

r1 = sumar_lambda(10,3)
r2 = sumar(10,3)

print(r1 == r2)

def mayor_siete(alumno: tuple) -> bool:
    nota = alumno[1]
    return nota > 7.0

alumnos = [('maite',6.0), ('alicia',8.2), ('luis',7.5), ('juan',7.0)]

def sumar_medio_punto(alumno: tuple) -> tuple:
    alumno_modificado = (alumno[0], alumno[1] + 0.5)
    return alumno_modificado

# map -> tranformacion
#alumnos_nota_corregida = list(map(lambda alumno: (alumno[0],alumno[1]+0.5) , alumnos))
alumnos_nota_corregida = list(map(sumar_medio_punto , alumnos))
print(type(alumnos_nota_corregida))
print(alumnos_nota_corregida)


# filter -> filtrado  
alumnos_mas_siete = list(filter(lambda alumno: alumno[1] > 7.0 , alumnos))
#alumnos_mas_siete = list(filter(lambda alumno: mayor_siete(alumno) , alumnos))
print(type(alumnos_mas_siete))
print(alumnos_mas_siete)






