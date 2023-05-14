import requests
import tkinter as tk
import customtkinter as ctk
import webbrowser


# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")


class MusicWidget(ctk.CTkFrame):
    def __init__(self, parent, bg_color="transparent"):
        super().__init__(parent, bg_color=bg_color)


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Music Widget Example")
    app.geometry("400x660")
    music_widget = MusicWidget(app)
    music_widget.pack(fill="both", expand=True)
    app.mainloop()
