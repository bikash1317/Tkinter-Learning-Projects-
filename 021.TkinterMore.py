from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("Bikash_Kumar_Dash - Title Of My GUI")
# root.wm_iconbitmap("1.ico")  # Setting the icon 
root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close", command = root.destroy).pack()    # To destroy/close the button here 

root.mainloop()
