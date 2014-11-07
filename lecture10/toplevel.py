import tkinter

def changewindow():
	window1.geometry("100x100")

base = tkinter.Tk()
base.title("base")
b = tkinter.Button(base, text="Make it smaller", command=changewindow)
b.pack()

window1 = tkinter.Toplevel()
window1.title("window1")

base.mainloop() 