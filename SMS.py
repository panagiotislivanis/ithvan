from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import customtkinter
from customtkinter import *
from PIL import ImageTk, Image

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

class SMS(customtkinter.CTk):    
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("SMS")
        self.geometry(f"{400}x{600}")

        # Load image
        image = Image.open("Resources-img/SMS.png")
        image = image.resize((400, 600), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        # Create label with the image
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Adjust label size to fit window
        label.bind("<Configure>", lambda event: self.resize_image(event, label, image))

    def resize_image(self, event, label, image):
        new_width = event.width
        new_height = event.height
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
        new_photo = ImageTk.PhotoImage(resized_image)
        label.configure(image=new_photo)
        label.image = new_photo

if __name__ == "__main__":
    app = SMS()
    app.mainloop()
