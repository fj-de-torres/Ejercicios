"""
Tu tarea es implementar una clase llamada Weeker. Sí, tus ojos no te engañan, este nombre proviene del hecho de que los objetos de esta clase podrán almacenar y manipular los días de la semana.

El constructor de la clase acepta un argumento: una cadena. La cadena representa el nombre del día de la semana y los únicos valores aceptables deben provenir del siguiente conjunto:

Lun Mar Mie Jue Vie Sab Dom

Invocar al constructor con un argumento desde fuera de este conjunto debería generar la excepción WeekDayError (defínela tu mismo; no te preocupes, pronto hablaremos sobre la naturaleza objetiva de las excepciones). La clase debe proporcionar las siguientes facilidades:

    Los objetos de la clase deben ser "imprimibles", es decir, deben poder convertirse implícitamente en cadenas de la misma forma que los argumentos del constructor.
    La clase debe estar equipada con métodos de un parámetro llamados add_days(n) y subtract_days(n), siendo n un número entero que actualiza el día de la semana almacenado dentro del objeto mediante el número de días indicado, hacia adelante o hacia atrás.
    Todas las propiedades del objeto deben ser privadas.

Completa la plantilla que te proporcionamos en el editor, ejecuta su código y verifica si tu salida se ve igual que la nuestra.
Salida Esperada

Lun
Mar
Dom
Lo siento, no puedo atender tu solicitud.
"""
from os import system
from collections import namedtuple

class WeekDayError(Exception):
    pass

class Weeker:

    @property
    def num_dia(self):
        return self.__num_dia
    
    @property
    def dias_semana(self):
        return self.__dias_semana
    @property
    def dia_semana(self):
        return self.__dia_semana

    __dias_semana =('Lun','Mar','Mie','Jue','Vie','Sab','Dom')

    def __init__(self, day):
        self.__dia_semana = day
        try:
            self.__num_dia = self.dias_semana.index(self.__dia_semana)
        except:
            raise WeekDayError
        # Escribir código aquí.
        #

    def __str__(self):
        return f"{self.__dia_semana}"
        # Escribir código aquí.
        #

    def add_days(self, n):
        num_dia = self.dias_semana.index(self.__dia_semana)
        __num_dias = ((self.__num_dia + n) % 7)
        self.__dia_semana = self.dias_semana[__num_dias]


    def subtract_days(self, n):
        num_dia = self.dias_semana.index(self.__dia_semana)
        num_dia = ((num_dia - n)% 7)
        self.__dia_semana = self.dias_semana[num_dia]
        # Escribir código aquí.
        #

system("cls || clear")
try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
