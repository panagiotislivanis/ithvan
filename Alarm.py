from tkinter import *
import tkinter
from tkinter import ttk 
import customtkinter
from customtkinter import * 
import datetime as dt  
import time

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

class Alarm(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Reminders & Alarms")
        self.geometry(f"{800}x{580}")
        
         # Create a layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)
        
        def alarm_popup():
            popup = CTkToplevel()
            popup.title("Alarm")
            popup.geometry('400x350+900+400')
            popup.resizable(False, False)

            #alarm grid
            popup.grid_rowconfigure(0, weight=1)
            popup.grid_columnconfigure(0, weight=0)
            popup.grid_columnconfigure(1, weight=1)
            popup.grid_columnconfigure(2, weight=1)
            
            #get data
            def set_alarm():
                days.clear()
                if day1.get() == 1:
                    days.append("Monday")
                if day2.get() == 1:
                    days.append("Tuesday")
                if day3.get() == 1:
                    days.append("Wednesday")
                if day4.get() == 1:
                    days.append("Thursday")
                if day5.get() == 1:
                    days.append("Friday")
                if day6.get() == 1:
                    days.append("Saturday")
                if day7.get() == 1:
                    days.append("sunday")
                if day8.get() == 1:
                    days.append("Tomorrow")
                if day9.get() == 1:
                    days.append("Every Day")
                days.append(hour.get())
                days.append(minute.get())
                print(days, "  ", hour.get(), ":", minute.get())  #delete  
            
            #variables to store data
            hour = customtkinter.StringVar(value="00")
            minute = customtkinter.StringVar(value="00")
            days = []
            day1 = customtkinter.IntVar()
            day2 = customtkinter.IntVar()
            day3 = customtkinter.IntVar()
            day4 = customtkinter.IntVar()
            day5 = customtkinter.IntVar()
            day6 = customtkinter.IntVar()
            day7 = customtkinter.IntVar()
            day8 = customtkinter.IntVar()
            day9 = customtkinter.IntVar()
            
            #day picker
            popup.monday = customtkinter.CTkCheckBox(popup, text="Monday", variable=day1, onvalue="1", offvalue="")
            popup.monday.place(relx=0.15, rely=0.04, anchor=tkinter.CENTER)
            popup.checkbox = customtkinter.CTkCheckBox(popup, text="Tuesday", variable=day2, onvalue="1", offvalue="")
            popup.checkbox.place(relx=0.375, rely=0.04, anchor=tkinter.CENTER)
            popup.checkbox = customtkinter.CTkCheckBox(popup, text="Wednesday", variable=day3, onvalue="1", offvalue="")
            popup.checkbox.place(relx=0.625, rely=0.04, anchor=tkinter.CENTER)
            popup.checkbox = customtkinter.CTkCheckBox(popup, text="Thursday", variable=day4, onvalue="1", offvalue="")
            popup.checkbox.place(relx=0.90, rely=0.04, anchor=tkinter.CENTER)
            popup.checkbox = customtkinter.CTkCheckBox(popup, text="Friday", variable=day5, onvalue="1", offvalue="")
            popup.checkbox.place(relx=0.275, rely=0.135, anchor=tkinter.CENTER)
            popup.checkbox = customtkinter.CTkCheckBox(popup, text="Saturday", variable=day6, onvalue="1", offvalue="")
            popup.checkbox.place(relx=0.52, rely=0.135, anchor=tkinter.CENTER)
            popup.checkbox = customtkinter.CTkCheckBox(popup, text="Sunday", variable=day7, onvalue="1", offvalue="")
            popup.checkbox.place(relx=0.76, rely=0.135, anchor=tkinter.CENTER)
            popup.checkbox = customtkinter.CTkCheckBox(popup, text="Tomorrow", variable=day8, onvalue="1", offvalue="")
            popup.checkbox.place(relx=0.375, rely=0.235, anchor=tkinter.CENTER)
            popup.checkbox = customtkinter.CTkCheckBox(popup, text="Every Day", variable=day9, onvalue="1", offvalue="")
            popup.checkbox.place(relx=0.64, rely=0.235, anchor=tkinter.CENTER)
            
            #hour picker
            alarm1 = customtkinter.CTkOptionMenu(popup, values=["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"], font=('Arial', 100), variable=hour)
            alarm1.grid(row=0, column=0, columnspan=1, padx=15, pady=10)
            popup.dots = customtkinter.CTkLabel(popup, text=":", font=('Arial',70), fg_color='transparent')
            popup.dots.grid(row=0, column=1, padx=0, pady=90, sticky="nsew")
            #minutes picker
            alarm2 = customtkinter.CTkOptionMenu(popup, values=["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                                               "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47","48","49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"], font=('Arial', 100), variable=minute)
            alarm2.grid(row=0, column=3, columnspan=1, padx=15, pady=90)
                
            #setting button
            popup.set_button = customtkinter.CTkButton(popup, text="Set alarm", fg_color='midnight blue', cursor="hand2", command=set_alarm)
            popup.set_button.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)
            
            popup.mainloop()
                            
                 
        self.main_button = customtkinter.CTkButton(self, text="Add reminder", fg_color='midnight blue', cursor="hand2", command=alarm_popup)
        self.main_button.grid(row=0, column=0, rowspan=1, columnspan=1, padx=10, pady=10, sticky="nsew")
        


if __name__ == "__main__":
    app = Alarm()
    app.mainloop()