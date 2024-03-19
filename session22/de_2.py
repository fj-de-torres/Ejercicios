import sqlite3

connection = sqlite3.connect('empleados.db')

cursor = connection.cursor()

sql = """
INSERT INTO employees (id, name, department, phone, email) VALUES (1, "Juan Lopez", "QA", "1234567890", "juanl@gmail.com");
INSERT INTO employees (id, name, department, phone, email) VALUES (2, "Maria Lopez", "RRHH", "1234567891", "marial@gmail.com");
INSERT INTO employees (id, name, department, phone, email) VALUES (3, "Laura Garcia", "IT", "1234567892", "laurag@gmail.com");
"""
#cuando tengamos varias instrucciones seguidas, es decir, varias líneas de sql separadas por ;, el comando para ejecutarlas es:
cursor.executescript(sql)
connection.commit() #consolidar la operacion
connection.close()
#Es decir, executescript(sql) en vez de execute(sql)