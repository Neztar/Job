from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
import sys

def hello(event):
    #Dialog box
    #messagebox.showinfo(title="แสดงข้อความ",message="Hello User!")
    #messagebox.showwarning(title="แจ้งเตือน",message="ระวัง!")
    #messagebox.askquestion(title="กรุณายืนยัน",message="แน่ใจนะ")
    #messagebox.askokcancel(title="กรุณายืนยัน",message="แน่ใจนะ")
    status = messagebox.askyesno(title="คำยืนยัน",message="คุณต้องการออกจากโปรแกรมหรือไม่")
    if status>0 :
        x = sex.get()
        print(x)
        sys.exit()

def fColor(event):
    #Color Dialog
    Color = colorchooser.askcolor()
    print(Color)
def fOpen(event):
    #File Dialog
    File = filedialog.askopenfile()
    print(File)
#Screen
gui=Tk()
gui.geometry("800x600")
gui.title("Test Gui")
#Label
name_label=Label(text="ชื่อ",fg="black",font=("Times",20)).pack(side="left")
#Button
ok_button=Button(text="submit").pack()
b1=Button(text="Hello")
b1.bind('<Button-1>',hello)
b1.pack()
b2=Button(text="Color")
b2.bind('<Button-1>',fColor)
b2.pack()
b3=Button(text="Select File:")
b3.bind('<Button-1>',fOpen)
b3.pack()
#Entry
name_textbox=Entry().pack()
#Menu
jobbar=Menu(gui)
    #file
filemenu=Menu(jobbar,tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save...As")
filemenu.add_command(label="Close")
    #help
helpmenu=Menu(jobbar,tearoff=0)
helpmenu.add_command(label="Contact")
helpmenu.add_command(label="Document")

jobbar.add_cascade(label="File",menu=filemenu)
jobbar.add_cascade(label="Help",menu=helpmenu)
gui.config(menu=jobbar)

#Radio Button
sex=StringVar()
r1=Radiobutton(text="ชาย",variable=sex,value=1).pack()
r2=Radiobutton(text="หญิง",variable=sex,value=2).pack()
#SpinBox
spin=Spinbox(from_=1,to=10,state=DISABLED).pack()
#ListBox
l1=Listbox()
l1.insert(1,"Python")
l1.insert(2,"Java")
l1.insert(3,"Database")
l1.pack()
#Slider
s1=Scale(orient=HORIZONTAL,width=20,length=300,from_=0,to=100,tickinterval=10)
s1.pack()

gui.mainloop()
