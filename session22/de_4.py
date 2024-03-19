import sqlite3

connection = sqlite3.connect('empleados.db')

cursor = connection.cursor()

id_empleado = input("Ingrese el id del empleado: ")

sql = "UPDATE employees SET department = 'IT' WHERE id = ?;"
cursor.execute(sql,(id_empleado,))#Una tupla en la que aparecen, sql, y los campos parametrizados después del where.

connection.commit() #consolidar la operacion
connection.close()