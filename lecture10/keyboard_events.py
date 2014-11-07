from tkinter import *

def keyPressed(  event ):
   var.set( repr(event.char) + " pressed")
   frame.focus_set()

base = Tk()
base.title("Keyboard Events")


frame = Frame(base, width=300, height=300)


var = StringVar()
var.set("Keyboard Events will show here")
label = Label(base, textvariable=var)
label.pack(side=BOTTOM)

frame.bind("<Key>", keyPressed)
frame.bind('<Left>', keyPressed)
frame.bind('<Right>', keyPressed)

frame.focus_set()
frame.pack()

base.mainloop()