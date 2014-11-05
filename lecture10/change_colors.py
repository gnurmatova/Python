import tkinter
from tkinter import messagebox

color1="#CCFFFF"
color2="#CCFFCC"
currentcolor=color1

def changecolor():
	global currentcolor
	if(currentcolor == color1):
		currentcolor = color2
	else:
		currentcolor = color1

	base.configure(bg=currentcolor)
	button.configure(text=currentcolor,highlightbackground=currentcolor ) 


base = tkinter.Tk()
base["bg"]=currentcolor #same can be achieved through base.configure(bg=color1)
base.geometry("500x500") #resize main window
button = tkinter.Button(base, 
	text=currentcolor, 
	command=changecolor, 
	highlightbackground=currentcolor)
button.pack()
base.mainloop()