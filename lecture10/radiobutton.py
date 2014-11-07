from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

def sel2():
   selection = "You selected the option " + str(var2.get())
   label2.config(text = selection)

root = Tk()
var = IntVar()
g1_1 = Radiobutton(root, text="Group1 Option 1", variable=var, value=1,command=sel)
g1_1.pack(side=TOP)
g1_2 = Radiobutton(root, text="Group1 Option 2", variable=var, value=2,command=sel)
g1_2.pack(side=TOP)
g1_3 = Radiobutton(root, text="Groups1 Option 3", variable=var, value=3,command=sel)
g1_3.pack(side=TOP)

label = Label(root, text="Your selection will appear here")
label.pack(side=TOP)

var2 = IntVar()
g2_1 = Radiobutton(root, text="Group1 Option 1", variable=var2, value=10,command=sel2)
g2_1.pack(side=TOP)
g2_2 = Radiobutton(root, text="Group1 Option 2", variable=var2, value=20,command=sel2)
g2_2.pack(side=TOP)
g2_3 = Radiobutton(root, text="Groups1 Option 3", variable=var2, value=30,command=sel2)
g2_3.pack(side=TOP)

label2 = Label(root, text="Your second selection will appear here")
label2.pack(side=TOP)
root.mainloop()