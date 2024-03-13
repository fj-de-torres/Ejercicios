import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

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


def create_file(content="", title="Sin titulo"):
    text_area = tk.Text(notebook)
    text_area.insert("end", content)
    text_area.pack(fill="both", expand=True)
    
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
    
    create_file(content=text, title=file_name)

def save_file():
    file_path = filedialog.asksaveasfilename()
    try:
        file_name = os.path.basename(file_path)
        text_widget = get_text_widget()
        text = text_widget.get("1.0", "end-1c")
        
        with open(file_path, "w") as file:
            file.write(text)

    except (AttributeError, FileNotFoundError):
        print("Guardado cancelado")
        return
    
    notebook.tab("current", text=file_name)
    text_contents[str(text_widget)] = hash(text)


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
        if not confirm:
            return
    
    root.destroy()

def close_current_tab():
    notebook.forget(notebook.select())

root = tk.Tk()
root.geometry("300x300")
root.title("Editor de texto")
root.option_add("*tearOff", False)

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True, padx=(1), pady=(4,0))

#crear menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Archivo", menu=file_menu)

#crear opcion en menu
file_menu.add_command(label="Nuevo", command=create_file, accelerator="Ctrl+N")
file_menu.add_command(label="Abrir", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Guardar", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Cerrar tab", command=close_current_tab, accelerator="Ctrl+Q")
file_menu.add_command(label="Salir", command=confirm_quit)

#creacion del notebook
notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)

create_file()

root.bind("<KeyPress>", lambda event: check_for_changes())
root.bind("<Control-n>", lambda event: create_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-q>", lambda event: close_current_tab())
root.bind("<Control-s>", lambda event: save_file())

root.mainloop()


"""
Añadir la opcion de ABRIR FICHERO asociada a una funcion llamada open_file que cargue
el contenido.
"""