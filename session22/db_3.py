import sqlite3

connection = sqlite3.connect('empleados.db')

cursor = connection.cursor()

sql = "select * from employees"

cursor.execute(sql)

#Sólo se tienen que consolidar las instrucciones que modifiquen la bbdd. Es decir, no hay que hacer commit aquí simplemente para obtener una lectura de la base de datos.

for row in cursor.fetchall():
    print(type(row))
    print(row)


cursor.close()