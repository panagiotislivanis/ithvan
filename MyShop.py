from tkinter import *
from tkinter import messagebox
import customtkinter
from customtkinter import *
from PIL import Image


# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

class MyShop(customtkinter.CTk):    
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("MY Shop")
        self.geometry(f"{700}x{700}")
        self.resizable(False, False)        
        
        # Create search panel
        search_panel = customtkinter.CTkFrame(self, bg_color="grey30", width=470, height=50)
        search_panel.place(x=5, y=5)
        # Create main panel
        main_panel = customtkinter.CTkFrame(self, bg_color="grey30", width=470, height=630)
        main_panel.place(x=5, y=65)
        # Create profile panel
        profile_panel = customtkinter.CTkScrollableFrame(self, bg_color="grey30", width=200, height=690)
        profile_panel.place(x=490, y=5)
        
        #images
        search_icon = customtkinter.CTkImage(light_image=Image.open("Images\Search_Icon.png"), size=(35, 35))
        prof_pic = customtkinter.CTkImage(light_image=Image.open("Images\Default_Profile.png"), size=(140, 160))
        credit_card = customtkinter.CTkImage(light_image=Image.open("Images\Credit_Card.png"), size=(65, 65))
        iphone = customtkinter.CTkImage(light_image=Image.open("Images\iphone14pro.png"), size=(90, 90))
        iphone14 = customtkinter.CTkImage(light_image=Image.open("Images\iphone14pro.png"), size=(300, 350))
        graphics_card = customtkinter.CTkImage(light_image=Image.open("Images\GraphicsCard.png"), size=(90, 90))
        gc = customtkinter.CTkImage(light_image=Image.open("Images\GraphicsCard.png"), size=(300, 350))
        lawn_mower = customtkinter.CTkImage(light_image=Image.open("Images\LawnMower.jpg"), size=(90, 90))
        lm = customtkinter.CTkImage(light_image=Image.open("Images\LawnMower.jpg"), size=(300, 350))
        shopping_cart = customtkinter.CTkImage(light_image=Image.open("Images\ShoppingCart.png"), size=(60, 60))
        
        
        # Create search bar widget
        searchcbar = customtkinter.CTkEntry(search_panel, placeholder_text="Search...", width=410, height=45)
        searchcbar.place(x=5, y=5)
        search_button = customtkinter.CTkButton(search_panel, text="", image=search_icon, fg_color='light green', cursor="hand2", width=35, height=45, corner_radius=5)
        search_button.place(x=420, y=5)
        
        # Main menu widgets
        submit_button = customtkinter.CTkButton(main_panel, fg_color="light green", cursor="hand2")
        cancel_button = customtkinter.CTkButton(main_panel, fg_color="light green", cursor="hand2")
        
        # Profile widgets
        profile_picture = customtkinter.CTkButton(main_panel, text="", image=prof_pic, fg_color="grey30", cursor="hand2", height=170, width=150)
        nameLB = customtkinter.CTkLabel(main_panel, text="Name", font=('Comic Sans MS', 16, 'bold'), text_color="light green")
        name = customtkinter.CTkTextbox(main_panel, font=('Arial', 16), fg_color="grey30", height=30, width=400)
        emailLB = customtkinter.CTkLabel(main_panel, text="Email", font=('Comic Sans MS', 16, 'bold'), text_color="light green")
        email = customtkinter.CTkTextbox(main_panel, font=('Arial', 16), fg_color="grey30", height=30, width=400)
        countryLB = customtkinter.CTkLabel(main_panel, text="Country", font=('Comic Sans MS', 16, 'bold'), text_color="light green")
        country = customtkinter.CTkTextbox(main_panel, font=('Arial', 16), fg_color="grey30", height=30, width=400)
        adressLb = customtkinter.CTkLabel(main_panel, text="Adress", font=('Comic Sans MS', 16, 'bold'), text_color="light green")
        adress = customtkinter.CTkTextbox(main_panel, font=('Arial', 16), fg_color="grey30", height=30, width=400)
        postalcodeLb = customtkinter.CTkLabel(main_panel, text="Postal Code", font=('Comic Sans MS', 16, 'bold'), text_color="light green")
        postalcode = customtkinter.CTkTextbox(main_panel, font=('Arial', 16), fg_color="grey30", height=30, width=400)
        cardsLB = customtkinter.CTkLabel(main_panel, text="Cards", font=('Comic Sans MS', 16, 'bold'), text_color="light green")
        cards = customtkinter.CTkButton(main_panel, text="", image=credit_card, fg_color="light green", cursor="hand2", height=65, width=65)
        
        # Shop widgets
        
        
        def recomended_opener1():
            popup = CTkToplevel()
            popup.geometry("400x500+1100+200")
            popup.resizable(False, False)
            prod_label = customtkinter.CTkLabel(popup, text="", image=iphone14, height=350, width=200)
            product_info = customtkinter.CTkLabel(popup, text="Iphone 14 Pro", font=('Comic Sans MS', 20, 'bold'), text_color="light green")
            product_price = customtkinter.CTkLabel(popup, text="950€", font=('Comic Sans MS', 20, 'bold'), text_color="light green")
            add_to_cart = customtkinter.CTkButton(popup, text="", image=shopping_cart, fg_color="light green", height=70, width=150)
            prod_label.place(x=50, y=5)
            product_info.place(x=20, y=370)
            product_price.place(x=300, y=370)
            add_to_cart.place(x=130, y=420)
            
        def recomended_opener2():
            popup = CTkToplevel()
            popup.geometry("400x500+1100+200")
            popup.resizable(False, False)
            prod_label = customtkinter.CTkLabel(popup, text="", image=gc, height=350, width=200)
            product_info = customtkinter.CTkLabel(popup, text="NVIDIA Geforce GTX 3060 6GB", font=('Comic Sans MS', 20, 'bold'), text_color="light green")
            product_price = customtkinter.CTkLabel(popup, text="    360€", font=('Comic Sans MS', 20, 'bold'), text_color="light green")
            add_to_cart = customtkinter.CTkButton(popup, text="", image=shopping_cart, fg_color="light green", height=70, width=150)
            prod_label.place(x=50, y=5)
            product_info.place(x=20, y=370)
            product_price.place(x=300, y=370)
            add_to_cart.place(x=130, y=420)
            
        def recomended_opener3():
            popup = CTkToplevel()
            popup.geometry("400x500+1100+200")
            popup.resizable(False, False)
            prod_label = customtkinter.CTkLabel(popup, text="", image=lm, height=350, width=200)
            product_info = customtkinter.CTkLabel(popup, text="40V 21''Self-Propelled Lawn Mower", font=('Comic Sans MS', 20, 'bold'), text_color="light green")
            product_price = customtkinter.CTkLabel(popup, text="350€", font=('Comic Sans MS', 20, 'bold'), text_color="light green")
            add_to_cart = customtkinter.CTkButton(popup, text="", image=shopping_cart, fg_color="light green", height=70, width=150)
            prod_label.place(x=50, y=5)
            product_info.place(x=20, y=370)
            product_price.place(x=300, y=400)
            add_to_cart.place(x=130, y=420)

        recomended = customtkinter.CTkLabel(main_panel, text="Recomended", font=('Comic Sans MS', 16, 'bold'), text_color="light green")
        rec_prod1 = customtkinter.CTkButton(main_panel, text="", image=iphone, fg_color="grey30", cursor="hand2", height=100, width=100, command=recomended_opener1)
        rec_prod2 = customtkinter.CTkButton(main_panel, text="", image=graphics_card, fg_color="grey30", cursor="hand2", height=100, width=100, command=recomended_opener2)
        rec_prod3 = customtkinter.CTkButton(main_panel, text="", image=lawn_mower, fg_color="grey30", cursor="hand2", height=100, width=100, command=recomended_opener3)
        blackline = customtkinter.CTkLabel(main_panel, text="", font=('Arial', 2), fg_color="black", height=1, width=430)
        categories = customtkinter.CTkLabel(main_panel, text="Categories", font=('Comic Sans MS', 20, 'bold'), text_color="light green", height=30, width=180)
        cat1 = customtkinter.CTkButton(main_panel, text="Devices & Technology", font=('Comic Sans MS', 20, 'bold'), fg_color="DeepSkyBlue4", cursor="hand2", height=190, width=200)
        cat2 = customtkinter.CTkButton(main_panel, text="Fashion & Clothing", font=('Comic Sans MS', 20, 'bold'), fg_color="medium orchid", cursor="hand2", height=190, width=200)
        cat3 = customtkinter.CTkButton(main_panel, text="Home & Garden", font=('Comic Sans MS', 20, 'bold'), fg_color="SpringGreen4", cursor="hand2", height=190, width=220) 
        cat4 = customtkinter.CTkButton(main_panel, text="Sports & Hobbies", font=('Comic Sans MS', 20, 'bold'), fg_color="tomato", cursor="hand2", height=190, width=200) 
        
        
        # Help widgets
        assistance = customtkinter.CTkLabel(main_panel, text="Assistance Center", font=('Comic Sans MS', 30, 'bold'), text_color="grey30", bg_color="light green", height=60, width=450)
        reasonLB = customtkinter.CTkLabel(main_panel, text="What is the issue?", font=('Comic Sans MS', 24, 'bold'), text_color="light green", height=60, width=450)
        reason = customtkinter.CTkComboBox(main_panel, values=["About a product", "Problems with a delivery", "Product destroyed or damaged", "Payment issues and refunds"], font=('Comic Sans MS', 20, 'bold'), width=350)
        explanation = customtkinter.CTkTextbox(main_panel, font=('Arial', 20), fg_color="grey30", height=250, width=400)
        
        
        def open_prof():
            
            submit_button.place_forget()
            cancel_button.place_forget()
            assistance.place_forget()
            reasonLB.place_forget()
            reason.place_forget()
            explanation.place_forget()
            recomended.place_forget()
            rec_prod1.place_forget()
            rec_prod2.place_forget()          
            rec_prod3.place_forget()
            blackline.place_forget()
            categories.place_forget()
            cat1.place_forget()
            cat2.place_forget()
            cat3.place_forget()
            cat4.place_forget()
            
            
            profile_picture.place(x=140, y=10)
            nameLB.place(x=35, y=180)
            name.place(x=30, y=210)
            emailLB.place(x=35, y=250)
            email.place(x=30, y=280)
            countryLB.place(x=35, y=320)
            country.place(x=30, y=350)
            adressLb.place(x=35, y=390)
            adress.place(x=30, y=420)
            postalcodeLb.place(x=35, y=460)
            postalcode.place(x=30, y=490)
            cardsLB.place(x=35, y=530)
            cards.place(x=30, y=555)
            submit_button.configure(text="Save changes", font=('Comic Sans MS', 16, 'bold'), text_color="grey30", height=30, width=90)
            submit_button.place(x=350, y=580)
            cancel_button.configure (text="Discard changes", font=('Comic Sans MS', 16, 'bold'), text_color="grey30", height=30, width=90)
            cancel_button.place(x=210, y=580)
        
        def open_orders():
            submit_button.place_forget()
            cancel_button.place_forget()
            profile_picture.place_forget()
            nameLB.place_forget()
            name.place_forget()
            emailLB.place_forget()
            email.place_forget()
            countryLB.place_forget()
            country.place_forget()
            adressLb.place_forget()
            adress.place_forget()
            postalcodeLb.place_forget()
            postalcode.place_forget()
            cardsLB.place_forget()
            cards.place_forget()
            assistance.place_forget()
            reasonLB.place_forget()
            reason.place_forget()
            explanation.place_forget()
            recomended.place_forget()
            rec_prod1.place_forget()
            rec_prod2.place_forget()          
            rec_prod3.place_forget()
            blackline.place_forget()
            categories.place_forget()
            cat1.place_forget()
            cat2.place_forget()
            cat3.place_forget()
            cat4.place_forget()
            
        def open_shop():
            submit_button.place_forget()
            cancel_button.place_forget()
            profile_picture.place_forget()
            nameLB.place_forget()
            name.place_forget()
            emailLB.place_forget()
            email.place_forget()
            countryLB.place_forget()
            country.place_forget()
            adressLb.place_forget()
            adress.place_forget()
            postalcodeLb.place_forget()
            postalcode.place_forget()
            cardsLB.place_forget()
            cards.place_forget()
            assistance.place_forget()
            reasonLB.place_forget()
            reason.place_forget()
            explanation.place_forget() 
        
            recomended.place(x=20, y=5)
            rec_prod1.place(x=50, y=35)
            rec_prod2.place(x=190, y=35)
            rec_prod3.place(x=330, y=35)
            blackline.place(x=20, y=145)
            categories.place(x=145, y=150)
            cat1.place(x=20, y=200)
            cat2.place(x=260, y=200)
            cat3.place(x=20, y=420)
            cat4.place(x=260, y=420)
        
        def open_shop_help():
            
            submit_button.place_forget()
            cancel_button.place_forget()
            profile_picture.place_forget()
            nameLB.place_forget()
            name.place_forget()
            emailLB.place_forget()
            email.place_forget()
            countryLB.place_forget()
            country.place_forget()
            adressLb.place_forget()
            adress.place_forget()
            postalcodeLb.place_forget()
            postalcode.place_forget()
            cardsLB.place_forget()
            cards.place_forget()
            recomended.place_forget()
            rec_prod1.place_forget()
            rec_prod2.place_forget()          
            rec_prod3.place_forget()
            blackline.place_forget()
            categories.place_forget()
            cat1.place_forget()
            cat2.place_forget()
            cat3.place_forget()
            cat4.place_forget()
            
            assistance.place(x=10, y=20)
            reasonLB.place(x=10, y=100)
            reason.place(x=60, y=160)
            explanation.place(x=30, y=220)
            submit_button.configure(text="Submit help ticket", font=('Comic Sans MS', 20, 'bold'), text_color="grey30", height=40, width=100)
            submit_button.place(x=130, y=500)
        
        # Create profile widgets
        prof = customtkinter.CTkButton(profile_panel, text="Profile", font=('Comic Sans MS', 27, 'bold'), text_color="grey30", fg_color="light green", cursor="hand2", height=60, width=180, command=open_prof)
        prof.pack(padx=5, pady=5)
        orders = customtkinter.CTkButton(profile_panel, text="My Orders", font=('Comic Sans MS', 27, 'bold'), text_color="grey30", fg_color="light green", cursor="hand2", height=60, width=180, command=open_orders)
        orders.pack(padx=5, pady=20)
        shop_menu = customtkinter.CTkButton(profile_panel, text="Shop", font=('Comic Sans MS', 27, 'bold'), text_color="grey30", fg_color="light green", cursor="hand2", height=60, width=180, command=open_shop)
        shop_menu.pack(padx=5, pady=10)
        cart = customtkinter.CTkButton(profile_panel, text="My Cart", font=('Comic Sans MS', 27, 'bold'), text_color="grey30", fg_color="light green", cursor="hand2", height=60, width=180)
        cart.pack(padx=5, pady=20)
        shop_help = customtkinter.CTkButton(profile_panel, text="Help", font=('Comic Sans MS', 27, 'bold'), text_color="grey30", fg_color="light green", cursor="hand2", height=60, width=180, command=open_shop_help)
        shop_help.pack(padx=5, pady=260)
        
        
if __name__ == "__main__":
    app = MyShop()
    app.mainloop()