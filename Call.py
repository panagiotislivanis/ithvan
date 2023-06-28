from tkinter import *
import customtkinter
from customtkinter import *

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

class Call(customtkinter.CTk):    
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Calls")
        self.geometry(f"{300}x{600}")
        
        # Create a layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        
        # Create the entry field
        self.entry = Entry(self, font=("Arial", 20))
        self.entry.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky="we")
        
        # Create keypad buttons
        buttons = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            "*", "0", "#"
        ]
        
        row = 1
        col = 0
        
        for button_text in buttons:
            button = Button(self, text=button_text, font=("Arial", 15), width=5, height=2, command=lambda text=button_text: self.on_keypress(text))
            button.grid(row=row, column=col, padx=2, pady=2)
            col += 1
            
            if col > 2:
                col = 0
                row += 1
        
        # Create the call button
        call_button = Button(self, text="Call", font=("Arial", 15), width=5, height=2, command=self.on_call)
        call_button.config(bg="green", fg="white")  # Set the background color to green and foreground (text) color to white
        call_button.grid(row=row+1, column=0, padx=2, pady=2)  # Adjusted row and column values
        
        # Create the delete button
        delete_button = Button(self, text="Delete", font=("Arial", 15), width=5, height=2, command=self.on_delete)
        delete_button.grid(row=row+1, column=2, padx=2, pady=2)  # Adjusted row and column values
   
    def on_keypress(self, key):
        current_number = self.entry.get()
        new_number = current_number + key
        self.entry.delete(0, "end")
        self.entry.insert("end", new_number)
        
    def on_delete(self):
        current_number = self.entry.get()
        new_number = current_number[:-1]  # Remove the last character
        self.entry.delete(0, "end")
        self.entry.insert("end", new_number)
        
    def on_call(self):
        number = self.entry.get()
        # Perform the call action with the entered number
        print(f"Calling {number}...")

if __name__ == "__main__":
    app = Call()
    app.mainloop()
