import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x400")
main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

main2 = ttk.Frame(master=main)
main2.pack(side="left", fill="both")

tk.Label(main, text="Etiqueta 1", bg="lightgreen").pack(side="top", expand=True, fill="both")
tk.Label(main, text="Etiqueta 2", bg="pink").pack(side=tk.TOP, expand=True, fill="both")
tk.Label(main2, text="Etiqueta 3", bg="cyan").pack(side=tk.LEFT, expand=True, fill="both")



root.mainloop()