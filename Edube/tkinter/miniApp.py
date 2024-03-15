import tkinter as tk
from tkinter import messagebox


def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        window.destroy();


window = tk.Tk()
window.geometry("600x650")

window.title("Mini App with Tkinter")

# Add image file 
bg = tk.PhotoImage(file = "/home/francisco/Documents/Learning/PUE/Python/Ejercicios/Edube/tkinter/abstract2.png") 
  
# Show image using label 
main_frame = tk.Frame(window,height=450,width=400,bg="white")
main_frame.pack()
background_label = tk.Label( main_frame, image = bg)



title_label = tk.Label(main_frame, text="Mini App",font=("Arial",25,"bold"))
#title_label.pack(side=tk.TOP,fill="x",pady=(10,0))
title_label.pack(side=tk.TOP,fill="x")

background_label.pack()
#background_label.place(x = 0, y = 30)




button_1 = tk.Button(main_frame, text="Button #1")
button_2 = tk.Button(main_frame, text="Button #2")
button_3 = tk.Button(main_frame, text="Button #3")
exit_button = tk.Button(main_frame, text="Exit",command=Click)
# button_1.pack(s="left",fill="x",padx=(10,10))
# button_2.pack(s="left",fill="x",padx=(10,10))
# button_3.pack(s="left",fill="x",padx=(10,10))
# button_1.grid(row=2)
# button_2.grid(row=3)
# button_3.grid(row=4)
# exit_button.grid(row=5)
button_1.place(x=150,y=170)
button_2.place(x=150,y=230)
button_3.place(x=150,y=290)
exit_button.pack(side=tk.BOTTOM)
exit_button.place(x=170,y=340)
#button_4.pack(side=tk.BOTTOM,fill="x")
window.mainloop()