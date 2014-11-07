from tkinter import *
from tkinter import messagebox

def cmd():
   messagebox.showinfo("User Name", e1.get())


base = Tk()
l1 = Label(base, text="User Name")
l1.pack( side = LEFT)
e1 = Entry(base)
e1.pack(side = LEFT)
b1 = Button(base, text="Enter", command=cmd)
b1.pack()

base.mainloop()