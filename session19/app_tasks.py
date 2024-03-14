# Correción del profesor:
from os import system
import tkinter as tk
from tkinter import messagebox
from tasks import Tarea
#Creamos a continuacoión, una clase que represente la aplicación:
#Paso la ventana principal como parámetro externo.
class ApplicationTasks:

    def __init__(self, master) -> None:
        #lista de tareas
        self.lista_tareas = list()
        self.master = master
        self.master.title("Aplicación de tareas")

        #etiquetas
        tk.Label(self.master, text="Descripcion:").grid(row=0, column=0)
        tk.Label(self.master, text="Fecha:").grid(row=1, column=0)
        tk.Label(self.master, text="Prioridad:").grid(row=2, column=0)

        #entries
        self.descripcion_entry = tk.Entry(self.master)
        self.fecha_entry = tk.Entry(self.master)
        self.prioridad_entry = tk.Entry(self.master)

        self.descripcion_entry.grid(row=0, column=1)
        self.fecha_entry.grid(row=1, column=1)
        self.prioridad_entry.grid(row=2, column=1)

        #botones
        tk.Button(self.master, text="Agregar tarea", command=self.agregar_tarea).grid(row=3, column=0, columnspan=2)
        tk.Button(self.master, text="Ver tareas", command=self.ver_tareas).grid(row=4, column=0, columnspan=2)
        tk.Button(self.master, text="Eliminar esta tarea", command=self.eliminar_tarea).grid(row=5, column=0, columnspan=2)

    def agregar_tarea(self):
        #recogida de datos
        descripcion = self.descripcion_entry.get()
        fecha = self.fecha_entry.get()
        prioridad = self.prioridad_entry.get()

        #validaciones...
        if descripcion and fecha and prioridad:
            #creacion de la tarea
            nueva_tarea = Tarea(descripcion, fecha, prioridad)
            self.lista_tareas.append(nueva_tarea)

            messagebox.showinfo("Tarea agregada", "Tarea agregada con éxito")
        else:
            messagebox.showerror("Error", "Todos los campos son requeridos")

    def ver_tareas(self):
        tareas_str = ""
        if self.lista_tareas:
            for tarea in self.lista_tareas:
                estado = "Completada" if tarea.completada else "Pendiente"
                tareas_str += f"Descripcion: {tarea.descripcion}\nFecha: {tarea.fecha}\nPrioridad: {tarea.prioridad}\nEstado: {estado}\n\n"     

            if tareas_str:
                messagebox.showinfo("Tareas", tareas_str)

        else:
            messagebox.showinfo("Sin tareas", "No hay tareas para mostrar")

    def eliminar_tarea(self):
        if self.lista_tareas:
            descripcion_tarea = self.descripcion_entry.get()
            tarea_a_eliminar = list(filter(lambda tarea: tarea.descripcion == descripcion_tarea, self.lista_tareas))[0]
            self.lista_tareas.remove(tarea_a_eliminar)
            messagebox.showinfo("Tarea eliminada", f"Tarea {tarea_a_eliminar.descripcion} eliminada con éxito")
        else:
            messagebox.showinfo("Sin tareas", "No hay tareas para eliminar")

if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationTasks(root)
    root.mainloop()
