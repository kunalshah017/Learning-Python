from tkinter import *
from tkinter import ttk

def on_select(event):
    selected_item = combo_box.get()
    label.config(text = 'Selected Item' +selected_item)

root = Tk()
root.title("Combo Box Example")

label = Label(root, text = "Selected Item: ")
label.pack(pady = 10)

combo_box = ttk.Combobox(root, values = ["Option 1", "Option 2", "Option 3"])
combo_box.pack(pady = 5)
combo_box.set("Option 1")

root.mainloop()