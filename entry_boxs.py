
from tkinter import *

root = Tk()
root.title("Entry Boxs")
root.geometry("400x400")

def clicked():
    my_label2 = Label(root, text=e.get())
    my_label2.pack()
    
    
my_label = Label(root, text="Enter your name: ")
my_label.pack()
    
e = Entry(root,font=("Helvetica",16))
e.pack(pady=20)
my_button = Button(root, text="Click Me!", command=clicked)
my_button.pack(pady=20)


root.mainloop()