from tkinter import *
from tkinter import messagebox

def selch1():
   selection = "Music is " + str(chvar1.get())
   label.config(text = selection)

def selch2():
   selection = "Video is " + str(chvar2.get())
   label.config(text = selection)

base = Tk()
chvar1 = IntVar()
chvar2 = IntVar()
ch1 = Checkbutton(base, text = "Music", variable = chvar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20, command = selch1)
ch2 = Checkbutton(base, text = "Video", variable = chvar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20, command = selch2)
ch1.pack()
ch2.pack()

label = Label(base, text="Your selection will appear here")
label.pack(side=BOTTOM)
base.mainloop()