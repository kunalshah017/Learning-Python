from tkinter import *

root = Tk()

btn = Button(root, text='Click Me')
btn.pack(expand=True)

button = Button(root, text = "Click Me", activebackground = "blue",
                activeforeground = "white")
button.pack()

root.geometry('500x500')
root.mainloop()