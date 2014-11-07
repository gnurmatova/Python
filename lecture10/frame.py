import tkinter

base = tkinter.Tk()
base.title("frame example")

frame = tkinter.Frame(base)
frame.pack()

btn1 = tkinter.Button(frame, text="One")
btn2 = tkinter.Button(frame, text="Two")
btn3 = tkinter.Button(frame, text="Three")

btn1.pack(side=tkinter.RIGHT)
btn2.pack(side=tkinter.BOTTOM)
btn3.pack(side=tkinter.TOP)


frame2 = tkinter.Frame(base)
frame2.pack()

btn1 = tkinter.Button(frame2, text="One")
btn2 = tkinter.Button(frame2, text="Two")
btn3 = tkinter.Button(frame2, text="Three")
btn4 = tkinter.Button(frame2, text="Four")
btn5 = tkinter.Button(frame2, text="Five")

btn1.pack(side=tkinter.RIGHT)
btn2.pack(side=tkinter.RIGHT)
btn3.pack(side=tkinter.RIGHT)
btn4.pack(side=tkinter.RIGHT)
btn5.pack(side=tkinter.RIGHT)

base.mainloop()