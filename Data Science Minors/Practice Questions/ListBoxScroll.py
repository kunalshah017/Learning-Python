from tkinter import *

root = Tk()

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

listB = Listbox(root ,yscrollcommand=scroll.set)
for i in range(30):
    listB.insert(END, f'this is line {i}')

listB.pack()
scroll.config(command=listB.yview)

root.mainloop()