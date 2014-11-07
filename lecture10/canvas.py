import tkinter


base = tkinter.Tk()
base.title("canvas example")
canvas = tkinter.Canvas(base, bg="white", height=250, width=300)
canvas.pack()

canvas.create_line(0, 100, 100, 100, fill="black") #x, y to x, y
canvas.create_oval(10, 10, 50, 50, fill="red", outline="green")
canvas.create_oval(100, 100, 150, 150, outline="green")
canvas.create_polygon(0, 100, 100, 150, 200, 250, outline="green", fill="white")

points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
canvas.create_polygon(points, outline="black",fill='yellow', width=3)


canvas.create_line(0, 0, canvas["height"], canvas["width"], fill="black") #x, y to x, y
base.mainloop()

