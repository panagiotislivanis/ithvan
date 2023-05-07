import requests
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from io import BytesIO
from bs4 import BeautifulSoup
import webbrowser

# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")


class NewsWidget(ctk.CTkFrame):
    def __init__(self, parent, api_key, bg_color="transparent"):
        super().__init__(parent, bg_color=bg_color)
        self.api_key = api_key
        self.articles = self.fetch_news()
        self.current_article_index = 0

        self.create_widgets()

    def create_widgets(self):
        # Add Next and Previous buttons
        self.button_frame = ctk.CTkFrame(self, fg_color='#4c4c4c')
        self.button_frame.pack(side="bottom", pady=0, fill="both")
        prev_button = ctk.CTkButton(self.button_frame, text="Previous",
                                    command=self.previous_article, width=80)
        prev_button.pack(side="left", padx=(0, 0), anchor="s")
        next_button = ctk.CTkButton(self.button_frame, text="Next",
                                    command=self.next_article, width=80)
        next_button.pack(side="right", padx=(0, 0), anchor="s")

        # Add hyperlink to original article
        link_label = ctk.CTkLabel(
            self.button_frame, text="Read More...", cursor="hand2", font=("Arial bold", 14), text_color="#6da1ca",)
        link_label.bind(
            "<Button-1>", lambda e: webbrowser.open_new(self.articles[self.current_article_index]["url"]))
        link_label.pack(side="bottom", pady=0, anchor="s")

        # Display current article
        self.display_article()

    def display_article(self):
        article = self.articles[self.current_article_index]

        # Display article image
        image_url = article["urlToImage"]
        image_data = requests.get(image_url).content
        image = Image.open(BytesIO(image_data))
        image = image.resize((500, 400), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(self, text='', image=photo)
        image_label.image = photo  # Keep a reference to the image to prevent garbage collection
        image_label.pack(side="top", pady=(0, 0))

        # Display article text.
        text_bg = "#3c3c3c"
        # Text color.
        text_cl = '#6da1ca'  # 6da1ca
        # Text background.
        text_fg = "#333333"  # 2b2b2b
        text_font = ("Arial", 18)
        title = article["title"]
        # Getting only the first line of code to display, and if the window is fullscreen print the first paragraph.
        content_lines = article["content"].split('\n')
        first_line = '\n'.join(content_lines[:2])
        text = title + "\n\n" + first_line

        text_label = ctk.CTkLabel(
            self, text=text, text_color=text_cl, font=text_font, bg_color=text_bg, fg_color=text_fg, justify="center", wraplength=400)
        text_label.pack(side="top", padx=0, pady=(20, 0))

    def fetch_news(self):
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        articles = data["articles"]
        return articles[:5]  # Display only the top 5 articles

    def next_article(self):
        self.current_article_index = (
            self.current_article_index + 1) % len(self.articles)
        self.clear_widgets()
        self.display_article()

    def previous_article(self):
        self.current_article_index = (
            self.current_article_index - 1) % len(self.articles)
        self.clear_widgets()
        self.display_article()

    def clear_widgets(self):
        for widget in self.winfo_children():
            if widget != self.button_frame:
                widget.destroy()


# API key.
API_KEY = "46f1942a35684436a2eaa05b27fd06d8"

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("News Widget Example")
    app.geometry("400x660")
    news_widget = NewsWidget(app, API_KEY)
    news_widget.pack(fill="both", expand=True)
    app.mainloop()


# API_KEY = "46f1942a35684436a2eaa05b27fd06d8"
