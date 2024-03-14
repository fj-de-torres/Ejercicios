#Francisco José de Torres Sánchez-Simón
#The code doesn't work in gui mode. Only calling the class method from the terminal and commenting out the 'input' lines. I don't know why. I have received the aid of Copilot-Bing chat which conversation I share here: 
#https://copilot.microsoft.com/sl/iirHZFthDMa

#Online version: https://github.com/fj-de-torres/Ejercicios/tree/main/session17/proyecto_gui
import tkinter as tk
from tkinter import ttk

from bbdd import *
if __name__ = "__main__":

    clear()
    #This is the code I tried that doesn't display the widgets in an orderdly manner:
    tasks_francisco = Tasks()
    # tasks_francisco.add_task("Nothing for tomorrow","20/06/2024","low")
    # tasks_francisco.show_tasks()
    # root = tk.Tk()
    # root.geometry("500x400")
    # root.title("My tasks app")
    # app_title = tk.Label(root, text = "Simple Task Appp",font = ('Helvetica', 24, "bold"))
    # #app_title.grid(row=1, column=3)
    # app_title.pack(anchor='n')
    # #---Entry info frame:--------------
    # database_frame = tk.Frame(root)
    # database_frame.pack(side='left',padx= 0,pady=100)
    # #---Tasks button:---
    # task_label = ttk.Label(database_frame, text = "Brief task descripton:",font=('Arial',15))
    # task_label.pack(side="left",padx=(10,10))
    # task_var = tk.StringVar
    # task_text = ttk.Entry(task_label,width="30",textvariable=task_var)
    # task_text.pack(side="left")
    # #task_label.pack(side="left",padx=10)
    # #---Deadline button:----
    # deadline_label = ttk.Label(database_frame, text = "Deadline date:",font=('Arial',15))
    # deadline_label.pack(side="left",padx=(10,10))
    # deadline_var = tk.StringVar
    # deadline_text = ttk.Entry(task_label,width="30",textvariable=deadline_var)
    # deadline_text.pack(side="left")
    # #----Priority button:------------
    # priority_label = ttk.Label(database_frame, text = "Priority: ",font=('Arial',15))
    # priority_label.pack(side="left",padx=(10,10))
    # priority_var = tk.StringVar
    # priority_text = ttk.Entry(priority_label,width="30",textvariable=priority_var)
    # priority_text.pack(side="left")

    # #----Exit button inside a specific "Exit frame":--------------
    # exit_button_frame = tk.Frame(root)
    # exit_button_frame.pack(side = 'bottom')
    # exit_button = ttk.Button(exit_button_frame,text = "Exit", command = root.destroy)
    # exit_button.pack()
    # root.mainloop()

    def gui():

        # Create an instance of the tasks class
        tasks_francisco = Tasks()

        # Create the main window with specified dimensions
        root = tk.Tk()
        root.geometry("500x400")
        root.title("My tasks app")

        # Create a Frame for the title
        title_frame = tk.Frame(root)
        title_frame.pack(side='top', fill='x')

        # Create a Label for the title
        app_title = tk.Label(title_frame, text="Simple Task App", font=('Helvetica', 24, "bold"))
        app_title.pack(side='top')

        # Create a Frame for the input fields
        input_frame = tk.Frame(root)
        input_frame.pack(expand=True)

        # Create Labels and Entry widgets
        entry_vars = []  # List to hold the StringVar objects
        for i, label_text in enumerate(["Brief task description:", "Deadline date:", "Priority:"]):
            # Create a Label
            label = ttk.Label(input_frame, text=label_text, font=('Arial', 15))
            label.grid(row=i, column=0, sticky='e', padx=(10, 10), pady=5)

            # Create an Entry (text box)
            entry_var = tk.StringVar()
            entry_vars.append(entry_var)  # Add the StringVar object to the list
            entry = ttk.Entry(input_frame, width=30, textvariable=entry_var)
            entry.grid(row=i, column=1, padx=(0, 10), pady=5)

        # Function to fetch the text and call tasks_francisco
        def fetch_and_call():
            # Fetch the text from the StringVar objects
            args = [var.get() for var in entry_vars]
            # Call tasks_francisco.add_task with the fetched text
            tasks_francisco.add_task(*args)

        # Create a Frame for the buttons
        button_frame = tk.Frame(root)
        button_frame.pack(side='bottom', fill='x')

        # Create a Fetch button
        fetch_button = ttk.Button(button_frame, text="Fetch", command=fetch_and_call)
        fetch_button.pack(side='top', fill="x")

        # Create an Exit button
        exit_button = ttk.Button(button_frame, text="Exit", command=root.destroy)
        exit_button.pack(side='top', fill="x")

        root.mainloop()
    

