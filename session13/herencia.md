## Ejercicio de *herencia*

```
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

    def __init__(self, marca: str, modelo: str, anno: str, tipo_carroceria: str) -> None:
        super().__init__(marca, modelo, anno)
        self.__tipo_carroceria = tipo_carroceria

    def arrancar(self):
        return f"El coche de la marca {self._marca} esta arrancando..."
    
    def __str__(self):
        return f"{Vehiculo.__str__(self)}"
```
Supongamos que tenemos un conjunto acotado de términos (para carrocería en este caso), podemos usar la *clase enumerados*:

```

from enum import Enum

class TIPO_CARROCERIA(Enum):
    SEDAN = 1,
    BERLINA = 2,
    SUV = 3,
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
```


```
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
```
Resultado:

> Seat -- Leon -- 2021 TIPO_CARROCERIA.SEDAN
> El coche de la marca Seat esta arrancando...
> Seat -- Leon -- 2021
> Toyota -- Rav -- 2018 TIPO_CARROCERIA.TT
> El coche de la marca Toyota esta arrancando...
> Toyota -- Rav -- 2018
> Toyota -- Corolla -- 2015 Otra cosa

Para trabajar con el nº del tipo numerado:

```
if __name__ == "__main__":

    seat_leon = Automovil("Seat", "Leon", "2021", TIPO_CARROCERIA.SEDAN)
    print(seat_leon.mostrar_informacion())
    print(seat_leon.arrancar())
    print(seat_leon)
    
    toyota_rav4 = Automovil("Toyota", "Rav", "2018", TIPO_CARROCERIA.TT)
    print(toyota_rav4.mostrar_informacion())
    print(toyota_rav4.arrancar())
    print(toyota_rav4)
    
    toyota_corolla = Automovil("Toyota", "Corolla", "2015", TIPO_CARROCERIA.BERLINA)
    print(toyota_corolla.mostrar_informacion())
```
Resultado:

> Seat -- Leon -- 2021 (1,)
> El coche de la marca Seat esta arrancando...
> Seat -- Leon -- 2021
> Toyota -- Rav -- 2018 4
> El coche de la marca Toyota esta arrancando...
> Toyota -- Rav -- 2018
> Toyota -- Corolla -- 2015 2> 

##### Supongamos que tenemos una lista de coches que no queremos que se pierda:
```
coches = [seat_leon, toyota_rav4, toyota_corolla]
```
```
    import pickle

    def guardar_coches(lista_coches:list):
        with open('coches.pickle', 'wb') as file:
            pickle.dump(lista_coches, file)

```
wb: porque pickle trabaja en binario

###### Guardar coches:

```
def cargar_coches() -> list:
        data = None
        with open('coches.pickle', 'rb') as file:
            data = pickle.load(file)
        
        return data
    
    coches_cargado = cargar_coches()
    print(coches_cargado)
```
Resultado:

> Seat -- Leon -- 2021 SEDAN
> El coche de la marca Seat esta arrancando...
> Seat -- Leon -- 2021
> [<__main__.Automovil object at 0x000001CA2D069910>, <__main__.Automovil object at 0x000001CA2D069D60>, <__main__.Automovil object at 0x000001CA2D0D0410>]

```
    coches_cargado = cargar_coches()
    for coche in coches_cargado:
        print(coche)
```
Resultado:

> Seat -- Leon -- 2021 SEDAN
> El coche de la marca Seat esta arrancando...
> Seat -- Leon -- 2021
> Seat -- Leon -- 2021
> Toyota -- Rav -- 2018
> Toyota -- Corolla -- 2015

