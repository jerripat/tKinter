
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Radio Button Demo")
root.geometry("400x400")
root.resizable(False, False)


def show_selected_size():
    showinfo(title='Result', message=selected_size.get())


selected_size = tk.StringVar()
sizes = (('Small', 'S'),
         ('Medium', 'M'),
         ('Large', 'L'),
         ('Extra Large', 'XL'),
         ('Extra Extra Large', 'XXL'))


def show():
    file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)


def hide():
    file_frame.grid_forget()


def new():

    hide_menu_frames()
    current_status.set("File Status")

    file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)


def cut():
    current_status.set("Cut Status")
    hide_menu_frames()
    edit_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)


def hide_menu_frames():
    edit_frame.grid_forget()
    file_frame.grid_forget()


def fake_command():
    pass


my_menu = Menu(root)
root.config(menu=my_menu)

current_status = StringVar()
current_status.set("Waiting")
rad = IntVar()

# rbutton_1 = tk.RadioButton(root, text="One", variable=rad, value=1)
# rbutton_2 = tk.RadioButtonGroup(root, text="Two", variable=rad, value=2)
# rbutton_3 = tk.RadioButton(root, text="Three", variable=rad, value=3)


file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_separator()
edit_menu.add_command(label="Exit", command=root.quit)

choice_menu = Menu(my_menu)
my_menu.add_cascade(label="Conversion", menu=choice_menu)
choice_menu.add_command(label="cm -> mm", command=fake_command)
choice_menu.add_command(label="mm -> inch", command=fake_command)
choice_menu.add_command(label="inch -> mm", command=fake_command)
choice_menu.add_command(label="inch -> cm", command=fake_command)
choice_menu.add_command(label="mm -> feet", command=fake_command)
choice_menu.add_command(label="feet -> mm", command=fake_command)
choice_menu.add_separator()
choice_menu.add_command(label="Exit", command=root.quit)

# show_button = Button(root, text="Show", command=show)
# hide_button = Button(root, text="Hide", command=hide)

# show_button.grid(row=2, column=0)
# hide_button.grid(row=2, column=1)

# File Menu frame
file_frame = Frame(root, width=200, height=200, bd=2,
                   bg="#c9ae63", relief="groove")
#file_frame.grid(row=1,column=0, columnspan=2, padx=20, pady=20)
file_frame_label = Label(file_frame, textvariable="File Frame").pack(padx=20, pady=20)

# Edit Menu Frame
edit_frame = Frame(root, width=200, height=200, bd=2,
                   bg="#c9ae63", relief="groove")
#file_frame.grid(row=1,column=0, columnspan=2, padx=20, pady=20)
edit_frame_label = Label(edit_frame, textvariable="Cut Frame").pack(padx=20, pady=20)


status_bar = Label(root, textvariable=current_status, bd=2,
                   relief="sunken", width=50).grid(row=3, column=0)


root.mainloop()
