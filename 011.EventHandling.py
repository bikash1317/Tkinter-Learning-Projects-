
from tkinter import *
root = Tk()
root.title("Events in Tkinter")
root.geometry("644x334")

def Bikash(event):
    print(f"You clicked on the button at {event.x}, {event.y}")



widget = Button(root, text='Click me please',font="while")
widget.pack()

widget.bind('<Button-1>', Bikash)
widget.bind('<Double-1>', quit)

root.mainloop()
