# Correción del profesor:
import tkinter as tk
from tkinter import messagebox

#Creamos a continuacoión, una clase que represente la aplicación:

class ApplicationTasks:

    def __init__(self,master) -> None: #Paso la ventana principal como parámetro externo.
        #Lista de tareas
        self.lista_tareas = list()
        self.master = master
        self.master.title("Aplicación de tareas")

        #etiquetas
        