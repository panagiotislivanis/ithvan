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
import time


def create_weather():

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("file://" + os.path.abspath("weather.html"))
    time.sleep(1)
    driver.set_window_size(1920, 1080)
    # time.sleep(5)
    driver.save_screenshot("images/weather.png")
    # time.sleep(5)
    driver.quit()

    image = Image.open("images/weather.png")
    image = image.crop((10, 10, image.width - 1500, image.height - 953))
    # image = image.resize(1920, 1080)

    # Αποθήκευση της εικόνας σε μορφή JPEG
    print("Saving image as PNG...")
    image.save("images/weather.png", "PNG")
    print("Image saved as weather.PNG")
