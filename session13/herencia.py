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
