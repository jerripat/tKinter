from tkinter import *
from tkinter import ttk
from PIL import Image


root = Tk()
root.title("New Window")
root.geometry("400x400")

im = Image.open('owl2.ico')
im.show()
root.iconbitmap('wm',im)
# img = PhotoImage()


def open_window():
    new =Toplevel()
    new.title("New Sub-Window")
    new.geometry("300x300")
    # root.iconbitmap('owl2.ico')
    # img = PhotoImage('')
    my_label = Label(new, text="My fancy new window").pack(pady=20)
    destroy_button = Button(new, text='Quit',command=new.destroy).pack()
    
    # Minimize original window
    #hide_button = Button(new, text = 'Hide Main Window',command=root.iconify).pack(pady=10)
    #show_button = Button(new, text = 'Show Main Window',command=root.deiconify).pack(pady=10)
    # Withdraw Original window
    hide_button = Button(new, text = 'Hide Main Window',command=root.withdraw).pack(pady=10)
    show_button = Button(new, text = 'Show Main Window',command=root.deiconify).pack(pady=10)
    kill_original = Button(new, text='Quit Original',command=root.destroy ).pack(pady=10)
    new.mainloop()
my_button = Button(root, text="Open 2nd window",command=open_window).pack(pady=10)




root.mainloop()