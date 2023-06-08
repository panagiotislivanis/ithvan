from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import customtkinter
from customtkinter import *
from tkcalendar import Calendar
from datetime import datetime

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

root = Tk()
root.title("Calendar")
p1 = PhotoImage(file = 'Resources-img\calendar.png')
root.iconphoto(False, p1)
width = 300
height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#242424")

#============================VARIABLES===================================
EVENT_NAME = StringVar()
EVENT_START = StringVar()
EVENT_END = StringVar()
DATE = StringVar()



#============================METHODS=====================================

def Database():
    conn = sqlite3.connect("calendar.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, Eventname TEXT, date TEXT, startTime TEXT, endTime TEXT)")
    fetch = cursor.fetchall()
    cursor.execute("SELECT * FROM `member` ORDER BY `startTime` ASC")
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SubmitData():
    if  EVENT_NAME.get() == "" or EVENT_START.get() == "" or EVENT_END.get() == "" or DATE.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("calendar.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `member` (Eventname, date, startTime, endTime) VALUES(?, ?, ?, ?)", (str(EVENT_NAME.get()), str(EVENT_START.get()), int(EVENT_END.get()), str(DATE.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `startTime` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        EVENT_NAME.set("")
        EVENT_START.set("")
        EVENT_END.set("")
        DATE.set("")

def UpdateData():
    if DATE.get() == "":
       result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `member` SET `Eventname` = ?, `date` = ?, `startTime` = ?,  `endTime` = ? WHERE `mem_id` = ?", (str(EVENT_NAME.get()), str(EVENT_START.get()), str(EVENT_END.get()), str(DATE.get()), int(mem_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `startTime` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        EVENT_NAME.set("")
        EVENT_START.set("")
        EVENT_END.set("")
        DATE.set("")
        
    
def OnSelected(event):
    global mem_id, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    EVENT_NAME.set("")
    EVENT_START.set("")
    EVENT_END.set("")
    DATE.set("")
    EVENT_NAME.set(selecteditem[1])
    EVENT_START.set(selecteditem[2])
    EVENT_END.set(selecteditem[3])
    DATE.set(selecteditem[4])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Calencar")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()

    #===================FRAMES==============================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Updating Event", font=('arial', 16), bg="orange",  width = 300)
    lbl_title.pack(fill=X)
    lbl_eventname = Label(ContactForm, text="Event name", font=('arial', 14), bd=5)
    lbl_eventname.grid(row=0, sticky=W)
    lbl_dateofevent = Label(ContactForm, text="Date Happening", font=('arial', 14), bd=5)
    lbl_dateofevent.grid(row=1, sticky=W)
    lbl_starttime = Label(ContactForm, text="Event Start", font=('arial', 14), bd=5)
    lbl_starttime.grid(row=3, sticky=W)
    lbl_endtime = Label(ContactForm, text="Event End", font=('arial', 14), bd=5)
    lbl_endtime.grid(row=4, sticky=W)

    #===================ENTRY===============================
    eventname = Entry(ContactForm, textvariable=EVENT_NAME, font=('calibri', 14))
    eventname.grid(row=0, column=1)
    dateofevent = Entry(ContactForm, textvariable=DATE, font=('calibri', 14))
    dateofevent.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    starttime = Entry(ContactForm, textvariable=EVENT_START,  font=('calibri', 14))
    starttime.grid(row=3, column=1)
    endtime = Entry(ContactForm, textvariable=EVENT_END,  font=('calibri', 14))
    endtime.grid(row=4, column=1)
    

    #==================BUTTONS==============================
    btn_updatecon = Button(ContactForm, text="Update", width=50, command=UpdateData)
    btn_updatecon.grid(row=6, columnspan=2, pady=10)


#fn1353p    
def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please first select an event to delete!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("calendar.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `member` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def AddNewWindow():
    global NewWindow
    EVENT_NAME.set("")
    EVENT_START.set("")
    EVENT_END.set("")
    DATE.set("")
    NewWindow = Toplevel()
    NewWindow.title("Calendar")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
   
    #===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Adding New Event", font=('arial', 16), bg="#B9B2C5",  width = 300)
    lbl_title.pack(fill=X)
    lbl_eventname = Label(ContactForm, text="Event name", font=('arial', 14), bd=5)
    lbl_eventname.grid(row=0, sticky=W)
    lbl_dateofevent = Label(ContactForm, text="Date of the event", font=('arial', 14), bd=5)
    lbl_dateofevent.grid(row=1, sticky=W)
    lbl_tel = Label(ContactForm, text="Start time", font=('arial', 14), bd=5)
    lbl_tel.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="End Time", font=('arial', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)

    #===================ENTRY===============================
    eventname = Entry(ContactForm, textvariable=EVENT_NAME, font=('arial', 14))
    eventname.grid(row=0, column=1)
    dateofevent = Entry(ContactForm, textvariable=DATE, font=('arial', 14))
    dateofevent.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    starttime = Entry(ContactForm, textvariable=EVENT_START,  font=('arial', 14))
    starttime.grid(row=3, column=1)
    endtime = Entry(ContactForm, textvariable=EVENT_END,  font=('arial', 14))
    endtime.grid(row=4, column=1)
    

    #==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="Save", width=50, command=SubmitData)
    btn_addcon.grid(row=6, columnspan=2, pady=10)




    
#============================FRAMES======================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500,  bg="#72BFF4")
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=500)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="#72BFF4")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
MidBottom = Frame(Mid, width=100)
MidBottom.pack(side=BOTTOM, pady=10)
MidBottomPadding = Frame(Mid, width=370, bg="#72BFF4")
MidBottomPadding.pack(side=BOTTOM)
TableMargin = Frame(root, width=200)
TableMargin.pack(side=TOP)
#============================LABELS======================================
lbl_title = Label(Top, text="Calendar", font=('arial', 16), width=500,bg="#242424", fg="#72BFF4")
lbl_title.pack(fill=X)

#============================ENTRY=======================================

#============================BUTTONS=====================================
btn_add = Button(MidLeft, text="+ ADD NEW", bg="#66ff66", command=AddNewWindow)
btn_add.pack(side=LEFT)
btn_delete = Button(MidRight, text="DELETE", bg="red", command=DeleteData)
btn_delete.pack(side=RIGHT)

            

#============================TABLES======================================
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("MemberID", "Event name", "Date of the event", "Start time", "End Time"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemberID', text="MemberID", anchor=W)
tree.heading('Event name', text="Event name", anchor=W)
tree.heading('Date of the event', text="Date of the event", anchor=W)
tree.heading('Start time', text="Start time", anchor=W)
tree.heading('End Time', text="End Time", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=120)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

cal = Calendar(MidBottom, selectmode="day", year=2023, month=5, day=26)


#============================INITIALIZATION==============================
if __name__ == '__main__':
    Database()
    root.mainloop()
    