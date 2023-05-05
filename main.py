import sqlite3
from PIL import Image, ImageTk
import os
import tkinter
import tkinter.messagebox
import customtkinter
from customtkinter import *
from Widgets.Search_bar import SearchBar

from Alarm import Alarm

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("ITHVAN")
        self.geometry(f"{800}x{580}")

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
        self.homepage_frame = self.tabview.tab("Homepage")

        self.homepage_frame.columnconfigure(0, weight=1)
        self.homepage_frame.columnconfigure(1, weight=2)
        self.homepage_frame.rowconfigure(0, weight=1)
        self.homepage_frame.rowconfigure(1, weight=2)
        self.homepage_frame.rowconfigure(2, weight=2)
        self.homepage_frame.rowconfigure(3, weight=2)
        self.homepage_frame.rowconfigure(4, weight=2)
        self.homepage_frame.rowconfigure(5, weight=2)
        self.homepage_frame.rowconfigure(6, weight=2)
        self.homepage_frame.rowconfigure(7, weight=2)
        self.homepage_frame.rowconfigure(8, weight=2)
        self.homepage_frame.rowconfigure(9, weight=2)
        self.homepage_frame.rowconfigure(10, weight=2)

        # Widgets for homepage tab
        # Left upper / Music
        self.left_upper = customtkinter.CTkLabel(
            self.homepage_frame, text="Music", fg_color='pink')
        self.left_upper.grid(row=0, column=0, rowspan=2,
                             padx=10, pady=10, sticky="nsew")

        # Left lower / Weather and traffic
        self.left_lower = customtkinter.CTkLabel(
            self.homepage_frame, text="Weather traffic", fg_color='red')
        self.left_lower.grid(row=2, column=0, rowspan=9,
                             padx=10, pady=10, sticky="nsew")

        # Right upper / Google search bar
        self.right_upper = customtkinter.CTkLabel(
            self.homepage_frame, text="Google search bar", fg_color='transparent')
        self.right_upper.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        # Add search bar
        # Load images with light and dark mode
        image_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "Resources-img")
        # Search icon Dark/Light versions
        self.searchimage = customtkinter.CTkImage(
            dark_image=Image.open(os.path.join(image_path, "search-dark.png")), light_image=Image.open(os.path.join(image_path, "search-light.png")))
        # Create search bar widget
        entry = customtkinter.CTkEntry(
            self.right_upper, placeholder_text="Search...")
        # Search button
        search_button = customtkinter.CTkButton(
            self, text="", image=self.searchimage, width=entry.cget("width")/3, corner_radius=0)
        search_button.place(in_=entry, relx=1.0, rely=0.0, relheight=1,
                            anchor=customtkinter.NE)
        entry.place(relwidth=1, relheight=1.0)

        # Right lower / News exc
        self.right_lower = customtkinter.CTkLabel(
            self.homepage_frame, text="News", fg_color='green')
        self.right_lower.grid(row=1, column=1, rowspan=10,
                              padx=10, pady=10, sticky="nsew")

        # -----------------------------------------------------------#
        # Timetable Tab
        self.Timetable_frame = self.tabview.tab("Timetable")
        self.Timetable_frame.columnconfigure(0, weight=1)
        self.Timetable_frame.columnconfigure(1, weight=2)
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
        self.left_upper = customtkinter.CTkButton(
            self.Timetable_frame, text="Scheduling and management of meetings", fg_color='#4F02FF', cursor="hand2")
        self.left_upper.grid(row=0, column=0, rowspan=3, columnspan=3,
                             padx=10, pady=10, sticky="nsew")

        # Center / Calls and send text messages SMS
        self.left_center = customtkinter.CTkButton(
            self.Timetable_frame, text="Calls and send text messages SMS", fg_color='green', cursor="hand2")
        self.left_center.grid(row=3, column=0, rowspan=3, columnspan=2,
                              padx=10, pady=10, sticky="nsew")

        # Bottom / Organise and manage contacts
        def open_contacts():
            os.system('Contacts.py')
        Contacts_image = ImageTk.PhotoImage(Image.open(
            "Resources-img\contacts.png").resize((25, 25), Image.ANTIALIAS))
        self.left_lower = customtkinter.CTkButton(
            self.Timetable_frame, text="Organise and manage contacts", fg_color='#72BFF4', cursor="hand2", image=Contacts_image, command=open_contacts)
        self.left_lower.grid(row=6, column=0, rowspan=5, columnspan=2,
                             padx=10, pady=10, sticky="nsew")

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
        self.left_upper = customtkinter.CTkButton(
            self.dManager_frame, text="Task Manager", fg_color='dark red', cursor="hand2")
        self.left_upper.grid(row=0, column=0, rowspan=3, columnspan=3,
                             padx=10, pady=10, sticky="nsew")

        # Left center / Navigator
        self.left_center = customtkinter.CTkButton(
            self.dManager_frame, text="Navigator", fg_color='green', cursor="hand2")
        self.left_center.grid(row=3, column=0, rowspan=3, columnspan=2,
                              padx=10, pady=10, sticky="nsew")

        # Left lower / Device controler
        self.left_lower = customtkinter.CTkButton(
            self.dManager_frame, text="Device Controler", fg_color='blue', cursor="hand2")
        self.left_lower.grid(row=6, column=0, rowspan=5, columnspan=2,
                             padx=10, pady=10, sticky="nsew")

        # Right upper / Reminder
        self.right_upper = customtkinter.CTkButton(
            self.dManager_frame, text="Reminders & Alarms", fg_color='coral', cursor="hand2")
        self.right_upper.grid(row=0, column=3, rowspan=3, columnspan=2,
                              padx=10, pady=10, sticky="nsew")

        # Right lower / E-shop
        self.right_lower = customtkinter.CTkButton(
            self.dManager_frame, text="Your shop", fg_color='light green', cursor="hand2")
        self.right_lower.grid(row=3, column=2, rowspan=8, columnspan=3,
                              padx=10, pady=10, sticky="nsew")
        # -----------------------------------------------------------#


if __name__ == "__main__":
    app = App()
    app.mainloop()
