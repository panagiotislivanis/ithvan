import tkinter as tk
from PIL import Image
import customtkinter
import os

# Modes: "System" (standard), "Dark", "Light"


class SearchBar(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Load images with light and dark mode
        image_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "Resources-img")
        # Search icon Dark/Light versions
        self.searchimage = customtkinter.CTkImage(
            dark_image=Image.open(os.path.join(image_path, "search-dark.png")), light_image=Image.open(os.path.join(image_path, "search-light.png")))
        # Create search bar widget
        entry = customtkinter.CTkEntry(self, placeholder_text="Search...")
        entry.pack()
        # Search button
        search_button = customtkinter.CTkButton(
            self, text="", image=self.searchimage, width=entry.cget("width")/3, corner_radius=5, fg_color="transparent")
        search_button.place(in_=entry, relx=1.0, rely=0.0,
                            anchor=customtkinter.N)


if __name__ == "__main__":
    app = SearchBar()
    app.mainloop()
