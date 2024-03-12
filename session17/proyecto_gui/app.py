from os import system
from time import sleep
from datetime import datetime
import sqlite3
import tkinter as tk
from tkinter import ttk
from colorama import Fore, Back, Style

#------Formatting functions for the command line:-----------------
def clear():
    system("cls || clear")

def title(string:str)->str:
    return Style.BRIGHT + f"{string}" + Style.RESET_ALL

def alert(string:str) -> str:
    return Style.BRIGHT + Fore.RED + f"{string}" + Style.RESET_ALL

class InvalidDateException(Exception):
    pass

class Tareas:
    def __init__(self) -> None:
        """Connect to the local data base"""
        self.connect = sqlite3.connect('contactos.db') # If it doesn't exist, it will be created.
        self.cursor = self.connect.cursor() #Cursor is needed to do transactions to the data base

        #tasks table creation:
        self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY,
        nombre_tarea TEXT NOT NULL,
        fecha_tarea DATE NOT NULL,
        prioridad TEXT CHECK(prioridad IN ('baja', 'media', 'alta')) NOT NULL)
        ''')

        self.connect.commit()#Latter op. consolidation

    def agregar_tarea(self):
        try:
            nombre_tarea = input('Descripción de tarea: ')
            clear()
            while True:
                try:
                    fecha_tarea = input('Fecha límite de la tarea (en formato DD/MM/YYYY): ')
                    fecha_tarea = fecha_tarea.strip()
                    fecha_tarea = fecha_tarea.split("/")
                    #Si el formato ingresado no contiene "/" o no es de la forma DD/MM/YYYY, siguiente línea fallará:
                    #If input format does not have "/" or doesn't match with the one required, it will raise an exception.
                    fecha_tarea = datetime(*tuple(map(lambda x: int(x),fecha_tarea[::-1]))) #Como he solicitado la fecha en formato contrario al americano, le doy la vuelta a la lista, convierto a int cada  uno de sus valores (con lambda y map), eso lo paso a tupla, la deshago, y ya tengo el formato adecuado para generar una fecha con date().
                    #Este es el formato en el que deseo guardar las fechas. Coincide con la solicitada al usuario, pero  es al revés de la que maneja el sistema.
                    fecha_tarea_str = fecha_tarea.strftime("%d/%m/%Y")
                    if fecha_tarea < datetime.today():
                        raise InvalidDateException
                except InvalidDateException:
                    print(alert("La fecha  límite no puede ser anterior a la actual"))
                
                except Exception:
                    print(alert("Formato de fecha no válida. Por favor, ajústese al formato indicado"))
                #Check that input date is in the required format:
                else:
                    break
        
            prioridad = input('Prioridad (alta/media/baja): ')
            while True:
                if prioridad.isalpha():
                    prioridad = prioridad.lower()
                    match prioridad:
                        case "baja":
                            prioridad = "baja"
                        case "media":
                            prioridad = "media"
                        case "alta":
                            prioridad = "alta"
                        case _ :
                            prioridad = "baja"
                    break
                else:
                    print("Por favor defina la prioridad como \"baja\", \"media\" o \"alta\" (sin las comillas)")
    
            if nombre_tarea and fecha_tarea and prioridad:
                self.cursor.execute('''
                    INSERT INTO tareas (nombre_tarea, fecha_tarea, prioridad)
                    VALUES (?, ?, ?)
                ''', (nombre_tarea, fecha_tarea_str, prioridad))
                self.connect.commit() #Auque podría tener la bbdd configurada para hacer un *auto-commit*
                clear()
                print(Fore.YELLOW + "Tarea guardada" + Fore.WHITE)
            else:
                print(alert('Falta algún campo por rellenar'))
        except KeyboardInterrupt:
                print(Fore.YELLOW + "Terminado por el usuario" + Fore.WHITE)
                exit()

    def mostrar_tarea(self):
        self.cursor.execute('SELECT * FROM tareas')
        tareas = self.cursor.fetchall()
        clear()
        for tarea in tareas:
            print(title("ID_tarea:" )+ f"{tarea[0]}", title("Descripción de la tarea: ") + f"{tarea[1]}", title("Fecha límite: ") + f"{tarea[2]}", title("Prioridad: ") + f"{tarea[3]}",sep="\n")
            print('-'*50)

clear()
# tareas_francisco = Tareas()
# tareas_francisco.agregar_tarea()
# tareas_francisco.mostrar_tarea()

root = tk.Tk()
root.geometry("500x400")
root.title("My tasks app")
app_title = tk.Label(root, text = "Simple Task Appp",font = ('Helvetica', 24, "bold"))
#app_title.grid(row=1, column=3)
app_title.pack(anchor='n')
task_label = ttk.Label(root, text = "Brief task descripton:",font=('Arial',15))

root.mainloop()
