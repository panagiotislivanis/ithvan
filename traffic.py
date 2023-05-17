import requests
import folium
import webbrowser
# from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os
import threading
import customtkinter as ctk
from whether import create_whether
# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")


class traffic_widget(ctk.CTkFrame):

    def __init__(self, parent, bg_color="transparent"):
        super().__init__(parent, bg_color=bg_color)
        self.create_widget()

    def create_widget(self):
        photo = ctk.CTkImage(Image.open(
            "images/final.png"), size=(2000, 1400))
        image_label = ctk.CTkLabel(
            self, text='', image=photo, padx=0, pady=0)
        image_label.image = photo
        image_label.pack(side="top", pady=(0, 0))


def get_traffic_data():
    response = requests.get(
        "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json",
        params={
            "point": "37.989829,23.765133",
            "unit": "MPH",
            "key": "eRuAxCtEML4iTUX0urNXWgHOd0hM5CbO"
        }
    )

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception("Failed to get traffic data")


def create_traffic_map():
    m = folium.Map(location=[37.975633, 23.734591],
                   zoom_start=12, tiles="OpenStreetMap")

    data = get_traffic_data()
    m.save("images/traffic_map.html")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("file://" + os.path.abspath("images/traffic_map.html"))
    driver.set_window_size(1920, 1080)

    driver.save_screenshot("images/traffic_map_screenshot.png")
    driver.quit()

    image = Image.open("images/traffic_map_screenshot.png")
    image = image.crop((560, 200, image.width - 550, image.height - 200))
    # image = image.resize(1920, 1080)
    # Αποθήκευση της εικόνας σε μορφή JPEG
    print("Saving image as PNG...")
    image.save("images/traffic_map.png", "PNG")
    print("Image saved as traffic_map.PNG")
    create_whether()
    whether = Image.open("images/whether.png")
    back_im = image.copy()
    image.paste(whether, (400, 0))
    image.save('images/final.png', quality=95)
    path = os.path.abspath("images/traffic_map.png")
    return path


def create_traffic_map_repeat():
    create_traffic_map()
    # Επανάληψη της δημιουργίας του χάρτη κάθε 5 λεπτά (300 δευτερόλεπτα)
    threading.Timer(30, create_traffic_map_repeat).start()


create_traffic_map()
if __name__ == "__main__":
    app = ctk.CTk()
    app.title("test")
    app.geometry("400x660")
    widget = traffic_widget(app)
    widget.pack(fill="both", expand=True)
    app.mainloop()

# create_traffic_map_repeat()
