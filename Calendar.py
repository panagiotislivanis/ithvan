import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from customtkinter import *
from tkinter import *
from tkcalendar import Calendar
from datetime import datetime

def Database():
    conn = sqlite3.connect("calendar.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS events (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, event TEXT, date TEXT, startTime TEXT, endTime TEXT)")
    conn.commit()
    cursor.close()
    conn.close()

#Function for creating an event
def add_event():
    selected_date = cal.get_date()
    event = entry.get()
    
    start_time = entry_start.get()
    end_time = entry_end.get()

    if event and selected_date and start_time and end_time:
        conn = sqlite3.connect("calendar.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO events (event, date, startTime, endTime) VALUES (?, ?, ?, ?)", (event, selected_date, start_time, end_time))
        conn.commit()
        cursor.close()
        conn.close()

        entry.delete(0, tk.END)
        entry_start.delete(0, tk.END)
        entry_end.delete(0, tk.END)

        display_events()

#Function for deleting an event
def DeleteData():
    event = entry.get()
    selected_date = cal.get_date()
    start_time = entry_start.get()
    end_time = entry_end.get()
    selected = selection()
    if event and selected_date and start_time and end_time:
        conn = sqlite3.connect("calendar.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM events WHERE event=? AND date=? AND startTime=? AND endTime=?", (selected_date, event, start_time, end_time))
        conn.commit()
        cursor.close()
        conn.close()

        

def display_events():
    selected_date = cal.get_date()

    conn = sqlite3.connect("calendar.db")
    cursor = conn.cursor()
    cursor.execute("SELECT event, date, startTime, endTime FROM events WHERE date=? ORDER BY date ASC", (selected_date,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    event_listbox.delete(0, tk.END)  # Clear the listbox

    if results:
        for event in results:
            event_listbox.insert(tk.END, f"{event[0]}: {event[1]} - {event[2]}")



#Function for clearing the entry when user tries to enter something in the textbox
def clear_entry(event):
    if entry.get() == "Event name":
        entry.delete(0, tk.END)
    elif entry_start.get() == "Event start":
        entry_start.delete(0, tk.END)
    elif entry_end.get() == "Event end":
        entry_end.delete(0, tk.END)
    

#Window configuration
root = tk.Tk()
root.title('Calendar')
root.geometry("300x600")
p1 = PhotoImage(file = 'Resources-img\calendar.png')
root.iconphoto(False, p1)
root.config(bg="#242424")


cal = Calendar(root, selectmode="day", year=2023, month=7, day=14)
cal.grid(row=0, column=0, padx=20, pady=10, columnspan=2)

#Event name field
entry = tk.Entry(root, width=30)
entry.insert(0,"Event name")
entry.bind("<FocusIn>", clear_entry) #Clearing the entry when user tries to enter event name
entry.grid(row=1, column=0, padx=20, pady=10, columnspan=2)

#Event time start field
entry_start = Spinbox(root, width=10, values=[str(i).zfill(2) for i in range(24)], wrap=True)
entry_start.delete(0, tk.END)
start_time_values = [datetime.strftime(datetime.strptime(str(i), "%H"), "%H:%M") for i in range(24)]
entry_start = ttk.Combobox(root, values=start_time_values, state="readonly", width=10)
entry_start.current(0)  # Set the default value to the first item
entry_start.bind("<FocusIn>", clear_entry)
entry_start.grid(row=2, column=0, padx=5, pady=10)

# Create a Spinbox widget for selecting the end time
entry_end = Spinbox(root, width=10, values=[str(i).zfill(2) for i in range(24)], wrap=True)
entry_end.delete(0, tk.END)
end_time_values = [datetime.strftime(datetime.strptime(str(i), "%H"), "%H:%M") for i in range(24)]
entry_end = ttk.Combobox(root, values=end_time_values, state="readonly", width=10)
entry_end.current(0)  # Set the default value to the first item
entry_end.bind("<FocusIn>", clear_entry)
entry_end.grid(row=2, column=1, padx=5, pady=10)

add_button = tk.Button(root, text="Add Event", command=add_event)
add_button.grid(row=3, column=0, padx=2, pady=20)

delete_button = tk.Button(root, text="Delete Event", bg="red", command=DeleteData)
delete_button.grid(row=3, column=1, padx=2, pady=20)

display_button = tk.Button(root, text="View your events", command=display_events)
display_button.grid(row=4, column=0, padx=20, pady=10, columnspan=2)

event_listbox = tk.Listbox(root, width=30)
event_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

Database() 

root.mainloop()

