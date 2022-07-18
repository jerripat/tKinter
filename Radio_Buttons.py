
from tkinter import *


root = Tk()
root.title = ("Radio Buttons")
root.geometry("400x400")
root.iconbitmap('owl2.ico')
img = PhotoImage()
# Radio Buttons
def radio():
    if rad.get() == 1:
          my_label = Label(root, text='You clicked radio button 1').pack(pady=5)
    else:
          my_label = Label(root, text='You clicked radio button 2').pack(pady=5) 
    

rad = IntVar()
rbutton_1 = Radiobutton(root, text="One", variable=rad, value=1).pack()
rbutton_2 = Radiobutton(root, text="Two", variable=rad, value=2).pack()

my_button = Button(root, text="Click me", command=radio).pack(pady=20)


root.mainloop()
