import sqlite3

connection = sqlite3.connect('empleados.db')

cursor = connection.cursor()

sql = """
    CREATE TABLE IF NOT EXISTS employees (
         id INTEGER,
         name VARCHAR(64),
         department VARCHAR(32),
         phone VARCHAR(16),
         email VARCHAR(32)
)
"""

cursor.execute(sql)
connection.commit() #Consolidar la operación.