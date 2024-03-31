#Esto es un doc string que es necesario añadir:
"""Clases que representan la funcionalidad de transacciones monetarias"""
from os import system
from colorama import Fore, Back, Style

class Scoop():
    """Clase que representa un scoop de helado
        Otra linea
    """
    @property
    def flavor(self): #Propiedad: Es el uso público de alguno de sus atributos.
        return self.__flavor

    def __init__(self, flavor):
        self.__flavor = flavor

class Bowl():
    """Clase que representa un bowl de helado"""

    def __init__(self):
        self.scoops = []
    
    def add_scoops(self, *new_scoops):
        for scoop in new_scoops:
            self.scoops.append(scoop)

    def __repr__(self) -> str: #Se ejecutará si no está el _str__. Si está este último, ese será el que se ejecute con un print del objeto.
        return '\n'.join(s.flavor for s in self.scoops)

class A():
    def __init__(self) ->  None:
        self._data = 10 #Atributo protegido. Solo puede usarse desde la clase que hereda. No puedo hacer un b = B() y b.data

class B(A):
    def __init__(self) -> None:
        super().__init__()
        print(self._data)    

b = B()
class CustomDict(dict): #Una subclase de la clase diccioario. Es decir, una clase diccionario a la que añadiré cosas propias.
    # def __setitem__(self, key, value):
    #         print(f"Setting {key} to {value}")
    #         super().__setitem__(key, value)

    # def __getitem__(self, key):
    #     print(f"Getting {key}")
    #     return super().__getitem__(key)
    def __getitem__(self, key):
        
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass    

        return super().__getitem__(key)

system("cls || clear")

f = dict()
f['a'] = 10
print(f"{f['a'] = }")
d = CustomDict()
d['a'] = 10
print(f"{d['a'] = }")

d[1] = 20
print(f"{d[1] = }")

d = CustomDict()
d['a'] = 10
print(f"{d['a'] = }")

d[1] = 20
print(f"{d[1] = }")

#print(d['b'])


# #Instanciar (no escarciar):
# s1 = Scoop("chocolate")
# s2 = Scoop("vainilla")
# s3 = Scoop("fresa")
# bowl = Bowl()
# bowl.add_scoops(s1, s2, s3)
# print(bowl)
# #print(bowl.__repr__())

# lista = list(range(20))

# for numero in lista:
#     if numero == 5:
#         break #Esto hace que el for temrine de forma anticipada; por lo que el else no se ejecutará.
#     print(numero)
# else:
#     print("Sólo se ejecuta el else si el for se ejecuta de forma completa")