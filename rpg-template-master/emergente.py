from tkinter import *
from tkinter import messagebox as MessageBox

def test():
    MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje

root = Tk()

Button(root, text = "Clícame", command=test).pack()

root.mainloop()