import tkinter as tk
from tkinter import messagebox


def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        skylight.destroy();


window = tk.Tk()
window.geometry("400x400")

button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.pack(s="left",fill="x",padx=(10,10))
button_2.pack(s="left",fill="x",padx=(10,10))
button_3.pack(s="left",fill="x",padx=(10,10))
window.mainloop()