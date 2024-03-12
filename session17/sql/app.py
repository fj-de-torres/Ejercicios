import sqlite3
from time import sleep
from os import system
from colorama import Fore
def clear():
    system("cls || clear")
class Appcontactos:
    def __init__(self) -> None:
        #Conectar con la base de datos
        self.conn = sqlite3.connect('contactos.db') # Si no existe, lo crea.
        self.cursor = self.conn.cursor() #Para hacer operaciones en la bbdd necesito un cursor

        #Crear tabla de contactos:
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                telefono TEXT NOT NULL,
                email TEXT NOT NULL)
        ''')
        self.conn.commit()#Consolidación de la oeración anterior. Ejecución real

    def agregar_contacto(self):
        nombre = input('Nombre: ')
        telefono = input('Telefono: ')
        email = input('Email: ')

        if nombre and telefono and email:
            self.cursor.execute('''
                INSERT INTO contactos (nombre, telefono, email)
                VALUES (?, ?, ?)
            ''', (nombre, telefono, email))
            self.conn.commit() #Auque podría tener la bbdd configurada para hacer un *auto-commit*
            print("Contacto guardado")
        else:
            print('Falta algún cmapo por rellenar')
    
    def mostrar_contactos(self):
        self.cursor.execute('SELECT * FROM contactos')
        contactos = self.cursor.fetchall()

        for contacto in contactos:
            print(f"ID: {contacto[0]}, Nombre: {contacto[1]}, Telefono: {contacto[2]}, Email: {contacto[3]}")

    def ejecutar(self):
        """Presesnta al usuario un menú de usuario que permita las opciones:
        1.- Agregar contactos
        2.- Mostrar contactos
        3.- Salir"""
        # clear()
        # response = None
        # while response != 3:
        #     clear()
        #try:
            # """ """ response = input("""Press number in your keyboard to choose an option from the menu:
            #          1. - Add contacts
            #          2. - List contacts
            #          3. - Exit\n""")
            # if response == "1":
            #     clear()
            #     self.agregar_contacto()
            # elif response == "2":
            #     clear()
            #     self.mostrar_contactos()
            #     sleep(2)
            # elif response == "3":
            #     clear()
            #     print(Fore.YELLOW + "See you..!" + Fore.WHITE)
            #     sleep(.5)
            #     exit() """ """
        # except KeyboardInterrupt:
        #     print("Exiting app...")
        #     sleep(.5)
    #Versión del profesor:
        while True:
            print('\n----Menu app de contactos----')
            print("1.- Agregar contacto")
            print("2.- Mostrar contactos")
            print("3.- Salir")

            opcion = input('Opción: ')
            
            """ if opcion == "1":
                self.agregar_contacto()
            elif opcion == "2":
                self.mostrar_contactos()
            elif opcion == "3":
                break
             """ 
            #Nueva forma en la versión 3.11:
            match opcion: 
                    case "1":
                        self.agregar_contacto()
                    case "2":
                        self.mostrar_contactos()
                    case "3":
                        break
                    case _:
                        print('Opción no válida')    
db_app = Appcontactos()
# for _ in range(3):
#     db_app.agregar_contacto() #Nos va a pedir los contactos a añadir:

db_app.mostrar_contactos()
db_app.ejecutar()


