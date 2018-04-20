from tkinter import *

root = Tk()
root.grid()

v = StringVar()
Radiobutton(root, text = "Test RadioButton 1", variable=v, value="1").grid(row = 0, column = 0, sticky = W)
Radiobutton(root, text = "Test RadioButton 2", variable=v, value="2").grid(row = 1, column = 0, sticky = W)

root.mainloop()