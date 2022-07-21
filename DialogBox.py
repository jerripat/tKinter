from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("New Window")
root.geometry("400x400")
#root.iconbitmap(r'python.ico')

text_file=filedialog.askopenfile(initialdir='/home/jerripat/PythonProjects/guis/tKinter',title='Dialog Window',filetypes=( ( 'All files', '*.*' )))
    
#     my_label = Label(root, text=root.filename).pack(pady=10) 
#     my_img = ImageTk.PhotoImage(Image.open("light.jpg"))
#     img_label = Label(new, image=my_img).pack(pady=5)

    
# my_button = Button(root, text="Dialog Window", command=open_dialog).pack(pady=10)

#open_dialog()
root.mainloop()