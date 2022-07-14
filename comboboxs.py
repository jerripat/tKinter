
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Combo Boxs")
root.geometry("400x400")
# root.iconbitmap('owl2.ico')
# img = PhotoImage()

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


root.mainloop()
