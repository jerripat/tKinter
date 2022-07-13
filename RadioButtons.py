
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.title("Radio Button Demo")
root.geometry("400x400")
root.resizable(False, False)
img = PhotoImage(file='owl2.ico')
root.tk.call('wm', 'iconphoto', root._w, img)

def show_selected_size():
    showinfo(title='Result', message=selected_size.get())


selected_size = tk.StringVar()

sizes = (('Small', 'S'),
         ('Medium', 'M'),
         ('Large', 'L'),
         ('Extra Large', 'XL'),
         ('Extra Extra Large', 'XXL'))

# label
label = ttk.Label(text="What's your t-shirt size?").grid(padx=5,
                                                         pady=5, column=0, row=0)
#label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_size
    )
    r.grid_configure(row=1, column=1, padx=5, pady=5)

# button
button = ttk.Button(
    root,
    text="Get Selected Size",
    command=show_selected_size)

button.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
