from tkinter import *
root=Tk()
root.geometry("700x400")

def update():
    print("updating the gui")
    root.geometry(f"{width.get()}x{heigth.get()}")

width=StringVar()
heigth=StringVar()

Entry(root,textvariable="width").pack()
Entry(root,textvariable="height").pack()
Button(root,text="Apply",command=update).pack()
root.mainloop()