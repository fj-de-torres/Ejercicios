from funfont import *
from os import system

class Counter():
    count = 0

    def __init__(self):
        Counter.count += 1 

    @classmethod
    def create_two(cls):
        two_counters = [cls(), cls()]
        print(f"Se han creado {cls.count} instancias")
        return two_counters


#c1 = Counter()
#c2 = Counter()
    
c1, c2 = Counter.create_two()


x, y = c1.create_two()
print(type(x), type(y))


class Receta():

    def __init__(self, patata, huevo, cebolla):
        self.__patata = patata
        self.__huevo = huevo
        self.__cebolla = cebolla
    
    @classmethod
    def receta_sin_cebolla(cls, n_papatas=2, n_huevos=4):
        return cls(n_papatas,n_huevos,0)
    
    @classmethod
    def receta_con_mas_huevo(cls):
        return cls(2,6,1)



    

primer_plato = Receta(2,4,1) #tapa estandard
tortilla_sin_cebolla = Receta.receta_sin_cebolla(n_papatas=3)
tortilla_betanzos = Receta.receta_con_mas_huevo() #betanzos


#metodos estaticos
class Tiempo_Atmosferico():
    def __init__(self, temperaturas):
        self.__temperaturas = temperaturas #farenheit

    @staticmethod
    def convert_from_faren_to_celsius(temp_f):
        calculation = round((temp_f - 32) / 1.8,2)
        return calculation

    def in_celsius(self):
        return [Tiempo_Atmosferico.convert_from_faren_to_celsius(temp) for temp in self.__temperaturas]


t_at = Tiempo_Atmosferico([56.55,45.90,68.90,32.10])
temps_celsius = t_at.in_celsius()
#print(temps_celsius)
linea_gruesa()
print_columna("print(temps_celsius)",temps_celsius)
temp_c = Tiempo_Atmosferico.convert_from_faren_to_celsius(56.55)
#print(temp_c)
print_columna("print(tem_c)",str(temp_c))

