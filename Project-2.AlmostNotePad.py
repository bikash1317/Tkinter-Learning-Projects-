from tkinter import *
root = Tk()
root.geometry("800x1200")
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(root, yscrollcommand = scrollbar.set)
text.pack(fill="both")
scrollbar.config(command=text.yview)
root.mainloop()