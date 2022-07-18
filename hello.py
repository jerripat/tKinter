from tkinter import  *
from tkinter import messagebox

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
option_menu = {
    
    1: 'Option 1' ,
    2: 'Option 2' ,
    3: 'Option 3' 
}
   
def print_options():
    
     for key in option_menu.keys():
        
         options_label  = print(key , '--------' , option_menu[key])
   
root = Tk()
root.geometry("500x500")

root.title("Conversions")
menu_label = Label(root, text="Menu Options",fg="blue",font=("monospace",13)).pack()
my_button = Button(root, text="Click Me!", command=print_options).pack(pady=20)


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)



root.config(menu=menubar)
root.mainloop()