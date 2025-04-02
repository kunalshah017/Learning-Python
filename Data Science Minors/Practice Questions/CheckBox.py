from tkinter import *

root = Tk()

chk1 = Checkbutton(root, text='Check button 1')
chk2 = Checkbutton(root, text='Check button 2')

chk1.pack(expand=True)
chk2.pack(expand=True)

root.geometry('500x500')

root.mainloop()