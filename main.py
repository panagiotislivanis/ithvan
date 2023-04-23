import tkinter
import tkinter.messagebox
import customtkinter

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("ITHVAN")
        self.geometry(f"{800}x{580}")

        # Crate a layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create tabview
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(row=0, column=0, sticky="nsew")
        self.tabview.add("Homepage")
        self.tabview.add("Tab 2")
        # self.tabview.add("Tab 3")
        # Create custom grid for homepage tab
        self.homepage_frame = self.tabview.tab("Homepage")

        self.homepage_frame.columnconfigure(0, weight=1)
        self.homepage_frame.columnconfigure(1, weight=1)
        self.homepage_frame.columnconfigure(2, weight=1)
        self.homepage_frame.rowconfigure(0, weight=1)
        self.homepage_frame.rowconfigure(1, weight=2)
        # Widgets for homepage tab
        self.left_upper = customtkinter.CTkLabel(
            self.homepage_frame, text="Left Upper Widget", fg_color='pink')
        self.left_upper.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.left_lower = customtkinter.CTkLabel(
            self.homepage_frame, text="Left Lower Widget", fg_color='red')
        self.left_lower.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.right_upper_left = customtkinter.CTkLabel(
            self.homepage_frame, text="Right Upper Left Widget", fg_color='orange')
        self.right_upper_left.grid(
            row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.right_upper_right = customtkinter.CTkLabel(
            self.homepage_frame, text="Right Upper Right Widget", fg_color='blue')
        self.right_upper_right.grid(
            row=0, column=2, padx=10, pady=10, sticky="nsew")

        self.right_lower = customtkinter.CTkLabel(
            self.homepage_frame, text="Right Lower Widget", fg_color='green')
        self.right_lower.grid(row=1, column=1, columnspan=2,
                              padx=10, pady=10, sticky="nsew")

        # Tab2
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)
        self.label_tab_2 = customtkinter.CTkLabel(
            self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
