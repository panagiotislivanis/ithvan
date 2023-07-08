from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import os
import time


def create_whether():
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )

    driver.get("file://" + os.path.abspath("whether.html"))
    time.sleep(1.5)
    driver.set_window_size(1920, 1080)
    driver.save_screenshot("images/whether.png")
    driver.quit()
    image = Image.open("images/whether.png")
    image = image.crop((10, 10, image.width - 1500, image.height - 953))
    image.save("images/whether.png", "PNG")
