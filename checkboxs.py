
from tkinter import *

root = Tk()
root.title("Check Boxs")
root.geometry("440x440")
#root.iconbitmap()


def toppings():
    if cb.get() == "Ex Cheese":
        top_label = Label(root, text="You do not want extra cheese?")
    else:
        top_label = Label(root, text="You do want extra cheese?")
    

cb = StringVar()


my_check = Checkbutton(root, text="Pepperoni", variable=cb,
                       onvalue="Pepperoni", offvalue="No Pepperoni")
my_check.deselect()
my_check.pack()
# my_check = Checkbutton(root, text="Extra Cheese", variable=cb,
#                        onvalue="Ex Cheese", offvalue="No Ex Cheese")
# my_check.deselect()
# my_check.pack()

top_button = Button(root,text= 'Select Toppings', command=toppings).pack(pady=10)


root.mainloop()
