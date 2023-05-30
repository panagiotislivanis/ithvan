from tkinter import *
from tkinter import messagebox
import customtkinter
from customtkinter import *
from PIL import Image


# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

class MyShop(customtkinter.CTk):    
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("MY Shop")
        self.geometry(f"{700}x{700}")
        self.resizable(False, False)        
        
        # Create search panel
        search_panel = customtkinter.CTkFrame(self, bg_color="grey30", width=470, height=50)
        search_panel.place(x=5, y=5)
        
        # Create main panel
        main_panel = customtkinter.CTkFrame(self, bg_color="grey30", width=470, height=630)
        main_panel.place(x=5, y=65)
        
        # Create profile panel
        profile_panel = customtkinter.CTkScrollableFrame(self, bg_color="grey30", width=200, height=690)
        profile_panel.place(x=490, y=5)
        
        #images
        search_icon = customtkinter.CTkImage(light_image=Image.open("Images\Search_Icon.png"), size=(35, 35))
        
        
        
        # Create search bar widget
        searchcbar = customtkinter.CTkEntry(search_panel, placeholder_text="Search...", width=410, height=45)
        searchcbar.place(x=5, y=5)
        search_button = customtkinter.CTkButton(search_panel, text="", image=search_icon, fg_color='light green', cursor="hand2", width=35, height=45, corner_radius=5)
        search_button.place(x=420, y=5)
        
        
        
        
        
"""         
if __name__ == "__main__":
    app = MyShop()
    app.mainloop()         """
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    app = MyShop()
    app.mainloop()