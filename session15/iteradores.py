#Iteración normal:

for n in [1,2,3]:
    print(n)

for c in "Hola":
    print(c)
#Itera por cada línea de un texto:
try:
    for linea in open('data.txt'):
        print(linea)
except:
    pass

""" class Semana:
    def __init__(self) -> None:
        self.dias = {
            1: "Lunes",
            2: "Martes",
            3: "Miercoles",
            4: "Jueves",
            5: "Viernes",
        }

        self.index = 1



#Esto en principio no se puede hacer porque un diccionario no es iterable.
semana = Semana()
try:
    for dia in semana:
        print(dia)
except TypeError:
    pass """
#Añadimos esto a la clase:
        
class Semana:
    def __init__(self) -> None:
        self.dias = {
            1: "Lunes",
            2: "Martes",
            3: "Miercoles",
            4: "Jueves",
            5: "Viernes",
        }

        self.index = 1

    def __iter__(self):
        self.index = 1
        return self
    
    def __next__(self):
        if self.index < 1 | self.index > 5:
            raise StopIteration
        else:
            data = self.dias[self.index] 
            self.index += 1
            return data

#Ahora sí funciona:
semana = Semana()
counter = 0
for dia in semana:
    try:
        print(f"semna.index is: {semana.index}")
        print(dia)
        #print(f"semna.index is: {semana.index}")
    except StopIteration:
        print("Ya no hay más días de la semana")
    finally:
        print(f"counter: {counter}")
        counter += 1

#También funciona:

""" print(next(semana))
print(next(semana))
print(next(semana))
print(next(semana))
print(next(semana))
print(next(semana)) """
semana = Semana()
counter = 0
for _ in range(6):
    try:
        print(next(semana))
        print(f"counter: {counter}")
        counter += 1
    except StopIteration:
        print(f"Counter value that broke it down was: {counter}")