#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox


def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        window.destroy();

def gemini():
    messagebox.showinfo("Your choice","You've chosen to be Gemini")

def pisces():
    messagebox.showinfo("Your choice", "You've chosen to be Pisces")

def leo():
    messagebox.showinfo("your choice","You've chosen to be Leo")

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

#Switches:
switch_radio_buttons = tk.IntVar()
switch_radio_buttons.set(1)
switch_checkbox_1 = tk.IntVar()
switch_checkbox_1.set(1)
switch_checkbox_2 = tk.IntVar()
switch_checkbox_2.set(0)
switch_checkbox_3 = tk.IntVar()
switch_checkbox_3.set(0)
#Buttons:
button_pisces = tk.Button(main_frame, text="Pisces? ♓",bg="#e9a390",activebackground="#f7dcd4",activeforeground="#e76946",font=("Helvetica",12),command=pisces)
button_leo = tk.Button(main_frame, text="   Leo? ♌  ",bg="#e9a390",activebackground="#f7dcd4",activeforeground="#e76946",font=("Helvetica",12),command=leo)
button_gemini = tk.Button(main_frame, text="Gemini? ♊",bg="#e9a390",activebackground="#f7dcd4",activeforeground="#e76946",font=("Helvetica",12),command=gemini)

#Checkbuttons:
checkbutton_1 = tk.Checkbutton(main_frame,text="I like it!",bg="#f7dcd4", fg="darkorange4",activebackground="#e9a390", variable=switch_checkbox_1,font=("Helvetica",13),width="7")
checkbutton_2 = tk.Checkbutton(main_frame,text="I like it!",bg="#f7dcd4",fg="darkorange4",activebackground="#e9a390",variable=switch_checkbox_2,font=("Helvetica",13),width="7")
checkbutton_3 = tk.Checkbutton(main_frame,text="I like it!",bg="#f7dcd4",fg="darkorange4",activebackground="#e9a390",variable=switch_checkbox_3,font=("Helvetica",13),width="7")

#Text label and text box:
text_label = tk.Label(main_frame,text="Write yours here:",bg="#e5c5bc",font=("Helvetica",12,"bold"))
text_box = tk.Entry(main_frame,width=15,bg="#f7dcd4",fg="darkorange4",font=("Helvetica",12,"italic"))

#Radio buttons:
radiobutton_1 =tk.Radiobutton(main_frame,text="Gemini",bg="#f7dcd4",activebackground="#e9a390",variable=switch_radio_buttons,value=1)
radiobutton_2 = tk.Radiobutton(main_frame,text="Pisces",bg="#f7dcd4",activebackground="#e9a390",variable = switch_radio_buttons,value=2)
radiobutton_3 = tk.Radiobutton(main_frame,text="Leo poco",bg="#f7dcd4",activebackground="#e9a390",variable=switch_radio_buttons,value=3)

#Just exit button:
exit_button = tk.Button(main_frame, text="Exit",command=Click,font=("Helvetica",12),bg="#e76946",activebackground="#e9a390",activeforeground="white")


# button_1.pack(s="left",fill="x",padx=(10,10))
# button_2.pack(s="left",fill="x",padx=(10,10))
# button_3.pack(s="left",fill="x",padx=(10,10))
# button_1.grid(row=2)
# button_2.grid(row=3)
# button_3.grid(row=4)
# exit_button.grid(row=5)


button_pisces.place(x=70,y=120)

button_leo.place(x=75,y=170)
#switch_3.place(x=100,y=295)
button_gemini.place(x=220,y=170)

text_label.place(x=70,y=230)
text_box.place(x=220,y=225)

checkbutton_1.place(x=220,y=280)
checkbutton_2.place(x=220,y = 310)
checkbutton_3.place(x=220,y = 340)

radiobutton_1.place(x=60,y=280)
radiobutton_2.place(x=40,y=310)
radiobutton_3.place(x=60,y= 340)
#exit_button.pack(side=tk.BOTTOM)
exit_button.place(x=280,y=375)
#button_4.pack(side=tk.BOTTOM,fill="x")



window.mainloop()