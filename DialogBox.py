from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title("New Window")
root.geometry("400x400")
#root.iconbitmap(r'python.ico')
root.filename = filedialog.askopenfilename(initialdir='PythonProjects/ShellScripts', \
    title= 'Dialog Window', \
  filetypes=( ("Python File", "*.py"), \
  ( "All files", "*.*" )))

root.mainloop()