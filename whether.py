from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os
import time

def create_whether():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("file://" + os.path.abspath("whether.html"))
    #print("hello1")
    time.sleep(1.5)
    driver.set_window_size(1920, 1080)
    # time.sleep(1)
    driver.save_screenshot("images/whether.png")
    # time.sleep(5)
    driver.quit()
    image = Image.open("images/whether.png")
    image = image.crop((10, 10, image.width - 1500, image.height - 953))
    # Αποθήκευση της εικόνας σε μορφή PNG    
    image.save("images/whether.png", "PNG")



