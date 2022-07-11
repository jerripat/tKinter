from tkinter import *

root = Tk()
root.title("Frames")
root.geometry("400x400")


def show():
    file_frame.grid(row=1,column=0, columnspan=2, padx=20, pady=20)
def hide():
    file_frame.grid_forget()
    
def new():
    hide_menu_frames()
    file_frame.grid(row=1,column=0, columnspan=2, padx=20, pady=20)

def cut():
    hide_menu_frames()
    edit_frame.grid(row=1,column=0, columnspan=2, padx=20, pady=20)
    
def hide_menu_frames():
    edit_frame.grid_forget()
    file_frame.grid_forget()
        
def fake_command():
    pass

my_menu = Menu(root)
root.config(menu=my_menu)

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
file_frame = Frame(root, width=200, height=200, bd=2, bg="#c9ae63", relief="groove")
#file_frame.grid(row=1,column=0, columnspan=2, padx=20, pady=20)
file_frame_label= Label(file_frame, text="File Frame").pack(padx=20, pady=20)

# Edit Menu Frame
edit_frame = Frame(root, width=200, height=200, bd=2, bg="#c9ae63", relief="groove")
#file_frame.grid(row=1,column=0, columnspan=2, padx=20, pady=20)
edit_frame_label= Label(edit_frame, text="Cut Frame").pack(padx=20, pady=20)





root.mainloop()