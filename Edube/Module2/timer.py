"""


Necesitamos una clase capaz de contar segundos. ¿Fácil? No es tan fácil como podrías pensar, ya que tendremos algunos requisitos específicos.

Léelos con atención, ya que la clase sobre la que escribes se utilizará para lanzar cohetes en misiones internacionales a Marte. Es una gran responsabilidad. ¡Contamos contigo!

Tu clase se llamará Timer (temporizador en español). Su constructor acepta tres argumentos que representan horas (un valor del rango [0..23]; usaremos tiempo militar), minutos (del rango [0. .59]) y segundos (del rango [0..59]).

Cero es el valor predeterminado para todos los parámetros anteriores. No es necesario realizar ninguna comprobación de validación.

La clase en sí debería proporcionar las siguientes facilidades:

    Los objetos de la clase deben ser "imprimibles", es decir, deben poder convertirse implícitamente en cadenas de la siguiente forma: "hh:mm:ss", con ceros a la izquierda agregados cuando cualquiera de los valores es menor que 10.
    La clase debe estar equipada con métodos sin parámetros llamados next_second() y previous_second (), incrementando el tiempo almacenado dentro de los objetos en +1/-1 segundos respectivamente.

Emplea las siguientes sugerencias:

    Todas las propiedades del objeto deben ser privadas.
    Considera escribir una función separada (¡no un método!) para formatear la cadena con el tiempo.

Completa la plantilla que te proporcionamos en el editor. Ejecuta tu código y comprueba si el resultado es el mismo que el nuestro.
Salida Esperada

23:59:59
00:00:00
23:59:59
"""
from os import system

class Timer:
    def __init__( self, horas:str,minutos:str,segundos:str ):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    def __str__(self):
        horas, minutos, segundos = (self.__horas,self.__minutos,self.__segundos)
        if self.__horas < 10:
            horas = "0"+str(self.__horas)
        if self.__minutos < 10:
            minutos = "0" + str(self.__minutos)
        if self.__segundos < 10:
            segundos = "0" + str(self.__segundos)
            
        return f"{horas}:{minutos}:{segundos}"

    def next_second(self):
        self.__segundos += 1
        if self.__segundos == 60:
            self.__minutos += 1
            self.__segundos = 0
        if self.__minutos == 60:
           self.__horas += 1
           self.__minutos = 0
        if self.__horas == 24:
            self.__horas = 0

    def prev_second(self):
        self.__segundos -= 1
        if self.__segundos < 0:
            self.__minutos -= 1
            self.__segundos = 0
        if self.__minutos < 0:
            self.__horas -= 1
            self.__minutos = 0
        if self.__horas <= 0:
            self.__horas = 23
            self.__minutos = 59
            self.__segundos = 59


system("cls || clear")

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)