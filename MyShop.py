import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter
import customtkinter
from customtkinter import *
from PIL import Image

sum = 0
# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class MyShop(customtkinter.CTk):
    def __init__(self, master=None):
        super().__init__(master)

        # Configure window
        if master is None:  # Only set title, geometry and resizable if running as a standalone window
            self.title("MY Shop")
            self.geometry(f"{700}x{700}")
            self.resizable(False, False)

        # And the rest of your code...

        # Create search panel
        search_panel = customtkinter.CTkFrame(
            self, bg_color="grey30", width=470, height=50
        )
        search_panel.place(x=5, y=5)
        # Create main panel
        main_panel = customtkinter.CTkFrame(
            self, bg_color="grey30", width=470, height=630
        )
        main_panel.place(x=5, y=65)
        # Create profile panel
        profile_panel = customtkinter.CTkScrollableFrame(
            self, bg_color="grey30", width=200, height=690
        )
        profile_panel.place(x=490, y=5)

        # images
        search_icon = customtkinter.CTkImage(
            light_image=Image.open("Images\Search_Icon.png"), size=(35, 35)
        )
        prof_pic = customtkinter.CTkImage(
            light_image=Image.open("Images\Default_Profile.png"), size=(140, 160)
        )
        credit_card = customtkinter.CTkImage(
            light_image=Image.open("Images\Credit_Card.png"), size=(65, 65)
        )
        iphone = customtkinter.CTkImage(
            light_image=Image.open("Images\iphone14pro.png"), size=(90, 90)
        )
        iphone14 = customtkinter.CTkImage(
            light_image=Image.open("Images\iphone14pro.png"), size=(300, 350)
        )
        graphics_card = customtkinter.CTkImage(
            light_image=Image.open("Images\GraphicsCard.png"), size=(90, 90)
        )
        gc = customtkinter.CTkImage(
            light_image=Image.open("Images\GraphicsCard.png"), size=(300, 350)
        )
        lawn_mower = customtkinter.CTkImage(
            light_image=Image.open("Images\LawnMower.jpg"), size=(90, 90)
        )
        lm = customtkinter.CTkImage(
            light_image=Image.open("Images\LawnMower.jpg"), size=(300, 350)
        )
        shopping_cart = customtkinter.CTkImage(
            light_image=Image.open("Images\ShoppingCart.png"), size=(60, 60)
        )
        hp_laptop = customtkinter.CTkImage(
            light_image=Image.open("Images\HPLaptop.jpg"), size=(190, 260)
        )
        lg_tv = customtkinter.CTkImage(
            light_image=Image.open("Images\LGTV.jpg"), size=(190, 260)
        )
        rtx4080 = customtkinter.CTkImage(
            light_image=Image.open("Images\RTX4080.png"), size=(190, 260)
        )
        xiaomi = customtkinter.CTkImage(
            light_image=Image.open("Images\Xiaomi_Redmi_Note10.jpg"), size=(190, 260)
        )
        dress = customtkinter.CTkImage(
            light_image=Image.open("Images\Dress.jpg"), size=(190, 260)
        )
        jeans = customtkinter.CTkImage(
            light_image=Image.open("Images\Jeans.jpg"), size=(190, 260)
        )
        tshirt = customtkinter.CTkImage(
            light_image=Image.open("Images\polo.jpg"), size=(190, 260)
        )
        shoes = customtkinter.CTkImage(
            light_image=Image.open("Images\Shoes.png"), size=(190, 260)
        )
        chair = customtkinter.CTkImage(
            light_image=Image.open("Images\Chair.jpg"), size=(190, 260)
        )
        pots_pack = customtkinter.CTkImage(
            light_image=Image.open("Images\Planting pots.jpg"), size=(190, 260)
        )
        plates = customtkinter.CTkImage(
            light_image=Image.open("Images\plates.jpg"), size=(190, 260)
        )
        toolcase = customtkinter.CTkImage(
            light_image=Image.open("Images\Toolcase.jpg"), size=(190, 260)
        )
        canvas = customtkinter.CTkImage(
            light_image=Image.open("Images\Canvas.jpg"), size=(190, 260)
        )
        climbing_gear = customtkinter.CTkImage(
            light_image=Image.open("Images\Climbing_Gear.jpg"), size=(190, 260)
        )
        guitar = customtkinter.CTkImage(
            light_image=Image.open("Images\elec_guitar.jpg"), size=(190, 260)
        )
        ucl_ball = customtkinter.CTkImage(
            light_image=Image.open("Images\Ball.jpg"), size=(190, 260)
        )

        def createDB():
            conn = sqlite3.connect("myShop_prof.db")
            crs = conn.cursor()
            crs.execute(
                "CREATE TABLE IF NOT EXISTS myShop_prof(id integer primary key, name TEXT, email TEXT, country TEXT, adress TEXT, postalcode INT)"
            )
            crs.execute(
                "CREATE TABLE IF NOT EXISTS myShop_cards(id INT AUTO_INCREMENT primary key, number TEXT, owner TEXT, CVV INT, exp_date TEXT)"
            )
            crs.execute(
                "CREATE TABLE IF NOT EXISTS myShop_orders(id INT AUTO_INCREMENT primary key, status TEXT)"
            )
            conn.commit()
            conn.close()

        createDB()
        # Create search bar widget
        searchcbar = customtkinter.CTkEntry(
            search_panel, placeholder_text="Search...", width=410, height=45
        )
        searchcbar.place(x=5, y=5)
        search_button = customtkinter.CTkButton(
            search_panel,
            text="",
            image=search_icon,
            fg_color="light blue",
            cursor="hand2",
            width=35,
            height=45,
            corner_radius=5,
        )
        search_button.place(x=420, y=5)

        # Main menu widgets
        submit_button = customtkinter.CTkButton(
            main_panel, fg_color="light blue", cursor="hand2"
        )
        cancel_button = customtkinter.CTkButton(
            main_panel, fg_color="light blue", cursor="hand2"
        )
        product1 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=hp_laptop,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product2 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=lg_tv,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product3 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=rtx4080,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product4 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=xiaomi,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product5 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=dress,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product6 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=jeans,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product7 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=tshirt,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product8 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=shoes,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product9 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=chair,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product10 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=pots_pack,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product11 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=plates,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product12 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=toolcase,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product13 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=canvas,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product14 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=climbing_gear,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product15 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=guitar,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )
        product16 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=ucl_ball,
            fg_color="grey30",
            cursor="hand2",
            height=270,
            width=200,
        )

        # Profile widgets
        def card_manager():
            def show_cards():
                card_numberLB.place_forget()
                card_number.place_forget()
                ownerLB.place_forget()
                owner.place_forget()
                cvvLB.place_forget()
                cvv.place_forget()
                expdateLB.place_forget()
                expdate.place_forget()
                save_card.place_forget()
                my_cards.place_forget()

                conn = sqlite3.connect("myShop_prof.db")
                crs = conn.cursor()
                crs.execute("SELECT number, owner, CVV, exp_date FROM myShop_cards;")
                cards_info = crs.fetchall()
                cards_list = Listbox(
                    popup, font=("Arial", 18), background="grey20", width=34, height=12
                )
                for each_card in cards_info:
                    cards_list.insert(0, each_card)
                cards_list.place(x=4, y=10)
                conn.commit()
                crs.close()

                def back_to_cards():
                    cards_list.place_forget()
                    back_button.place_forget()

                    def add_card_to_back():
                        conn = sqlite3.connect("myShop_prof.db")
                        crs = conn.cursor()
                        entry_number = card_number.get()
                        entry_owner = owner.get()
                        entry_cvv = cvv.get()
                        entry_expdate = expdate.get()
                        crs.execute(
                            "INSERT INTO myShop_cards (number, owner, CVV, exp_date) VALUES (?, ?, ?, ?);",
                            (entry_number, entry_owner, entry_cvv, entry_expdate),
                        )
                        conn.commit()
                        crs.close()

                    card_numberLB = customtkinter.CTkLabel(
                        popup,
                        text="Card Number",
                        font=("arial", 16, "bold"),
                        text_color="light blue",
                    )
                    card_number = customtkinter.CTkTextbox(
                        popup,
                        font=("Arial", 16),
                        fg_color="grey30",
                        height=30,
                        width=430,
                    )
                    ownerLB = customtkinter.CTkLabel(
                        popup,
                        text="Owner",
                        font=("arial", 16, "bold"),
                        text_color="light blue",
                    )
                    owner = customtkinter.CTkTextbox(
                        popup,
                        font=("Arial", 16),
                        fg_color="grey30",
                        height=30,
                        width=430,
                    )
                    cvvLB = customtkinter.CTkLabel(
                        popup,
                        text="CVV",
                        font=("arial", 16, "bold"),
                        text_color="light blue",
                    )
                    cvv = customtkinter.CTkTextbox(
                        popup,
                        font=("Arial", 16),
                        fg_color="grey30",
                        height=30,
                        width=120,
                    )
                    expdateLB = customtkinter.CTkLabel(
                        popup,
                        text="Exparation Date",
                        font=("arial", 16, "bold"),
                        text_color="light blue",
                    )
                    expdate = customtkinter.CTkTextbox(
                        popup,
                        font=("Arial", 16),
                        fg_color="grey30",
                        height=30,
                        width=180,
                    )
                    save_card = customtkinter.CTkButton(
                        popup,
                        text="Save Card",
                        font=("Arial", 18, "bold"),
                        text_color="grey30",
                        fg_color="light blue",
                        cursor="hand2",
                        height=30,
                        width=40,
                        command=add_card_to_back,
                    )
                    my_cards = customtkinter.CTkButton(
                        popup,
                        text="My Cards",
                        font=("Arial", 40, "bold"),
                        text_color="grey30",
                        fg_color="light blue",
                        cursor="hand2",
                        height=80,
                        width=300,
                        command=show_cards,
                    )

                    card_numberLB.place(x=5, y=5)
                    card_number.place(x=5, y=40)
                    ownerLB.place(x=5, y=80)
                    owner.place(x=5, y=115)
                    cvvLB.place(x=5, y=155)
                    cvv.place(x=5, y=190)
                    expdateLB.place(x=150, y=155)
                    expdate.place(x=150, y=190)
                    save_card.place(x=340, y=191)
                    my_cards.place(x=75, y=270)

                back_button = customtkinter.CTkButton(
                    popup,
                    text="Back",
                    font=("Arial", 18, "bold"),
                    text_color="grey30",
                    fg_color="light blue",
                    cursor="hand2",
                    height=30,
                    width=40,
                    command=back_to_cards,
                )
                back_button.place(x=205, y=360)

            def add_card():
                conn = sqlite3.connect("myShop_prof.db")
                crs = conn.cursor()
                entry_number = card_number.get()
                entry_owner = owner.get()
                entry_cvv = cvv.get()
                entry_expdate = expdate.get()
                crs.execute(
                    "INSERT INTO myShop_cards (number, owner, CVV, exp_date) VALUES (?, ?, ?, ?);",
                    (entry_number, entry_owner, entry_cvv, entry_expdate),
                )
                conn.commit()
                crs.close()

            popup = CTkToplevel()
            popup.title("Card Manager")
            popup.geometry("450x400+1000+250")
            popup.resizable(False, False)
            card_numberLB = customtkinter.CTkLabel(
                popup,
                text="Card Number",
                font=("arial", 16, "bold"),
                text_color="light blue",
            )
            card_number = customtkinter.CTkEntry(
                popup, font=("Arial", 16), fg_color="grey30", height=30, width=430
            )
            ownerLB = customtkinter.CTkLabel(
                popup,
                text="Owner",
                font=("arial", 16, "bold"),
                text_color="light blue",
            )
            owner = customtkinter.CTkEntry(
                popup, font=("Arial", 16), fg_color="grey30", height=30, width=430
            )
            cvvLB = customtkinter.CTkLabel(
                popup, text="CVV", font=("arial", 16, "bold"), text_color="light blue"
            )
            cvv = customtkinter.CTkEntry(
                popup, font=("Arial", 16), fg_color="grey30", height=30, width=120
            )
            expdateLB = customtkinter.CTkLabel(
                popup,
                text="Exparation Date",
                font=("arial", 16, "bold"),
                text_color="light blue",
            )
            expdate = customtkinter.CTkEntry(
                popup, font=("Arial", 16), fg_color="grey30", height=30, width=180
            )
            save_card = customtkinter.CTkButton(
                popup,
                text="Save Card",
                font=("Arial", 18, "bold"),
                text_color="grey30",
                fg_color="light blue",
                cursor="hand2",
                height=30,
                width=40,
                command=add_card,
            )
            my_cards = customtkinter.CTkButton(
                popup,
                text="My Cards",
                font=("Arial", 40, "bold"),
                text_color="grey30",
                fg_color="light blue",
                cursor="hand2",
                height=80,
                width=300,
                command=show_cards,
            )

            card_numberLB.place(x=5, y=5)
            card_number.place(x=5, y=40)
            ownerLB.place(x=5, y=80)
            owner.place(x=5, y=115)
            cvvLB.place(x=5, y=155)
            cvv.place(x=5, y=190)
            expdateLB.place(x=150, y=155)
            expdate.place(x=150, y=190)
            save_card.place(x=340, y=191)
            my_cards.place(x=75, y=270)

        profile_picture = customtkinter.CTkButton(
            main_panel,
            text="",
            image=prof_pic,
            fg_color="grey30",
            cursor="hand2",
            height=170,
            width=150,
        )
        nameLB = customtkinter.CTkLabel(
            main_panel,
            text="Name",
            font=("arial", 16, "bold"),
            text_color="light blue",
        )
        name = customtkinter.CTkEntry(
            main_panel, font=("Arial", 16), fg_color="grey30", height=30, width=400
        )
        emailLB = customtkinter.CTkLabel(
            main_panel,
            text="Email",
            font=("arial", 16, "bold"),
            text_color="light blue",
        )
        email = customtkinter.CTkEntry(
            main_panel, font=("Arial", 16), fg_color="grey30", height=30, width=400
        )
        countryLB = customtkinter.CTkLabel(
            main_panel,
            text="Country",
            font=("arial", 16, "bold"),
            text_color="light blue",
        )
        country = customtkinter.CTkEntry(
            main_panel, font=("Arial", 16), fg_color="grey30", height=30, width=400
        )
        adressLb = customtkinter.CTkLabel(
            main_panel,
            text="Adress",
            font=("arial", 16, "bold"),
            text_color="light blue",
        )
        adress = customtkinter.CTkEntry(
            main_panel, font=("Arial", 16), fg_color="grey30", height=30, width=400
        )
        postalcodeLb = customtkinter.CTkLabel(
            main_panel,
            text="Postal Code",
            font=("arial", 16, "bold"),
            text_color="light blue",
        )
        postalcode = customtkinter.CTkEntry(
            main_panel, font=("Arial", 16), fg_color="grey30", height=30, width=400
        )
        cardsLB = customtkinter.CTkLabel(
            main_panel,
            text="Cards",
            font=("arial", 16, "bold"),
            text_color="light blue",
        )
        cards = customtkinter.CTkButton(
            main_panel,
            text="",
            image=credit_card,
            fg_color="light blue",
            cursor="hand2",
            height=65,
            width=65,
            command=card_manager,
        )

        def discard_changes():
            open_prof()

        # Shop widgets
        def add_prod_to_cart(prod_name, prod_price):
            global sum
            product_to_cart = prod_name
            sum = sum + prod_price
            if product_to_cart:
                cart_list.insert(0, product_to_cart)
            else:
                messagebox.showerror("Error", "Enter a task.")

        def recomended_opener1():
            popup = CTkToplevel()
            popup.title("My Shop")
            popup.geometry("400x500+1100+200")
            popup.resizable(False, False)
            prod_label = customtkinter.CTkLabel(
                popup, text="", image=iphone14, height=350, width=200
            )
            product_info = customtkinter.CTkLabel(
                popup,
                text="Iphone 14 Pro",
                font=("arial", 20, "bold"),
                text_color="light blue",
            )
            product_price = customtkinter.CTkLabel(
                popup, text="950€", font=("arial", 20, "bold"), text_color="light blue"
            )
            add_to_cart = customtkinter.CTkButton(
                popup,
                text="",
                image=shopping_cart,
                fg_color="light blue",
                cursor="hand2",
                height=70,
                width=150,
                command=lambda: add_prod_to_cart("Iphone 14 Pro", 950),
            )
            prod_label.place(x=50, y=5)
            product_info.place(x=20, y=370)
            product_price.place(x=300, y=370)
            add_to_cart.place(x=130, y=420)

        def recomended_opener2():
            popup = CTkToplevel()
            popup.title("My Shop")
            popup.geometry("400x500+1100+200")
            popup.resizable(False, False)
            prod_label = customtkinter.CTkLabel(
                popup, text="", image=gc, height=350, width=200
            )
            product_info = customtkinter.CTkLabel(
                popup,
                text="NVIDIA Geforce GTX 3060 6GB",
                font=("arial", 20, "bold"),
                text_color="light blue",
            )
            product_price = customtkinter.CTkLabel(
                popup,
                text="    360€",
                font=("arial", 20, "bold"),
                text_color="light blue",
            )
            add_to_cart = customtkinter.CTkButton(
                popup,
                text="",
                image=shopping_cart,
                fg_color="light blue",
                cursor="hand2",
                height=70,
                width=150,
                command=lambda: add_prod_to_cart("NVIDIA Geforce GTX 3060 6GB", 360),
            )
            prod_label.place(x=50, y=5)
            product_info.place(x=20, y=370)
            product_price.place(x=300, y=370)
            add_to_cart.place(x=130, y=420)

        def recomended_opener3():
            popup = CTkToplevel()
            popup.title("My Shop")
            popup.geometry("400x500+1100+200")
            popup.resizable(False, False)
            prod_label = customtkinter.CTkLabel(
                popup, text="", image=lm, height=350, width=200
            )
            product_info = customtkinter.CTkLabel(
                popup,
                text="40V 21''Self-Propelled Lawn Mower",
                font=("arial", 20, "bold"),
                text_color="light blue",
            )
            product_price = customtkinter.CTkLabel(
                popup, text="350€", font=("arial", 20, "bold"), text_color="light blue"
            )
            add_to_cart = customtkinter.CTkButton(
                popup,
                text="",
                image=shopping_cart,
                fg_color="light blue",
                cursor="hand2",
                height=70,
                width=150,
                command=lambda: add_prod_to_cart(
                    "40V 21''Self-Propelled Lawn Mower", 350
                ),
            )
            prod_label.place(x=50, y=5)
            product_info.place(x=20, y=370)
            product_price.place(x=300, y=400)
            add_to_cart.place(x=130, y=420)

        def technology():
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

            hp = customtkinter.CTkImage(
                light_image=Image.open("Images\HPLaptop.jpg"), size=(300, 350)
            )
            lg = customtkinter.CTkImage(
                light_image=Image.open("Images\LGTV.jpg"), size=(300, 350)
            )
            rtx = customtkinter.CTkImage(
                light_image=Image.open("Images\RTX4080.png"), size=(300, 350)
            )
            redmi = customtkinter.CTkImage(
                light_image=Image.open("Images\Xiaomi_Redmi_Note10.jpg"),
                size=(300, 350),
            )

            def laptop_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=hp, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="HP 15s-eq2037nv R3-5300U",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="450€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("HP 15s-eq2037nv R3-5300U", 450),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=400)
                add_to_cart.place(x=130, y=420)

            def tv_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=lg, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="Τηλεόραση LG LED 32'' Full HD Smart",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="290€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart(
                        "Τηλεόραση LG LED 32'' Full HD Smart", 290
                    ),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=400)
                add_to_cart.place(x=130, y=420)

            def rtx_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=rtx, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="MSI GeForce RTX 4080 16GB GDDR6X",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="1600€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart(
                        "MSI GeForce RTX 4080 16GB GDDR6X", 1600
                    ),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=400)
                add_to_cart.place(x=130, y=420)

            def phone_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=redmi, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="Xiaomi Redmi Note 10",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="150€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("Xiaomi Redmi Note 10", 150),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=370)
                add_to_cart.place(x=130, y=420)

            product1.place(x=20, y=20)
            product1.configure(command=laptop_info)
            product2.place(x=260, y=20)
            product2.configure(command=tv_info)
            product3.place(x=20, y=320)
            product3.configure(command=rtx_info)
            product4.place(x=260, y=320)
            product4.configure(command=phone_info)

        def fashion():
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

            w_dress = customtkinter.CTkImage(
                light_image=Image.open("Images\Dress.jpg"), size=(300, 350)
            )
            m_jeans = customtkinter.CTkImage(
                light_image=Image.open("Images\Jeans.jpg"), size=(300, 350)
            )
            polo_tshirt = customtkinter.CTkImage(
                light_image=Image.open("Images\polo.jpg"), size=(300, 350)
            )
            huh_shoes = customtkinter.CTkImage(
                light_image=Image.open("Images\Shoes.png"), size=(300, 350)
            )

            def dress_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=w_dress, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="Black Dress",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="55€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("Black Dress", 55),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=370)
                add_to_cart.place(x=130, y=420)

            def jeans_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=m_jeans, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="Slim Jeans",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="20€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("Slim Jeans", 20),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=370)
                add_to_cart.place(x=130, y=420)

            def shirt_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=polo_tshirt, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="Purple Polo T-Shirt",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="60€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("Purple Polo T-Shirt", 60),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=370)
                add_to_cart.place(x=130, y=420)

            def shoes_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=huh_shoes, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="WHAT ARE THOOOSE?",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="300€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("WHAT ARE THOOOSE?", 300),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=370)
                add_to_cart.place(x=130, y=420)

            product5.place(x=20, y=20)
            product5.configure(command=dress_info)
            product6.place(x=260, y=20)
            product6.configure(command=jeans_info)
            product7.place(x=20, y=320)
            product7.configure(command=shirt_info)
            product8.place(x=260, y=320)
            product8.configure(command=shoes_info)

        def home_garden():
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

            chair_i = customtkinter.CTkImage(
                light_image=Image.open("Images\Chair.jpg"), size=(300, 350)
            )
            pots_pack_i = customtkinter.CTkImage(
                light_image=Image.open("Images\Planting pots.jpg"), size=(300, 350)
            )
            plates_i = customtkinter.CTkImage(
                light_image=Image.open("Images\plates.jpg"), size=(300, 350)
            )
            toolcase_i = customtkinter.CTkImage(
                light_image=Image.open("Images\Toolcase.jpg"), size=(300, 350)
            )

            def chair_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=chair_i, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="Desk Chair",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="65€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("Desk Chair", 65),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=370)
                add_to_cart.place(x=130, y=420)

            def pots_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=pots_pack_i, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="Planting Pots Pack",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="30€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("Planting Pots Pack", 30),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=370)
                add_to_cart.place(x=130, y=420)

            def plates_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=plates_i, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="Set of Plates",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="15€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("Set of Plates", 15),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=370)
                add_to_cart.place(x=130, y=420)

            def tools_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=toolcase_i, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="Toolcase",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="45€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("Toolcase", 45),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=370)
                add_to_cart.place(x=130, y=420)

            product9.place(x=20, y=20)
            product9.configure(command=chair_info)
            product10.place(x=260, y=20)
            product10.configure(command=pots_info)
            product11.place(x=20, y=320)
            product11.configure(command=plates_info)
            product12.place(x=260, y=320)
            product12.configure(command=tools_info)

        def hobbies():
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

            canvas_i = customtkinter.CTkImage(
                light_image=Image.open("Images\Canvas.jpg"), size=(300, 350)
            )
            climbing_gear_i = customtkinter.CTkImage(
                light_image=Image.open("Images\Climbing_Gear.jpg"), size=(300, 350)
            )
            guitar_i = customtkinter.CTkImage(
                light_image=Image.open("Images\elec_guitar.jpg"), size=(300, 350)
            )
            ucl_ball_i = customtkinter.CTkImage(
                light_image=Image.open("Images\Ball.jpg"), size=(300, 350)
            )

            def canvas_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=canvas_i, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="Canvas",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="15€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("Canvas", 15),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=370)
                add_to_cart.place(x=130, y=420)

            def climbing_gear_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=climbing_gear_i, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="Climbing Gear",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="70€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("Climbing Gear", 70),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=370)
                add_to_cart.place(x=130, y=420)

            def guitar_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=guitar_i, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="Electronic Guitar",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="550€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("Electronic Guitar", 550),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=370)
                add_to_cart.place(x=130, y=420)

            def uclBall_info():
                popup = CTkToplevel()
                popup.title("My Shop")
                popup.geometry("400x500+1100+200")
                popup.resizable(False, False)
                prod_label = customtkinter.CTkLabel(
                    popup, text="", image=ucl_ball_i, height=350, width=200
                )
                product_info = customtkinter.CTkLabel(
                    popup,
                    text="UCL 2023 Ball",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                product_price = customtkinter.CTkLabel(
                    popup,
                    text="35€",
                    font=("arial", 20, "bold"),
                    text_color="light blue",
                )
                add_to_cart = customtkinter.CTkButton(
                    popup,
                    text="",
                    image=shopping_cart,
                    fg_color="light blue",
                    cursor="hand2",
                    height=70,
                    width=150,
                    command=lambda: add_prod_to_cart("UCL 2023 Ball", 35),
                )
                prod_label.place(x=50, y=5)
                product_info.place(x=20, y=370)
                product_price.place(x=300, y=370)
                add_to_cart.place(x=130, y=420)

            product13.place(x=20, y=20)
            product13.configure(command=canvas_info)
            product14.place(x=260, y=20)
            product14.configure(command=climbing_gear_info)
            product15.place(x=20, y=320)
            product15.configure(command=guitar_info)
            product16.place(x=260, y=320)
            product16.configure(command=uclBall_info)

        recomended = customtkinter.CTkLabel(
            main_panel,
            text="Recomended",
            font=("arial", 16, "bold"),
            text_color="light blue",
        )
        rec_prod1 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=iphone,
            fg_color="grey30",
            cursor="hand2",
            height=100,
            width=100,
            command=recomended_opener1,
        )
        rec_prod2 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=graphics_card,
            fg_color="grey30",
            cursor="hand2",
            height=100,
            width=100,
            command=recomended_opener2,
        )
        rec_prod3 = customtkinter.CTkButton(
            main_panel,
            text="",
            image=lawn_mower,
            fg_color="grey30",
            cursor="hand2",
            height=100,
            width=100,
            command=recomended_opener3,
        )
        blackline = customtkinter.CTkLabel(
            main_panel, text="", font=("Arial", 2), fg_color="black"
        )
        categories = customtkinter.CTkLabel(
            main_panel,
            text="Categories",
            font=("arial", 20, "bold"),
            text_color="light blue",
            height=30,
            width=180,
        )
        cat1 = customtkinter.CTkButton(
            main_panel,
            text="Devices & Technology",
            font=("arial", 20, "bold"),
            fg_color="DeepSkyBlue4",
            cursor="hand2",
            height=190,
            width=200,
            command=technology,
        )
        cat2 = customtkinter.CTkButton(
            main_panel,
            text="Fashion & Clothing",
            font=("arial", 20, "bold"),
            fg_color="medium orchid",
            cursor="hand2",
            height=190,
            width=200,
            command=fashion,
        )
        cat3 = customtkinter.CTkButton(
            main_panel,
            text="Home & Garden",
            font=("arial", 20, "bold"),
            fg_color="SpringGreen4",
            cursor="hand2",
            height=190,
            width=220,
            command=home_garden,
        )
        cat4 = customtkinter.CTkButton(
            main_panel,
            text="Sports & Hobbies",
            font=("arial", 20, "bold"),
            fg_color="tomato",
            cursor="hand2",
            height=190,
            width=200,
            command=hobbies,
        )

        # Orders widgets
        def complete_order():
            conn = sqlite3.connect("myShop_prof.db")
            crs = conn.cursor()
            crs.executescript('INSERT INTO myShop_orders (status) VALUES ("Pending");')
            conn.commit()
            crs.close()
            open_orders()

        order_label = customtkinter.CTkLabel(
            main_panel,
            text="Order",
            font=("arial", 20, "bold"),
            text_color="light blue",
        )
        orstatus_label = customtkinter.CTkLabel(
            main_panel,
            text="Status",
            font=("arial", 20, "bold"),
            text_color="light blue",
        )
        orders_catalog = Listbox(
            main_panel, font=("Arial", 18), background="grey20", width=24, height=20
        )
        status_catalog = Listbox(
            main_panel, font=("Arial", 18), background="grey20", width=8, height=20
        )

        # Cart widgets
        cart_list = Listbox(
            main_panel,
            font=("Arial", 18),
            background="DarkSeaGreen1",
            width=34,
            height=20,
        )
        conn = sqlite3.connect("myShop_prof.db")
        crs = conn.cursor()
        crs.execute("SELECT number, owner, CVV, exp_date FROM myShop_cards;")
        cards_info = crs.fetchall()
        card_picker = Listbox(
            main_panel, font=("Arial", 18), background="grey20", width=34, height=5
        )
        for each_card in cards_info:
            card_picker.insert(0, each_card)

        conn.commit()
        crs.close()
        total_text = "Your total is:" + str(sum)
        cost_label = customtkinter.CTkLabel(
            main_panel,
            text=total_text,
            font=("arial", 30, "bold"),
            text_color="grey30",
            bg_color="light blue",
            height=60,
            width=420,
        )

        def load_cart():
            try:
                with open("cart.txt", "r") as file:
                    tasks = file.readlines()
                    for task in tasks:
                        cart_list.insert(0, task.strip())
            except FileNotFoundError:
                pass

        # Help widgets
        def succesfull_submition():
            messagebox.showinfo(
                title="Thank you!😊",
                message="Your ticket has been submited successfully.\nThank you for contacting with us we will do our best to solve the issue(s)!",
            )

        assistance = customtkinter.CTkLabel(
            main_panel,
            text="Assistance Center",
            font=("arial", 30, "bold"),
            text_color="grey30",
            bg_color="light blue",
            height=60,
            width=450,
        )
        reasonLB = customtkinter.CTkLabel(
            main_panel,
            text="What is the issue?",
            font=("arial", 24, "bold"),
            text_color="light blue",
            height=60,
            width=450,
        )
        reason = customtkinter.CTkComboBox(
            main_panel,
            values=[
                "About a product",
                "Problems with a delivery",
                "Product destroyed or damaged",
                "Payment issues and refunds",
            ],
            font=("arial", 20, "bold"),
            width=350,
        )
        explanation = customtkinter.CTkTextbox(
            main_panel, font=("Arial", 20), fg_color="grey30", height=250, width=400
        )

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
            product1.place_forget()
            product2.place_forget()
            product3.place_forget()
            product4.place_forget()
            product5.place_forget()
            product6.place_forget()
            product7.place_forget()
            product8.place_forget()
            product9.place_forget()
            product10.place_forget()
            product11.place_forget()
            product12.place_forget()
            product13.place_forget()
            product14.place_forget()
            product15.place_forget()
            product16.place_forget()
            order_label.place_forget()
            orstatus_label.place_forget()
            orders_catalog.place_forget()
            status_catalog.place_forget()
            cart_list.place_forget()
            card_picker.place_forget()
            cost_label.place_forget()

            def save_changes():
                conn = sqlite3.connect("myShop_prof.db")
                crs = conn.cursor()
                entry_name = name.get()
                entry_email = email.get()
                entry_country = country.get()
                entry_adress = adress.get()
                entry_postalcode = postalcode.get()
                crs.execute(
                    "UPDATE myShop_prof SET name=(?), email=(?), country=(?), adress=(?), postalcode=(?) WHERE id=1;",
                    (
                        entry_name,
                        entry_email,
                        entry_country,
                        entry_adress,
                        entry_postalcode,
                    ),
                )
                conn.commit()
                crs.close()

            conn = sqlite3.connect("myShop_prof.db")
            crs = conn.cursor()
            crs.execute("SELECT name FROM myShop_prof WHERE id=1;")
            entry_var = crs.fetchone()
            profile_picture.place(x=140, y=10)
            nameLB.place(x=35, y=180)
            name.configure(placeholder_text=entry_var)
            name.place(x=30, y=210)
            emailLB.place(x=35, y=250)
            crs.execute("SELECT email FROM myShop_prof WHERE id=1;")
            entry_var = crs.fetchone()
            email.configure(placeholder_text=entry_var)
            email.place(x=30, y=280)
            countryLB.place(x=35, y=320)
            crs.execute("SELECT country FROM myShop_prof WHERE id=1;")
            entry_var = crs.fetchone()
            country.configure(placeholder_text=entry_var)
            country.place(x=30, y=350)
            adressLb.place(x=35, y=390)
            crs.execute("SELECT adress FROM myShop_prof WHERE id=1;")
            entry_var = crs.fetchone()
            adress.configure(placeholder_text=entry_var)
            adress.place(x=30, y=420)
            postalcodeLb.place(x=35, y=460)
            crs.execute("SELECT postalcode FROM myShop_prof WHERE id=1;")
            entry_var = crs.fetchone()
            postalcode.configure(placeholder_text=entry_var)
            postalcode.place(x=30, y=490)
            cardsLB.place(x=35, y=530)
            cards.place(x=30, y=555)
            submit_button.configure(
                text="Save changes",
                font=("arial", 16, "bold"),
                text_color="grey30",
                height=30,
                width=90,
                command=save_changes,
            )
            submit_button.place(x=350, y=580)
            cancel_button.configure(
                text="Discard changes",
                font=("arial", 16, "bold"),
                text_color="grey30",
                height=30,
                width=90,
                command=discard_changes,
            )
            cancel_button.place(x=210, y=580)
            conn.commit()
            crs.close()

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
            product1.place_forget()
            product2.place_forget()
            product3.place_forget()
            product4.place_forget()
            product5.place_forget()
            product6.place_forget()
            product7.place_forget()
            product8.place_forget()
            product9.place_forget()
            product10.place_forget()
            product11.place_forget()
            product12.place_forget()
            product13.place_forget()
            product14.place_forget()
            product15.place_forget()
            product16.place_forget()
            cart_list.place_forget()
            card_picker.place_forget()
            cost_label.place_forget()

            conn = sqlite3.connect("myShop_prof.db")
            crs = conn.cursor()
            crs.execute("SELECT id FROM myShop_orders;")
            order_info = crs.fetchall()
            for each_order in order_info:
                orders_catalog.insert(0, each_order)

            crs.execute("SELECT status FROM myShop_orders;")
            status_info = crs.fetchall()
            for each_status in status_info:
                status_catalog.insert(0, each_status)

            order_label.place(x=10, y=10)
            orstatus_label.place(x=350, y=10)
            blackline.configure(height=600, width=2)
            blackline.place(x=340, y=10)
            orders_catalog.place(x=10, y=50)
            status_catalog.place(x=350, y=50)
            conn.commit()
            crs.close()

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
            blackline.place_forget()
            product1.place_forget()
            product2.place_forget()
            product3.place_forget()
            product4.place_forget()
            product5.place_forget()
            product6.place_forget()
            product7.place_forget()
            product8.place_forget()
            product9.place_forget()
            product10.place_forget()
            product11.place_forget()
            product12.place_forget()
            product13.place_forget()
            product14.place_forget()
            product15.place_forget()
            product16.place_forget()
            order_label.place_forget()
            orstatus_label.place_forget()
            orders_catalog.place_forget()
            status_catalog.place_forget()
            cart_list.place_forget()
            card_picker.place_forget()
            cost_label.place_forget()

            recomended.place(x=20, y=5)
            rec_prod1.place(x=50, y=35)
            rec_prod2.place(x=190, y=35)
            rec_prod3.place(x=330, y=35)
            blackline.configure(height=1, width=430)
            blackline.place(x=20, y=145)
            categories.place(x=145, y=150)
            cat1.place(x=20, y=200)
            cat2.place(x=260, y=200)
            cat3.place(x=20, y=420)
            cat4.place(x=260, y=420)

        def open_cart():
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
            product1.place_forget()
            product2.place_forget()
            product3.place_forget()
            product4.place_forget()
            product5.place_forget()
            product6.place_forget()
            product7.place_forget()
            product8.place_forget()
            product9.place_forget()
            product10.place_forget()
            product11.place_forget()
            product12.place_forget()
            product13.place_forget()
            product14.place_forget()
            product15.place_forget()
            product16.place_forget()
            order_label.place_forget()
            orstatus_label.place_forget()
            orders_catalog.place_forget()
            status_catalog.place_forget()
            card_picker.place_forget()
            cost_label.place_forget()

            load_cart()

            def proceed():
                submit_button.place_forget()
                cart_list.place_forget()

                total_text = "Your total is:" + str(sum) + "€"
                conn = sqlite3.connect("myShop_prof.db")
                crs = conn.cursor()
                crs.execute("SELECT name FROM myShop_prof WHERE id=1;")
                entry_var = crs.fetchone()
                nameLB.place(x=35, y=170)
                name.configure(placeholder_text=entry_var)
                name.place(x=30, y=195)
                emailLB.place(x=35, y=230)
                crs.execute("SELECT email FROM myShop_prof WHERE id=1;")
                entry_var = crs.fetchone()
                email.configure(placeholder_text=entry_var)
                email.place(x=30, y=255)
                countryLB.place(x=35, y=290)
                crs.execute("SELECT country FROM myShop_prof WHERE id=1;")
                entry_var = crs.fetchone()
                country.configure(placeholder_text=entry_var)
                country.place(x=30, y=315)
                adressLb.place(x=35, y=360)
                crs.execute("SELECT adress FROM myShop_prof WHERE id=1;")
                entry_var = crs.fetchone()
                adress.configure(placeholder_text=entry_var)
                adress.place(x=30, y=375)
                postalcodeLb.place(x=35, y=410)
                crs.execute("SELECT postalcode FROM myShop_prof WHERE id=1;")
                entry_var = crs.fetchone()
                postalcode.configure(placeholder_text=entry_var)
                postalcode.place(x=30, y=435)

                card_picker.place(x=5, y=20)
                cost_label.configure(text=total_text)
                cost_label.place(x=20, y=490)
                submit_button.configure(
                    text="Complete Payment",
                    font=("arial", 22, "bold"),
                    text_color="grey30",
                    height=40,
                    width=120,
                    command=complete_order,
                )
                submit_button.place(x=130, y=580)

            cart_list.place(x=10, y=10)
            submit_button.configure(
                text="Proceed to payment >",
                font=("arial", 22, "bold"),
                text_color="grey30",
                height=30,
                width=90,
                command=proceed,
            )
            submit_button.place(x=200, y=580)

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
            product1.place_forget()
            product2.place_forget()
            product3.place_forget()
            product4.place_forget()
            product5.place_forget()
            product6.place_forget()
            product7.place_forget()
            product8.place_forget()
            product9.place_forget()
            product10.place_forget()
            product11.place_forget()
            product12.place_forget()
            product13.place_forget()
            product14.place_forget()
            product15.place_forget()
            product16.place_forget()
            order_label.place_forget()
            orstatus_label.place_forget()
            orders_catalog.place_forget()
            status_catalog.place_forget()
            cart_list.place_forget()
            card_picker.place_forget()
            cost_label.place_forget()

            assistance.place(x=10, y=20)
            reasonLB.place(x=10, y=100)
            reason.place(x=60, y=160)
            explanation.place(x=30, y=220)
            submit_button.configure(
                text="Submit help ticket",
                font=("arial", 20, "bold"),
                text_color="grey30",
                height=40,
                width=100,
                command=succesfull_submition,
            )
            submit_button.place(x=130, y=500)

        # Create profile widgets
        prof = customtkinter.CTkButton(
            profile_panel,
            text="Profile",
            font=("arial", 27, "bold"),
            text_color="grey30",
            fg_color="light blue",
            cursor="hand2",
            height=60,
            width=180,
            command=open_prof,
        )
        prof.pack(padx=5, pady=5)
        orders = customtkinter.CTkButton(
            profile_panel,
            text="My Orders",
            font=("arial", 27, "bold"),
            text_color="grey30",
            fg_color="light blue",
            cursor="hand2",
            height=60,
            width=180,
            command=open_orders,
        )
        orders.pack(padx=5, pady=20)
        shop_menu = customtkinter.CTkButton(
            profile_panel,
            text="Shop",
            font=("arial", 27, "bold"),
            text_color="grey30",
            fg_color="light blue",
            cursor="hand2",
            height=60,
            width=180,
            command=open_shop,
        )
        shop_menu.pack(padx=5, pady=10)
        cart = customtkinter.CTkButton(
            profile_panel,
            text="My Cart",
            font=("arial", 27, "bold"),
            text_color="grey30",
            fg_color="light blue",
            cursor="hand2",
            height=60,
            width=180,
            command=open_cart,
        )
        cart.pack(padx=5, pady=20)
        shop_help = customtkinter.CTkButton(
            profile_panel,
            text="Help",
            font=("arial", 27, "bold"),
            text_color="grey30",
            fg_color="light blue",
            cursor="hand2",
            height=60,
            width=180,
            command=open_shop_help,
        )
        shop_help.pack(padx=5, pady=260)


if __name__ == "__main__":
    app = MyShop()
    app.mainloop()
