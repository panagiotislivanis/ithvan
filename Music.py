import os
import pygame
import mutagen.mp3
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


class MusicPlayer(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Music player")
        self.geometry("568x119")

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
            height=100,
            command=self.change_volume,
            button_color="#00ffff",
            progress_color="#00ffbf",
        )
        self.__volume_slider.pack(side="left", pady=(00, 16))

        self.update_progress()

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
        elif not self.__play_status:
            self.__manual_positioning = False

        self.after(1000, self.update_progress)

    def play(self, index: Union[int, str] = "active") -> None:
        self.__play_status = True
        total_len_music = len(self.__pathMp3Dict)
        if index == total_len_music:
            index = 0
        song = self.music_now(index)
        mp3 = mutagen.mp3.MP3(song)
        self.__total_length = mp3.info.length
        self.__progress_bar.configure(to=self.__total_length)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        self.__play_button.configure(image=self.__pause_image, command=self.pause)

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
        self.play(self.__activate_now)

    def prev(self) -> None:
        self.__play_status = False
        pygame.mixer.music.stop()
        self.__activate_now -= 1
        self.play(self.__activate_now)


root = MusicPlayer()
root.mainloop()
