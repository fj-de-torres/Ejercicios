from os import system
system(" cls || clear")
#------------ class definitions: ---------------------------------------------
class Vehiculo:

    @property
    def marca(self):
        return self.__marca
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def anno(self):
        return self.__anno
    
    def __init__(self,marca:str,modelo:str,anno:str):
        self.__marca = marca
        self.__modelo = modelo
        self.__anno = anno
    
    def __str__(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__anno}"
    
    def mostrar_informacion(self):
         
        return self.__str__()
        

class Automovil(Vehiculo):

    def __init__(self,tipo_carroceria:str):
        Vehiculo.__init__(self._marca,self._modelo,self.__anno)
        self.__tipo_carroceria = tipo_carroceria

    def arracancar(self):
        print("El coche está arrancando")
    
    def mostrar_informacion(self):
        return super().mostrar_informacion() + self.__tipo_carroceria


#-----------------------------------------------------------------------
def linea(charac:str = "-",times: int = 80):
    print(charac*times)


seat = Vehiculo("Seat","León","2000")
print(seat)
linea()
print(seat.mostrar_informacion())
linea()
Automovil_seat = Automovil("Metalizada")
linea()