import customtkinter
import tkinter as tk
import sqlite3
from customtkinter import *
from tkinter import *
from tkcalendar import Calendar

def Database():
    conn = sqlite3.connect("calendar.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS events (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, event TEXT, date TEXT, startTime TEXT, endTime TEXT)")
    conn.commit()
    cursor.close()
    conn.close()

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

def display_events():
    selected_date = cal.get_date()

    conn = sqlite3.connect("calendar.db")
    cursor = conn.cursor()
    cursor.execute("SELECT event, startTime, endTime FROM events WHERE date=?", (selected_date,))
    results = cursor.fetchall()
    event_text = "\n".join([f"{event}: {start_time} - {end_time}" for event, start_time, end_time in results])
    cursor.close()
    conn.close()

    event_label.config(text=event_text)


root = tk.Tk()
root.title('Calendar')
root.geometry("400x500")
p1 = PhotoImage(file = 'Resources-img\calendar.png')
root.iconphoto(False, p1)
root.config(bg="#242424")


cal = Calendar(root, selectmode="day", year=2023, month=5, day=26)
cal.pack(ipadx=20)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

entry_start = tk.Entry(root, width=10)
entry_start.pack(pady=10)

entry_end = tk.Entry(root, width=10)
entry_end.pack(pady=10)

add_button = tk.Button(root, text="Add Event", command=add_event)
add_button.pack(pady=20)

event_label = tk.Label(root, text="")
event_label.pack(pady=20)

Database() 

root.mainloop()
