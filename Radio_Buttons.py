
from tkinter import *


root = Tk()
root.title = ("Radio Buttons")
root.geometry("400x400")
#root.iconbitmap('/guis/tKinter/owl2.ico')

# Radio Buttons
rad = IntVar()
rbutton_1 = Radiobutton(root, text="One", variable=rad, value=1).pack()
rbutton_2 = Radiobutton(root, text="Two", variable=rad, value=2).pack()


root.mainloop()
