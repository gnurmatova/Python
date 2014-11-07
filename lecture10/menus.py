from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

root = Tk()

def new_game():
   messagebox.showinfo("New Game", "New Game")
def save_game():
    filename = askopenfilename() #returns an absolute path to the file
    messagebox.showinfo("filename", filename)
def about():
   messagebox.showinfo( "About this page", "About this page")
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Game", menu=filemenu)
filemenu.add_command(label="New", command=new_game)
filemenu.add_command(label="Save", command=save_game)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about)

mainloop()