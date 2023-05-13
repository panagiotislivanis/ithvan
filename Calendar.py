import customtkinter
from customtkinter import *
from tkinter import *
from tkcalendar import *


root = Tk()
root.title('Calendar')
root.geometry("600x400")
p1 = PhotoImage(file = 'Resources-img\calendar.png')
root.iconphoto(False, p1)

cal = Calendar(root, selectmode="day", year=2023, monh=5, day=13)
cal.pack(ipadx=20)

def grab_date():
    my_label.config(text="Today's Date is " +cal.get_date())

my_button = Button(root, text="Add Event", command=grab_date)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)


root.mainloop()
