import requests
import tkinter as tk
import customtkinter as ctk
import webbrowser
import pygame
from ytmusicapi import YTMusic
# import vlc


# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")


class MusicWidget(ctk.CTkFrame):
    def __init__(self, parent, bg_color="transparent"):
        super().__init__(parent, bg_color=bg_color)

        # Create a VLC instance
        self.vlc_instance = vlc.Instance()
        # Create an empty VLC media player
        self.player = self.vlc_instance.media_player_new()

    # Add Play, Pause, and Stop buttons
        self.play_button = ctk.CTkButton(
            self, text="Play", command=self.play_music)
        self.play_button.pack(side="left", padx=10)

        self.play_button = ctk.CTkButton(
            self, text="Pause", command=self.pause_music)
        self.play_button.pack(side="left", padx=10)

        self.play_button = ctk.CTkButton(
            self, text="Stop", command=self.stop_music)
        self.play_button.pack(side="left", padx=10)

    def play_music(self):
        # Replace with your actual music file path
        pygame.mixer.music.load("\The Animals - House of the Rising Sun.mp3")
        pygame.mixer.music.play()

    def pause_music(self):
        # Define VLC media
        # replace with your actual MP3 file path
        media = self.vlc_instance.media_new(
            '\The Animals - House of the Rising Sun.mp3')
        # Set media to the player
        self.player.set_media(media)
        # Play the media
        self.player.play()

    def stop_music(self):
        print("Stop music")

    def change_volume(self, value):
        print(f"Change volume to {value}")


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Music Widget Example")
    app.geometry("500x120")
    music_widget = MusicWidget(app)
    music_widget.pack(fill="both", expand=True)
    app.mainloop()
