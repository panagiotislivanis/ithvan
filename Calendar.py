import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from customtkinter import *
from tkinter import *
from tkcalendar import Calendar
from datetime import datetime


class CalendarApp:
    def __init__(self, master):
        self.master = master
        # Replace 'root' with 'self.master' in the original code
        self.cal = Calendar(self.master, selectmode="day", year=2023, month=7, day=14)
        self.cal.grid(row=0, column=0, padx=20, pady=10, columnspan=2)

        # Event name field
        self.entry = tk.Entry(self.master, width=30)
        self.entry.insert(0, "Event name")
        self.entry.bind("<FocusIn>", self.clear_entry)
        self.entry.grid(row=1, column=0, padx=20, pady=10, columnspan=2)

        # Event time start field
        self.entry_start = Spinbox(
            self.master,
            width=10,
            values=[str(i).zfill(2) for i in range(24)],
            wrap=True,
        )
        self.entry_start.delete(0, tk.END)
        start_time_values = [
            datetime.strftime(datetime.strptime(str(i), "%H"), "%H:%M")
            for i in range(24)
        ]
        self.entry_start = ttk.Combobox(
            self.master, values=start_time_values, state="readonly", width=10
        )
        self.entry_start.current(0)  # Set the default value to the first item
        self.entry_start.bind("<FocusIn>", self.clear_entry)
        self.entry_start.grid(row=2, column=0, padx=5, pady=10)

        # Create a Spinbox widget for selecting the end time
        self.entry_end = Spinbox(
            self.master,
            width=10,
            values=[str(i).zfill(2) for i in range(24)],
            wrap=True,
        )
        self.entry_end.delete(0, tk.END)
        end_time_values = [
            datetime.strftime(datetime.strptime(str(i), "%H"), "%H:%M")
            for i in range(24)
        ]
        self.entry_end = ttk.Combobox(
            self.master, values=end_time_values, state="readonly", width=10
        )
        self.entry_end.current(0)  # Set the default value to the first item
        self.entry_end.bind("<FocusIn>", self.clear_entry)
        self.entry_end.grid(row=2, column=1, padx=5, pady=10)

        self.add_button = tk.Button(
            self.master, text="Add Event", command=self.add_event
        )
        self.add_button.grid(row=3, column=0, padx=2, pady=20)

        self.delete_button = tk.Button(
            self.master, text="Delete Event", bg="red", command=self.DeleteData
        )
        self.delete_button.grid(row=3, column=1, padx=2, pady=20)

        self.display_button = tk.Button(
            self.master, text="View your events", command=self.display_events
        )
        self.display_button.grid(row=4, column=0, padx=20, pady=10, columnspan=2)

        self.event_listbox = tk.Listbox(self.master, width=30)
        self.event_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

        self.Database()  # Corrected this line

    def clear_entry(self, event):
        if self.entry.get() == "Event name":
            self.entry.delete(0, tk.END)
        elif self.entry_start.get() == "Event start":
            self.entry_start.delete(0, tk.END)
        elif self.entry_end.get() == "Event end":
            self.entry_end.delete(0, tk.END)

    def Database(self):
        conn = sqlite3.connect("calendar.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS events (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, event TEXT, date TEXT, startTime TEXT, endTime TEXT)"
        )
        conn.commit()
        cursor.close()
        conn.close()

    # Function for creating an event
    def add_event(self):
        selected_date = self.cal.get_date()
        event = self.entry.get()

        start_time = self.entry_start.get()
        end_time = self.entry_end.get()

        if event and selected_date and start_time and end_time:
            conn = sqlite3.connect("calendar.db")
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO events (event, date, startTime, endTime) VALUES (?, ?, ?, ?)",
                (event, selected_date, start_time, end_time),
            )
            conn.commit()
            cursor.close()
            conn.close()

            self.entry.delete(0, tk.END)
            self.entry_start.delete(0, tk.END)
            self.entry_end.delete(0, tk.END)

            self.display_events()

    # Function for deleting an event
    def DeleteData(self):
        event = self.entry.get()
        selected_date = self.cal.get_date()
        start_time = self.entry_start.get()
        end_time = self.entry_end.get()
        selected = selection()
        if event and selected_date and start_time and end_time:
            conn = sqlite3.connect("calendar.db")
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM events WHERE event=? AND date=? AND startTime=? AND endTime=?",
                (selected_date, event, start_time, end_time),
            )
            conn.commit()
            cursor.close()
            conn.close()

    def display_events(self):
        selected_date = self.cal.get_date()

        conn = sqlite3.connect("calendar.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT event, date, startTime, endTime FROM events WHERE date=? ORDER BY date ASC",
            (selected_date,),
        )
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        self.event_listbox.delete(0, tk.END)  # Clear the listbox

        if results:
            for event in results:
                self.event_listbox.insert(
                    tk.END, f"{event[0]}: {event[1]} - {event[2]}"
                )
