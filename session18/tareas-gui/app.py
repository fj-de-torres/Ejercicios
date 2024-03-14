#Resources: https://www.youtube.com/watch?v=cd6cA3ekm_E

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

class Tasks:
    def __init__(self) -> None:
        """Connect to the local data base"""
        self.connect = sqlite3.connect('tasks.db') # If it doesn't exist, it will be created.
        self.cursor = self.connect.cursor() #Cursor is needed to do transactions to the data base

        #tasks table creation:
        self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        task_name TEXT NOT NULL,
        deadline DATE NOT NULL,
        priority TEXT CHECK(priority IN ('low', 'medium', 'high')) NOT NULL)
        ''')

        self.connect.commit()#Latter op. consolidation

    def add_task(self,task_name:str,deadline:str,priority:str):
        try:
            #nombre_tarea = input('Task description: ')
            clear()
            while True:
                try:
                    #deadline = input('Fecha límite de la tarea (en formato DD/MM/YYYY): ')
                    deadline = deadline.strip()
                    deadline = deadline.split("/")
                    #Si el formato ingresado no contiene "/" o no es de la forma DD/MM/YYYY, siguiente línea fallará:
                    #If input format does not have "/" or doesn't match with the one required, it will raise an exception.
                    deadline = datetime(*tuple(map(lambda x: int(x),deadline[::-1]))) #Como he solicitado la fecha en formato contrario al americano, le doy la vuelta a la lista, convierto a int cada  uno de sus valores (con lambda y map), eso lo paso a tupla, la deshago, y ya tengo el formato adecuado para generar una fecha con date().
                    #Este es el formato en el que deseo guardar las fechas. Coincide con la solicitada al usuario, pero  es al revés de la que maneja el sistema.
                    deadline_str = deadline.strftime("%d/%m/%Y")
                    if deadline < datetime.today():
                        raise InvalidDateException
                except InvalidDateException:
                    print(alert("Deadline cannot be older than current date!"))
                
                except Exception:
                    print(alert("Formato de fecha no válida. Por favor, ajústese al formato indicado"))
                #Check that input date is in the required format:
                else:
                    break
        
            #priority = input('priority (high/medium/low): ')
            while True:
                if priority.isalpha():
                    priority = priority.lower()
                    match priority:
                        case "low":
                            priority = "low"
                        case "medium":
                            priority = "medium"
                        case "high":
                            priority = "high"
                        case _ :
                            priority = "low"
                    break
                else:
                    print("Please classify priority as \"low\", \"medium\" or \"high\" (without quotes)")
    
            if task_name and deadline and priority:
                self.cursor.execute('''
                    INSERT INTO tasks (task_name, deadline, priority)
                    VALUES (?, ?, ?)
                ''', (task_name, deadline_str, priority))
                self.connect.commit() #Auque podría tener la bbdd configurada para hacer un *auto-commit*
                clear()
                print(Fore.YELLOW + "Task saved!" + Fore.WHITE)
            else:
                print(alert(''))
        except KeyboardInterrupt:
                print(Fore.YELLOW + "Halted by user!" + Fore.WHITE)
                exit()

    def show_tasks(self):
        self.cursor.execute('SELECT * FROM tasks')
        tasks = self.cursor.fetchall()
        clear()
        for tarea in tasks:
            print(title("Task ID:" )+ f"{tarea[0]}", title("Task description: ") + f"{tarea[1]}", title("Deadline: ") + f"{tarea[2]}", title("priority: ") + f"{tarea[3]}",sep="\n")
            print('-'*50)

clear()
#This is the code I tried that doesn't display the widgets in an orderdly manner:
tasks = Tasks()

# Instancia de la clase Tasks
tasks = Tasks()

def agregar_tarea():
    tarea = entrada_tarea.get()
    deadline = "01/01/2025"  # Aquí deberías obtener la fecha límite de alguna manera
    priority = "low"  # Aquí deberías obtener la prioridad de alguna manera
    if tarea != "":
        # Insertar la tarea en la base de datos
        tasks.add_task(tarea, deadline, priority)
        actualizar_tareas()

def actualizar_tareas():
    lista_tareas.delete(0, tk.END)
    # Obtener todas las tareas de la base de datos
    for tarea in tasks.cursor.execute("SELECT * FROM tasks"):
        lista_tareas.insert(tk.END, tarea[1])  # tarea[1] es el nombre de la tarea

# Crear la ventana principal
ventana = tk.Tk()

# Widgets para ingresar nuevas tareas
entrada_tarea = tk.Entry(ventana)
entrada_tarea.pack()

boton_agregar = tk.Button(ventana, text="Agregar tarea", command=agregar_tarea)
boton_agregar.pack()

# Widget para mostrar las tareas existentes
lista_tareas = tk.Listbox(ventana)
lista_tareas.pack()

# Iniciar la GUI
ventana.mainloop()
#Ayuda:
# food_list = ['apple', 'banana', 'orange']
# list1 = tk.StringVar(value=food_list)
# lst = tk.Listbox(root,
#     listvariable=list1)
# lst.pack()
