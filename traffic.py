from PIL import Image
import customtkinter as ctk
from traffic_map import make_map


# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")


class TrafficWidget(ctk.CTkFrame):
    #make_map()

    def __init__(self, parent, bg_color="transparent"):
        super().__init__(parent, bg_color=bg_color)
        self.create_widget()

    def create_widget(self):
        image = Image.open("images/final_2.png")
        cropped_image = image.crop(
            (0, 0, 800, 800)
        )  # Adjust the cropping coordinates as needed

        photo = ctk.CTkImage(
            cropped_image, size=(800, 800)
        )  # Adjust the size as needed
        image_label = ctk.CTkLabel(self, text="", image=photo, padx=0, pady=0)
        image_label.image = photo
        image_label.pack(side="bottom", padx=10, pady=10)


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("test")
    app.geometry("400x660")
    widget = TrafficWidget(app)
    widget.pack(fill="both", expand=True)
    app.mainloop()
