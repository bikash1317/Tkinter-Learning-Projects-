
from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("Listbox ")

i = 1

def add():
    global i
    # While you are ACTIVE = the box which you have selected the next number will be displayed above that box 
    lbx.insert(ACTIVE, f"{i}")
    i+=1


lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of our listbox")

Button(root, text="Add Item", command=add).pack()




root.mainloop()
