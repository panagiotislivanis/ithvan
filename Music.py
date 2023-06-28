import os
import pygame
import mutagen.mp3
from PIL import Image, ImageTk
from tkinter import PhotoImage
from typing import Union
import customtkinter

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

config = {"path": "./music"}

# Initialize pygame mixer
pygame.mixer.init()


class MusicPlayer(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        # self.geometry("400x660")

        self.__play_image = PhotoImage(file="Resources-img/play-button.png")
        self.__pause_image = PhotoImage(file="Resources-img/pause.png")
        self.__next_image = PhotoImage(file="Resources-img/next.png")
        self.__prev_image = PhotoImage(file="Resources-img/previous.png")

        self.__play_status: bool = False
        self.__pathMp3Dict: dict = self.find_audio_files(config["path"])
        self.__activate_now: int = 0
        self.__position = 0
        self.__total_length = 0
        self.__manual_positioning = False

        self.__progress_bar = customtkinter.CTkSlider(
            self, from_=0, to=1, command=self.change_position
        )
        self.__progress_bar.pack(fill="x", pady=10)

        self.__song_title_label = customtkinter.CTkLabel(
            self, text="", font=("Gotham Circular", 20)
        )
        self.__song_title_label.pack(side="top", anchor="nw", padx=10, pady=(0, 0))

        customtkinter.CTkButton(
            self, text="", command=self.prev, image=self.__prev_image
        ).pack(side="left")

        self.__play_button = customtkinter.CTkButton(
            self, text="", command=self.play, image=self.__play_image
        )
        self.__play_button.pack(padx=10, side="left")

        customtkinter.CTkButton(
            self, text="", command=self.next, image=self.__next_image
        ).pack(side="left")
        # Adding volume slider below the progress bar
        self.__volume_slider = customtkinter.CTkSlider(
            self,
            from_=0,
            to=1,
            orientation="vertical",
            height=55,
            command=self.change_volume,
            button_color="#aab0b5",
            progress_color="#aab0b5",
        )
        self.__volume_slider.pack(side="left", padx=10, pady=(0, 16))

        self.__song_image = None
        self.__song_image_label = customtkinter.CTkLabel(self, text="")
        self.__song_image_label.pack(side="left", pady=(0, 10))

        self.update_progress()
        self.update_image()
        self.update_song_title()
        self.check_music()

    @staticmethod
    def find_audio_files(directory: str) -> dict:
        # Search for .mp3 files in the given directory
        audio_files = {
            os.path.splitext(file)[0]: os.path.join(directory, file)
            for file in os.listdir(directory)
            if file.endswith(".mp3")
        }
        return audio_files

    def music_now(self, index) -> str:
        key = list(self.__pathMp3Dict.keys())[index]
        return self.__pathMp3Dict[key]

    def change_position(self, position: Union[int, str]) -> None:
        self.__manual_positioning = True
        self.__position = float(position)
        song = self.music_now(self.__activate_now)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(start=self.__position)

    def change_volume(self, volume: float):
        pygame.mixer.music.set_volume(volume)

    def update_progress(self) -> None:
        if self.__play_status and not self.__manual_positioning:
            # update progress bar
            new_time = pygame.mixer.music.get_pos() / 1000
            self.__progress_bar.set(new_time)
            # check if song has finished
            if abs(self.__total_length - new_time) <= 1:
                self.next()
        elif not self.__play_status:
            self.__manual_positioning = False
        self.after(1000, self.update_progress)

    def check_music(self):
        if (
            not pygame.mixer.music.get_busy() and self.__play_status
        ):  # Check if the music is playing and is not paused
            self.next()
        self.after(
            100, self.check_music
        )  # If music is playing then check again after 100ms

    def play(self, index: Union[int, str] = None) -> None:
        if self.__play_status:
            self.pause()
            return
        total_len_music = len(self.__pathMp3Dict)
        if index is None:
            index = self.__activate_now
        elif index == total_len_music:
            index = 0
        self.__play_status = True
        song = self.music_now(index)
        mp3 = mutagen.mp3.MP3(song)
        self.__total_length = mp3.info.length
        self.__progress_bar.configure(to=self.__total_length)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        self.__play_button.configure(image=self.__pause_image, command=self.pause)
        self.update_image()
        self.update_song_title()

    def pause(self) -> None:
        self.__play_status = False
        pygame.mixer.music.pause()
        self.__play_button.configure(image=self.__play_image, command=self.unpause)

    def unpause(self) -> None:
        self.__play_status = True
        pygame.mixer.music.unpause()
        self.__play_button.configure(image=self.__pause_image, command=self.pause)

    def next(self) -> None:
        self.__play_status = False
        pygame.mixer.music.stop()
        self.__activate_now += 1
        if self.__activate_now >= len(self.__pathMp3Dict):
            self.__activate_now = 0
        self.__position = 0  # Reset position when song changes.
        self.__progress_bar.set(0)  # Reset progress bar when song changes.
        self.play(self.__activate_now)
        self.update_image()
        self.update_song_title()

    def prev(self) -> None:
        self.__play_status = False
        pygame.mixer.music.stop()
        self.__activate_now -= 1
        if self.__activate_now < 0:
            self.__activate_now = len(self.__pathMp3Dict) - 1
        self.__position = 0  # Reset position when song changes.
        self.__progress_bar.set(0)  # Reset progress bar when song changes.
        self.play(self.__activate_now)
        self.update_image()
        self.update_song_title()

    def update_image(self) -> None:
        song_key = list(self.__pathMp3Dict.keys())[self.__activate_now]
        image_path = f"./music/{song_key}.png"

        if os.path.isfile(image_path):
            image = Image.open(image_path)
            image = image.resize((50, 50), Image.ANTIALIAS)
            self.__song_image = ImageTk.PhotoImage(image)
        else:
            # Creates a blank image as a placeholder.
            blank_image = Image.new("RGB", (30, 30), color="white")
            self.__song_image = ImageTk.PhotoImage(blank_image)
        self.__song_image_label.configure(image=self.__song_image)
        self.__song_image_label.image = self.__song_image

    def update_song_title(self) -> None:
        song_key = list(self.__pathMp3Dict.keys())[self.__activate_now]
        song_title = os.path.splitext(song_key)[0]
        self.__song_title_label.configure(text=song_title)


if __name__ == "__main__":
    root = customtkinter.CTk()
    root.geometry("528x119")
    music_player = MusicPlayer(root)
    music_player.pack()

    root.mainloop()
