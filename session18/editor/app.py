import os
import tkinter as tk
from tkinter import ttk, filedialog
from colorama import Fore,Back, Style
def create_file():
    text_area = tk.Text(notebook)
    text_area.pack(fill="both", expand=True)
    
    notebook.add(text_area, text="Nuevo")

def save_file():
    file_path = filedialog.asksaveasfilename() #Se puede hacer con filepath comentado ayer.
    try:
        file_name = os.path.basename(file_path)
        text_widget = root.nametowidget(notebook.select()) #Selecciono el contenido del widget que está activo
        
        text = text_widget.get("1.0", "end-1c") #Le tengo que especificar, el contenido, desde donde empieza hasta donde acaba: Desde la primera línea, el primer carácter. Y llegar hasta el final menos un carácter; es decir, todo menos el salto de línea final.
        with open(file_name, "w") as file:
            file.write(text)
    except (AttributeError, FileNotFoundError):
        print(Fore.RED + Style.BRIGHT + "Guardado cancelado" + Style.RESET_ALL)
        return #Con este return, salgo de la función porque si no, seguiría ejecutando código
    notebook.tab("current", text=file_name)

root = tk.Tk()
root.geometry("300x300")
root.title("Editor de texto")

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True, padx=(1), pady=(4,0))
#Crear menu:
menu_bar = tk.Menu(root)

root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Archivo", menu=file_menu)

#crear opcion en menu
file_menu.add_command(label="Nuevo", command=create_file)
#file_menu = tk.Menu(menu_bar, tearoff = 0) # impide que se desacople el menú.
file_menu.add_command(label="Guardar", command=save_file) #Ojo! No se ponen paréntesis porque no se llama a la función. Se direcciona.
#creacion del notebook
notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)
create_file()
root.mainloop()
