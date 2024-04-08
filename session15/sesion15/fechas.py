from datetime import date, datetime
#from uuid import uuid4

cumple_juan = date(day=18, year=1985, month=4)
#print(type(cumple_juan))
#print(cumple_juan)

#id_unic = uuid4()
#print("ID:", id_unic)

#print(cumple_juan.day)

#dia de hoy
#print(date.today().day)


cumple_maria = datetime(day=1, year=1992, month=9, hour=14, minute=20, second=59)
#print(cumple_maria)
#print(cumple_maria.hour)

hoy = datetime.today()
tal_dia_2003 = hoy.replace(year=2003)
#print(tal_dia_2003)

#print(tal_dia_2003.microsecond)

print(hoy)
print(hoy.strftime("%d-%m"))
print(hoy.strftime("%y-%m-%d"))
print(hoy.strftime("%A"))

from datetime import time

inicio = time()
print(inicio)
print(inicio.hour)
print(inicio.minute)
print(inicio.second)

print(time(18, 25))

from datetime import timedelta


fecha1 = datetime(2003, 4, 15)
hoy = datetime.now()
print(hoy)

tiempo_transcurrido = hoy - fecha1
print(tiempo_transcurrido)
print(tiempo_transcurrido.total_seconds())
print(type(tiempo_transcurrido))


veinte_dias_cinco_horas = timedelta(days=20, hours=5)
print(tiempo_transcurrido + veinte_dias_cinco_horas)

seis_meses = timedelta(days=)

hoy + seis_meses













