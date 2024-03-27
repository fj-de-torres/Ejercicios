import os
from sys import path
from datetime import date, datetime
from colorama import Fore,Back, Style
#Local path to import funfont own module:
where_am_i = os.path.dirname(__file__)
if 'Ejercicios' in where_am_i:
    while os.path.basename(os.getcwd()) != 'Ejercicios':
        os.chdir('..')
current_path = os.getcwd()

#current_directory = os.path.basename(current_path)
path.append(current_path)
os.chdir(where_am_i)
from funfont import *


cumple_juan = date(1985, 4, 18)
print_columna("cumple_juan = date(1985, 4, 18)",cumple_juan)

#Si cambio el orden americano normal, lo tengo que especificar:
cumple_juan = date(day=18, year=1985, month=4)
print_columna("type(cumple_juan)",type(cumple_juan))
print_columna("cumple_juan",cumple_juan)

#¿Fecha del sistema?

#print_columna("date.today().day",date.today().date)
print(date.today().day)

cumple_maria = datetime(day=1, year=1992, month=9)
#rint_columna("cumple_maria",cumple_maria)

cumple_maria = datetime(day=1, year=1992, month=9, hour=14, minute=20, second=59)

columna.clear_rows
#print_columna("cumple_maria",cumple_maria)

print(cumple_maria.hour)

from datetime import time

#Puede servir para especificar un tiempo de inicio, como vimos en *performance*:



hoy = datetime.today()
tal_dia_2003 = hoy.replace(year=2003)
print_columna("tal_dia_2003",tal_dia_2003)

print(hoy)
print(hoy.strftime("%d-%m"))
print(hoy.strftime("%Y-%m-%d"))
print(hoy.strftime("%d-%m-%y"))
#Si lo pongo el año en mayúsculas, el año sale en 4 dígitos. En minúsculas, en dos dígitos.

inicio = time()
columna = PrettyTable()
# columna.del_column()
# columna.del_column()
# columna.del_column()
print_columna("inicio.hour",inicio.hour)
#Hay que iniciarlo:
print(time(18,25))
## timedela: incrementos de tiempo:
from datetime import timedelta
hoy = datetime.now()
print(hoy)

fecha1 = datetime(2003, 4, 15)
hoy = datetime.now()
print(hoy)

tiempo_transcurrido = hoy - fecha1
print(tiempo_transcurrido)

# En segundos:

print(tiempo_transcurrido.total_seconds())
print(type(tiempo_transcurrido))

veinte_dias_cinco_horas = timedelta(days=20, hours=5)
print(tiempo_transcurrido + veinte_dias_cinco_horas)

#https://docs.python.org/3/library/calendar.html Para cálculos de fechas
