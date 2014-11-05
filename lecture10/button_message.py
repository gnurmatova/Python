import tkinter
from tkinter import messagebox

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

base = tkinter.Tk()
button = tkinter.Button(base, text="show message", command=helloCallBack)
button.pack()
base.mainloop()
