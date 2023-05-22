from tkinter import *
from tkinter import messagebox
import customtkinter
from customtkinter import *


# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

class TaskManager(customtkinter.CTk):    
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Task Manager")
        self.geometry(f"{700}x{700}")
        self.resizable(False, False)
        
        #add task        
        def add_task():
            task = task_entry.get()
            if task:
                task_list.insert(0, task)
                task_entry.delete(0, END)
                save_tasks()
            else:
                messagebox.showerror('Error', 'Enter a task.')
        
        #remove task
        def remove_task():
            selected = task_list.curselection()
            if selected:
                task_list.delete(selected[0])
                save_tasks()
            else:
                messagebox.showerror('Error', 'Choose a task to delete.')
        
        #save tasks.txt state
        def save_tasks():
            with open("tasks.txt", "w") as file:
                tasks = task_list.get(0, END)
                for task in tasks:
                    file.write(task + "\n")
        
        #load tasks.txt
        def load_tasks():
            try:
                with open("tasks.txt", "r") as file:
                    tasks = file.readlines()
                    for task in tasks:
                        task_list.insert(0, task.strip())
            except FileNotFoundError:
                pass
        
        #window assets
        title = customtkinter.CTkLabel(self, text='My To-Do List', font=('Comic Sans MS', 40, 'bold'), bg_color='tomato4', corner_radius=5, height=60, width=260)
        title.place(x=225, y=15)
        add_button = customtkinter.CTkButton(self, text='Add task', font=('Comic Sans MS', 24, 'bold'), fg_color='green4', cursor='hand2', command=add_task, corner_radius=5, width=260)
        add_button.place(x=50, y=100)
        remove_button = customtkinter.CTkButton(self, text='Remove task', font=('Comic Sans MS', 24, 'bold'), fg_color='red4', cursor='hand2', command=remove_task, corner_radius=5, width=260)
        remove_button.place(x=385, y=100)
        task_entry = customtkinter.CTkEntry(self, font=('Arial', 20), border_color='grey50', width=600)
        task_entry.place(x=50, y=150)
        task_list = Listbox(self, font=('Arial',18), background='grey30', width=46, height=16)
        task_list.place(x=50, y=210)
        
        load_tasks()


if __name__ == "__main__":
    app = TaskManager()
    app.mainloop()