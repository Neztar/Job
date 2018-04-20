from tkinter import *

def testtb12(event):
    username = tb1.get()
    password = tb2.get()
    print(username)
    print(password)

#Screen
gui=Tk()
gui.geometry("800x600")
gui.title("Test Gui")
#Label
l1=Label(text="Username : ")
l1.grid(row=0)
l2=Label(text="Password : ")
l2.grid(row=1)
#Textbox
tb1=Entry()
tb1.grid(row=0,column=1)
tb2=Entry()
tb2.grid(row=1,column=1)
#Button
b1=Button(text="Login")
b1.grid(row=2,column=1)
b1.bind('<Button-1>',testtb12)
gui.mainloop()