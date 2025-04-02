from tkinter import *
from tkinter import colorchooser
root = Tk()
root.title("Color Chooser")
def choose_color():
    color = colorchooser.askcolor(title = "Choose Color:")
    print("Selected color: ", color[1])

button = Button(root, text = "Choose color", command = choose_color)
button.pack()

root.mainloop()
