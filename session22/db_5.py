import sqlite3

connection = sqlite3.connect('empleados.db')

cursor = connection.cursor()

sql = "DELETE FROM employees WHERE department = ?;"

departamento = input("Ingrese el departamento a eliminar:")
cursor.execute(sql, (departamento,))

connection.commit() #consolidar la operacion
connection.close()