# Módulo fechas:
## Módulo *datetime*:

```
from sys import path
path.append('/home/francisco/Documents/Learning/PUE/Python/Ejercicios/')
from funfont import *
from colorama import Fore,Back, Style
from os import system
from datetime import date, datetime

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

hoy = datetime.today()
tal_dia_2003 = hoy.replace(year=2003)
print_columna("tal_dia_2003",tal_dia_2003)

print(hoy)
print(hoy.strftime("%d-%m"))
print(hoy.strftime("%Y-%m-%d"))
print(hoy.strftime("%d-%m-%y"))
#Si lo pongo el año en mayúsculas, el año sale en 4 dígitos. En minúsculas, en dos dígitos.