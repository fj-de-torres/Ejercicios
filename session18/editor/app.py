import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from colorama import Fore,Back, Style

text_contents = dict()

def check_for_changes():
    current = get_text_widget()
    content = current.get("1.0", "end-1c")
    name = notebook.tab("current")["text"]

    if hash(content) != text_contents[str(current)]:
        if name[-1] != "*":
            notebook.tab("current", text=name + "*")
    elif name[-1] == "*":
        notebook.tab("current", text=name[:-1])

def get_text_widget():
    text_widget = notebook.nametowidget(notebook.select())

    return text_widget


def create_file(content="", title="New file"):
    text_area = tk.Text(notebook)
    text_area.insert("end", content) #Es como un append. Es decir, inserto desde el final del contenido.
    # text_area.pack(fill="both", expand=True)
    
    # notebook.add(text_area, text="Nuevo")
    notebook.add(text_area, text=title)
    notebook.select(text_area)

def open_file():
    file_path = filedialog.askopenfilename()
    try:
        file_name = os.path.basename(file_path)
        with open(file_path, "r") as file:
            text = file.read()
    except (AttributeError, FileNotFoundError):
        print("Carga cancelada")
        return
    # Probar también esta opción:
    # text_area = tk.Text(notebook)
    # text_area.pack(fill="both", expand=True)
    # text_area.insert("1.0", text)
    # notebook.add(text_area, text=file_name)
    create_file(content=text, title=file_name)
def save_file():
    file_path = filedialog.asksaveasfilename() #Se puede hacer con filepath comentado ayer.
    try:
        file_name = os.path.basename(file_path)
        text_widget = root.nametowidget(notebook.select()) #Selecciono el contenido del widget que está activo
        
        text = text_widget.get("1.0", "end-1c") #Le tengo que especificar, el contenido, desde donde empieza hasta donde acaba: Desde la primera línea, el primer carácter. Y llegar hasta el final menos un carácter; es decir, todo menos el salto de línea final.
        with open(file_path, "w") as file:
            file.write(text)
    except (AttributeError, FileNotFoundError):
        os.system("cls || clear")
        print(Fore.RED + Style.BRIGHT + "Guardado cancelado" + Style.RESET_ALL)
        return #Con este return, salgo de la función porque si no, seguiría ejecutando código
    notebook.tab("current", text=file_name)
    text_contents[str(text_widget)] = hash(text)

# def open_file():
    # file_path = filedialog.askopenfile()
    # try:
    #     file_name = os.path.basename(file_path)
    #     text_widget = root.nametowidget(notebook.select()) #Selecciono el contenido del widget que está activo
        
    #     #text = text_widget.get("1.0", "end-1c")
    #     with open(file_path, "r") as file:
    #         text = file.read()
    # except (AttributeError, FileNotFoundError):
    #     print(Fore.RED + Style.BRIGHT + "Guardado cancelado" + Style.RESET_ALL)
    #     return 
    # notebook.tab("current", text)
def confirm_quit():
    
    unsaved = False

    for tab in notebook.tabs():
        text_widget = root.nametowidget(tab)
        content = text_widget.get("1.0", "end-1c")

        if hash(content) != text_contents[str(text_widget)]:
            unsaved = True
            break
    
    if unsaved:
        confirm = messagebox.askyesno(
            message="¿Desea salir sin guardar?",
            icon="question",
            title="Salir sin guardar"
        )
def close_current_tab():
    notebook.forget(notebook.select())
#---------------main window-------------------------------------------------
root = tk.Tk()
root.geometry("300x300")
root.title("Editor de texto")
root.option_add("*tearOff",False)

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True, padx=(1), pady=(4,0))
#Crear menu:
menu_bar = tk.Menu(root)

root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Archivo", menu=file_menu)

#crear opcion en menu
file_menu.add_command(label="Nuevo", command=create_file, accelerator="Ctrl+N")
file_menu.add_command(label="Abrir", command=open_file,accelerator="Ctrl+O")
#file_menu = tk.Menu(menu_bar, tearoff = 0) # impide que se desacople el menú.
file_menu.add_command(label="Guardar", command=save_file,accelerator="Ctrl+S") #Ojo! No se ponen paréntesis porque no se llama a la función. Se direcciona.
#creacion del notebook
file_menu.add_command(label="Cerrar tab", command=close_current_tab, accelerator="Ctrl+Q")
file_menu.add_command(label="Salir",command=confirm_quit)

notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)
create_file()
root.bind("<Control-n>",lambda event: create_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-q>", lambda event: close_current_tab())
root.bind("<Control-s>", lambda event: save_file())
root.mainloop()
"""
TO DO LIST:
Añadir la opción de abrir fichero asociada a una función llamada open_file que cargue el contenido.
"""
