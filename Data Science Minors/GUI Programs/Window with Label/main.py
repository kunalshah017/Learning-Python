import tkinter as tk

root = tk.Tk()
root.title("Window with Label")
root.geometry("400x300")

label = tk.Label(root, text="Hello, World!")
label.pack()

root.mainloop()