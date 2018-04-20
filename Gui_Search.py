from tkinter import *


def getvalue(event):
    sec1 = vartype.get()
    sec2 = varedu.get()
    word_get = word_entry.get()
    thai = "ไทย " + langthai.get()
    eng = "อังกฤษ " + langEng.get()
    query = sec1 + " " + sec2 + " " + word_get + thai + " " + eng
    print(query)


# Screen
gui_search = Tk()
gui_search.geometry("300x250")
gui_search.title("Search")
    # ตำแหน่งงานที่จะรับ
# label
typeLabel = Label(text="ตำแหน่งงานที่จะรับ")
typeLabel.grid(row=0, column=0)
# drop down menu
typemenu = ["กฎหมาย", "การตลาด", "บัญชี/การเงิน", "คลังสินค้า/โลจิสติกส์", "งานบันเทิง/นักแสดง/นักร้อง/นางแบบ",
            "บริการลูกค้า/Call Center", "ศิลปะ/กราฟฟิค/ออกแบบ/ช่างภาพ", "ผู้จัดการ/ผู้อำนวยการ",
            "คอมพิวเตอร์/โปรแกรมเมอร์", "นักเขียน/บรรณาธิการ/นักแปลภาษา", "ล่าม/มัคคุเทศก์", "วิทยาศาสตร์/วิจัยพัฒนา",
            "วิศวกร", "สื่อสารมวลชน", "ออกแบบเว็บไซต์", "เลขานุการ", "สิ่งแวดล้อม/เจ้าหน้าที่ความปลอดภัย",
            "แพทย์/เภสัชกร", "โยธา/สถาปัตย์/ประเมินราคา", "อัญมณีและเครื่องประดับ"]
vartype = StringVar(gui_search)
vartype.set(typemenu[0])
typedrop = OptionMenu(gui_search, vartype, *typemenu)
typedrop.config(width=25, bg="white")
typedrop["menu"].config(bg="white")
typedrop.grid(row=0, column=1)

    # ระดับการศึกษา
# label
eduLabel = Label(text="ระดับการศึกษา")
eduLabel.grid(row=1, column=0)
# drop down menu
edumenu = ["ปริญญาตรี", "สูงกว่าปริญญาตรี", "ต่ำกว่าปริญญาตรี"]
varedu = StringVar(gui_search)
varedu.set(edumenu[0])
edudrop = OptionMenu(gui_search, varedu, *edumenu)
edudrop.config(width=25, bg="white")
edudrop["menu"].config(bg="white")
edudrop.grid(row=1, column=1)

    # ประเภทงานที่ต้องการ
# label
specLabel = Label(text="ประเภทงานที่จะรับ")
specLabel.grid(row=2, column=0)
# drop dowm menu
specmenu = ["ประจำ", "พาร์ทไทม์", "ฟรีแลนซ์", "ฝึกงาน"]
varspec = StringVar(gui_search)
varspec.set(specmenu[0])
specdrop = OptionMenu(gui_search, varspec, *specmenu)
specdrop.config(width=25, bg="white")
specdrop["menu"].config(bg="white")
specdrop.grid(row=2, column=1)

    # ความสามารถทางภาษา
#label
langLabel = Label(text="ความสามารถทางภาษา")
langLabel.grid(row=3, column=1)
    # ไทย
# label
langThaiLabel = Label(text="ภาษาไทย")
langThaiLabel.grid(row=4, column=0)
# Radio Button
langthai = StringVar()
langthai.set(' ')
langthaiRadio1 = Radiobutton(text="เยี่ยม", variable=langthai, value="เยี่ยม").grid(row=4, column=1, sticky=W)
langthaiRadio2 = Radiobutton(text="ดี", variable=langthai, value="ดี").grid(row=4, column=1, sticky=S)
langthaiRadio3 = Radiobutton(text="พอใช้", variable=langthai, value="พอใช้").grid(row=4, column=1, sticky=E)
    # อังกฤษ
# label
langEngLabel = Label(text="อังกฤษ")
langEngLabel.grid(row=5, column=0)
# Radio Button
langEng = StringVar()
langEng.set(' ')
langEngRadio1 = Radiobutton(text="เยี่ยม", variable=langEng, value="เยี่ยม").grid(row=5, column=1, sticky=W)
langEngRadio2 = Radiobutton(text="ดี", variable=langEng, value="ดี").grid(row=5, column=1, sticky=S)
langEngRadio3 = Radiobutton(text="พอใช้", variable=langEng, value="พอใช้").grid(row=5, column=1, sticky=E)

    # คำค้นหา
# label
word_search = Label(text="คำค้นหา")
word_search.grid(row=6, column=0)
# Entry
word_entry = Entry()
word_entry.config(width=30)
word_entry.grid(row=6, column=1)

#search button
searchButton = Button(text="Search")
searchButton.bind('<Button-1>', getvalue)
searchButton.grid(row=7, column=1, pady=(10, 0))
gui_search.mainloop()
