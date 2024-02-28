from os import system


class Vehiculo:

    def __init__(self,marca:str,modelo:str,anno:str) -> None:
        self._marca = marca
        self.__modelo = modelo
        self.__anno = anno

    def mostrar_informacion(self):
        return f"{self._marca} -- {self.__modelo} -- {self.__anno}"
    #Los métodos también pueden ser protegidos, públicos y privados
class Automovil(Vehiculo):

    def __init__(self,marca:str, modelo:str, anno:str, tipo_carrocerida:str):
        super().__init__(marca, modelo, anno)
        self.__tipo_carrocerida = tipo_carrocerida

    def arrancar(self):
        return f"El coche de la marca {self._marca} esta arrancando..."
    
if __name__ == "__main__":

    system("cls || clear")
    seat_leon = Automovil("Seat","Leon","2021","Sport")
    print(seat_leon.mostrar_informacion())
    print("-"*50)
    print(seat_leon.arrancar())

#### Modificación:


from enum import Enum

class TIPO_CARROCERIA(Enum):
    SEDAN = 1,
    BERLINA = 2
    SUV = 3
    TT = 4



class Vehiculo:

    def __init__(self, marca: str, modelo: str, anno: str) -> None:
        self._marca = marca
        self.__modelo = modelo
        self.__anno = anno

    def mostrar_informacion(self):
        return f"{self._marca} -- {self.__modelo} -- {self.__anno}"
    
    def __str__(self):
        return f"{self._marca} -- {self.__modelo} -- {self.__anno}"
    

class Automovil(Vehiculo):

    def __init__(self, marca: str, modelo: str, anno: str, tipo_carroceria: TIPO_CARROCERIA) -> None:
        super().__init__(marca, modelo, anno)
        self.__tipo_carroceria = tipo_carroceria

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} {self.__tipo_carroceria}"

    def arrancar(self):
        return f"El coche de la marca {self._marca} esta arrancando..."
    
    def __str__(self):
        return f"{Vehiculo.__str__(self)}"
    


if __name__ == "__main__":

    seat_leon = Automovil("Seat", "Leon", "2021", TIPO_CARROCERIA.SEDAN)
    print(seat_leon.mostrar_informacion())
    print(seat_leon.arrancar())
    print(seat_leon)

    toyota_rav4 = Automovil("Toyota", "Rav", "2018", TIPO_CARROCERIA.TT)
    print(toyota_rav4.mostrar_informacion())
    print(toyota_rav4.arrancar())
    print(toyota_rav4)

    toyota_corolla = Automovil("Toyota", "Corolla", "2015", "Otra cosa")
    print(toyota_corolla.mostrar_informacion())
    
    coches = [seat_leon, toyota_rav4, toyota_corolla]

    import pickle

    def guardar_coches(lista_coches:list):
        with open('coches.pickle', 'wb') as file:
            pickle.dump(lista_coches, file)

    #guardar_coches(coches)
    
    def cargar_coches() -> list:
        data = None
        with open('coches.pickle', 'rb') as file:
            data = pickle.load(file)
        
        return data
    
    coches_cargado = cargar_coches()
    for coche in coches_cargado:
        print(coche)