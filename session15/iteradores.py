#Iteración nomral:

for n in [1,2,3]:
    print(n)

for c in "Hola":
    print(c)
#Itera por cada línea de un texto:
for linea in open('data.txt'):
    print(linea)

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



#Esto en principio no se puede hacer porque un diccionario no es iterable.
semana = Semana()
for dia in semana:
    print(dia)

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

#Ahora sí funciona:
""" semana = Semana()
for dia in semana:
    print(dia) """

#También funciona:

print(next(semana))
print(next(semana))
print(next(semana))
print(next(semana))
print(next(semana))
print(next(semana))