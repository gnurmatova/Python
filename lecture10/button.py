import tkinter
import sys

base = tkinter.Tk()
button = tkinter.Button(base, text="close this", command=sys.exit)
button.pack()
base.mainloop()