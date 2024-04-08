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


if __name__ == "__main__":

    semana = Semana()
    
    """ print(next(semana))
    print(next(semana))
    print(next(semana))
    print(next(semana))
    print(next(semana)) """

    iterador1 = iter(semana)
    iterador2 = iter(semana)
    
    for dia in iterador1:
        print(dia)
    print("_" * 40)
    for dia in iterador2:
        print(dia)
    print("_" * 40)
    print(next(semana))
    print("_" * 40)
    for dia in semana:
        print(dia)


    
