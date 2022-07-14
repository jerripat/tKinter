
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Combo Boxs")
root.geometry("400x400")
# root.iconbitmap('owl2.ico')
# img = PhotoImage()

def select():
    answer = my_combo.get()
    my_label = Label(root, text= 'You clicked :' + answer).pack(pady=10)

options = [

    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

my_combo = ttk.Combobox(root, value=options)
my_combo.current(0)
my_combo.pack(pady=10)
my_button = Button(root, text='Select', command=select).pack(pady=10)

root.mainloop()
