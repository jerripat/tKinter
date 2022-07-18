from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Popup Boxs")
root.geometry("400x400")
# root.iconbitmap('owl2.ico')
# img = PhotoImage()

# Create popup


def popup():
    response = messagebox.askyesnocancel("Info Popup", "This is my popup!!")
    my_label = Label(root, text=response).pack(pady=10)


# Pop up Boxs
# showinfo, showwarning,show,error,askquestion, askokcancel,askyesno
pop_button = Button(root, text="Click to pop up", command=popup).pack(pady=20)

root.mainloop()
