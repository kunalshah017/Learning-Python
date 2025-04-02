from tkinter import *
from tkinter import ttk

root = Tk()

cb = ttk.Combobox(root, values=['val1', 'val2', 'val3'])
cb.pack(expand=True)

root.geometry("500x500")
root.mainloop()