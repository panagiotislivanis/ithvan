import sqlite3
from PIL import Image, ImageTk
import os
import tkinter
import subprocess
import tkinter.messagebox
import customtkinter
from customtkinter import *
from Calendar import CalendarApp
from Music import MusicPlayer
from Search import search_query
from News import NewsWidget
from traffic import TrafficWidget
import Alarm
from mail import EmailApp
from maps import Maps
from Music import MusicPlayer
# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class CustomCTk(customtkinter.CTk):
    def WM_Maximize(self):
        if not self.is_fullscreen:
            self.original_geometry = self.geometry()
            self.attributes("-fullscreen", True)
            self.is_fullscreen = True
        else:
            self.attributes("-fullscreen", False)
            self.geometry(self.original_geometry)
            self.is_fullscreen = False


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Configure window
        self.title("ITHVAN")
        self.geometry(f"{1100}x{950}")
        self.is_fullscreen = False
        # Create a layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Create tabview
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.tabview.add("Homepage")
        self.tabview.add("Timetable")
        self.tabview.add("Daily Manager")

        # -----------------------------------------------------------#
        # Create custom grid for homepage tab
        # For loop to make 11 columns.
        self.homepage_frame = self.tabview.tab("Homepage")
        for i in range(1, 15):
            self.homepage_frame.columnconfigure(i, weight=1)
        # For loop to make 11 rows.
        for i in range(1, 15):
            self.homepage_frame.rowconfigure(i, weight=1)

        # Widgets for homepage tab
        # Left upper / Music
        self.left_upper = MusicPlayer(self.homepage_frame)
        self.left_upper.grid(
            row=0, column=0, rowspan=2, columnspan=14, padx=10, pady=10, sticky="nsew"
        )

        # Left lower / Weather and traffic
        self.left_lower = TrafficWidget(self.homepage_frame)
        self.left_lower.grid(
            row=2, column=0, rowspan=13, columnspan=14, padx=10, pady=10, sticky="nsew"
        )
        # Right upper / Google search bar
        self.right_upper = customtkinter.CTkLabel(
            self.homepage_frame, text="Google search bar", fg_color="transparent"
        )
        self.right_upper.grid(
            row=0, column=14, columnspan=2, padx=10, pady=10, sticky="nsew"
        )
        # Add search bar
        # Load images with light and dark mode
        image_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "Resources-img"
        )
        # Search icon Dark/Light versions
        self.searchimage = customtkinter.CTkImage(
            dark_image=Image.open(os.path.join(image_path, "search-dark.png")),
            light_image=Image.open(os.path.join(image_path, "search-light.png")),
        )
        # Create search bar widget
        entry = customtkinter.CTkEntry(
            self.right_upper,
            placeholder_text="Search... [CHROME BROWSER]",
        )
        entry.bind("<Return>", lambda event: search_query(entry.get()))
        # Search button
        search_button = customtkinter.CTkButton(
            self,
            text="",
            image=self.searchimage,
            width=entry.cget("width") / 3,
            corner_radius=0,
            command=lambda: search_query(entry.get()),
        )
        search_button.place(
            in_=entry, relx=1.0, rely=0.0, relheight=1, anchor=customtkinter.NE
        )
        entry.place(relwidth=1, relheight=1.0)

        # Right lower / News exc
        # Replace this with your actual API key
        API_KEY = "46f1942a35684436a2eaa05b27fd06d8"
        self.right_lower = NewsWidget(self.homepage_frame, API_KEY)
        self.right_lower.grid(
            row=1, column=14, rowspan=14, columnspan=1, padx=10, pady=10, sticky="nsew"
        )

        # -----------------------------------------------------------#
        # Timetable Tab
        self.Timetable_frame = self.tabview.tab("Timetable")
        self.Timetable_frame.columnconfigure(0, weight=1)
        self.Timetable_frame.columnconfigure(1, weight=2)
        self.Timetable_frame.columnconfigure(2, weight=2)
        self.Timetable_frame.columnconfigure(3, weight=2)
        self.Timetable_frame.rowconfigure(0, weight=1)
        self.Timetable_frame.rowconfigure(1, weight=2)
        self.Timetable_frame.rowconfigure(2, weight=2)
        self.Timetable_frame.rowconfigure(3, weight=2)
        self.Timetable_frame.rowconfigure(4, weight=2)
        self.Timetable_frame.rowconfigure(5, weight=2)
        self.Timetable_frame.rowconfigure(6, weight=2)
        self.Timetable_frame.rowconfigure(7, weight=2)
        self.Timetable_frame.rowconfigure(8, weight=2)
        self.Timetable_frame.rowconfigure(9, weight=2)
        self.Timetable_frame.rowconfigure(10, weight=2)

        # Widgets for Timetable tab
        # Top / Scheduling and management of meetings
        Calendar_image = ImageTk.PhotoImage(
            Image.open("Resources-img\calendar.png").resize((25, 25), Image.ANTIALIAS)
        )

        self.left_upper = CTkFrame(self.Timetable_frame)
        self.left_upper.grid(
            row=0, column=0, rowspan=10, columnspan=1, padx=10, pady=10, sticky="nsew"
        )
        self.calendar_app = CalendarApp(self.left_upper)

        # email

        def open_email_app():
            app = customtkinter.CTk()
            app.title("Email App")
            app.geometry("500x650")
            email_app = EmailApp(app)
            email_app.pack(fill="both", expand=True)
            app.mainloop()

        mail_image = ImageTk.PhotoImage(
            Image.open("Resources-img\Mail.png").resize((25, 25), Image.ANTIALIAS)
        )

        self.right_upper = customtkinter.CTkButton(
            self.Timetable_frame, text="Email", fg_color='#4F02FF', cursor="hand2", image=mail_image,command=open_email_app)
        self.right_upper.grid(row=0, column=1, rowspan=3, columnspan=5,
                             padx=10, pady=10, sticky="nsew")
        #maps

        self.center_center = Maps(self.Timetable_frame)
        self.center_center.grid(
            row=3, column=1, rowspan=7, columnspan=5, padx=10, pady=10, sticky="nsew"
        )
        # Bottom

        # Calls
        def open_calls():
            subprocess.Popen(["python", "Call.py"])

        Calls_image = ImageTk.PhotoImage(
            Image.open("Resources-img\Calls.png").resize((25, 25), Image.ANTIALIAS)
        )
        self.left_center = customtkinter.CTkButton(
            self.Timetable_frame,
            text="Calls",
            fg_color="#49393B",
            cursor="hand2",
            image=Calls_image,
            command=open_calls,
        )
        self.left_center.grid(
            row=10, column=0, rowspan=2, columnspan=2, padx=10, pady=10, sticky="nsew"
        )

        # SMS
        def open_sms():
            subprocess.Popen(["python", "SMS.py"])

        SMS_image = ImageTk.PhotoImage(
            Image.open("Resources-img\Messages.png").resize((25, 25), Image.ANTIALIAS)
        )

        self.right_center = customtkinter.CTkButton(
            self.Timetable_frame,
            text="SMS",
            fg_color="#996888",
            cursor="hand2",
            image=SMS_image,
            command=open_sms,
        )
        self.right_center.grid(
            row=10, column=2, rowspan=2, columnspan=2, padx=10, pady=10, sticky="nsew"
        )

        # Organise and manage contacts
        def open_contacts():
            subprocess.Popen(["python", "Contacts.py"])

        Contacts_image = ImageTk.PhotoImage(
            Image.open("Resources-img\contacts.png").resize((25, 25), Image.ANTIALIAS)
        )
        self.left_lower = customtkinter.CTkButton(
            self.Timetable_frame,
            text="Manage contacts",
            fg_color="#3F826D",
            cursor="hand2",
            image=Contacts_image,
            command=open_contacts,
        )
        self.left_lower.grid(
            row=10, column=4, rowspan=2, columnspan=2, padx=10, pady=10, sticky="nsew"
        )

        # -----------------------------------------------------------#
        # Daily Manager
        self.dManager_frame = self.tabview.tab("Daily Manager")
        self.dManager_frame.columnconfigure(0, weight=1)
        self.dManager_frame.columnconfigure(1, weight=2)
        self.dManager_frame.columnconfigure(2, weight=2)
        self.dManager_frame.columnconfigure(3, weight=2)
        self.dManager_frame.columnconfigure(4, weight=2)
        self.dManager_frame.rowconfigure(0, weight=1)
        self.dManager_frame.rowconfigure(1, weight=2)
        self.dManager_frame.rowconfigure(2, weight=2)
        self.dManager_frame.rowconfigure(3, weight=2)
        self.dManager_frame.rowconfigure(4, weight=2)
        self.dManager_frame.rowconfigure(5, weight=2)
        self.dManager_frame.rowconfigure(6, weight=2)
        self.dManager_frame.rowconfigure(7, weight=2)
        self.dManager_frame.rowconfigure(8, weight=2)
        self.dManager_frame.rowconfigure(9, weight=2)
        self.dManager_frame.rowconfigure(10, weight=2)

        # Widgets for Daily Manager tab
        # Left upper / Task Manager
        def open_task_manager():
            subprocess.Popen(["python", "TaskManager.py"])

        self.left_upper = customtkinter.CTkButton(
            self.dManager_frame,
            text="Task Manager",
            fg_color="dark red",
            cursor="hand2",
            command=open_task_manager,
        )
        self.left_upper.grid(
            row=0, column=0, rowspan=3, columnspan=3, padx=10, pady=10, sticky="nsew"
        )

        # Left center / Navigator
        self.left_center = customtkinter.CTkButton(
            self.dManager_frame, text="Navigator", fg_color="green", cursor="hand2"
        )
        self.left_center.grid(
            row=3, column=0, rowspan=3, columnspan=2, padx=10, pady=10, sticky="nsew"
        )

        # Left lower / Device controler
        def open_device_controller():
            subprocess.Popen(["python", "DeviceControler.py"])

        self.left_lower = customtkinter.CTkButton(
            self.dManager_frame,
            text="Device Controler",
            fg_color="blue",
            cursor="hand2",
            command=open_device_controller,
        )
        self.left_lower.grid(
            row=6, column=0, rowspan=5, columnspan=2, padx=10, pady=10, sticky="nsew"
        )

        # Right upper / Reminder
        def open_alarm():
            subprocess.Popen(["python", "Alarm.py"])

        self.right_upper = customtkinter.CTkButton(
            self.dManager_frame,
            text="Reminders & Alarms",
            fg_color="coral",
            cursor="hand2",
            command=open_alarm,
        )
        self.right_upper.grid(
            row=0, column=3, rowspan=3, columnspan=2, padx=10, pady=10, sticky="nsew"
        )

        # Right lower / E-shop
        def open_shop():
            subprocess.Popen(["python", "MyShop.py"])

        self.right_lower = customtkinter.CTkButton(
            self.dManager_frame,
            text="Your shop",
            fg_color="light green",
            cursor="hand2",
            command=open_shop,
        )
        self.right_lower.grid(
            row=3, column=2, rowspan=8, columnspan=3, padx=10, pady=10, sticky="nsew"
        )
        # -----------------------------------------------------------#

        self.appearance_mode_label = customtkinter.CTkLabel(
            self.tabview, text="", anchor="w", padx=10
        )
        self.appearance_mode_label.grid(row=0, column=0, sticky="w")
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(
            self.tabview,
            values=["Dark", "Light", "System"],
            command=self.change_appearance_mode_event,
            width=10
)

        
        self.appearance_mode_optionmenu.grid(row=0, column=0, sticky="nw", padx=10)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
