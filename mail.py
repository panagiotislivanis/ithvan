import customtkinter as ctk
import yagmail
import smtplib
import ssl
from email.message import EmailMessage
import CTkMessagebox

# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
SERVICE_ACCOUNT_FILE = "key.json"


class EmailApp(ctk.CTkFrame):
    def show_checkmark(self):
        # Show some positive message with the checkmark icon
        CTkMessagebox(message="success", icon="check", option_1="Thanks")

    def show_error(self, error_message):
        # Show some error message
        CTkMessagebox(title="Error", message="Error", icon="cancel")

    def __init__(self, parent):
        super().__init__(parent, bg_color="white")
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.label_to = ctk.CTkLabel(self, text="To:")
        self.label_to.pack()

        self.entry_to = ctk.CTkEntry(self, width=450)
        self.entry_to.pack()

        self.label_subject = ctk.CTkLabel(self, text="Subject:")
        self.label_subject.pack()

        self.entry_subject = ctk.CTkEntry(self, width=450)
        self.entry_subject.pack()

        self.label_message = ctk.CTkLabel(self, text="Message:")
        self.label_message.pack()

        self.entry_message = ctk.CTkEntry(self, width=450, height=450)
        self.entry_message.pack()

        self.button_send = ctk.CTkButton(self, text="Send", command=self.send_email)
        self.button_send.pack()

    def send_email(self):
        receiver = self.entry_to.get()
        subject = self.entry_subject.get()
        message = self.entry_message.get()
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "ithvanithvan@gmail.com"
        password = "htrrapepazexbzlx"

        msg = EmailMessage()
        msg.set_content(message)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver
        context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.send_message(msg, from_addr=sender_email, to_addrs=receiver)
                self.show_checkmark()
        except Exception as e:
            self.show_error(str(e))


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Email App")
    app.geometry("400x400")
    email_app = EmailApp(app)
    email_app.pack(fill="both", expand=True)
    app.mainloop()
