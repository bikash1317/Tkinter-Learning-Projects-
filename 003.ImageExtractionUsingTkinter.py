
from tkinter import *
from PIL import Image, ImageTk

mahmudul_root = Tk()

mahmudul_root.geometry("1255x944")
# This is only for 'png' images 
#  photo = PhotoImage(file="1.png")
# varun_label = Label(image=photo)
# varun_label.pack()
# For Jpg Images

# This is for 'jpg' images 
image = Image.open("bikash2.jpg")
photo = ImageTk.PhotoImage(image)

varun_label = Label(image=photo)
varun_label.pack()



mahmudul_root.mainloop()
