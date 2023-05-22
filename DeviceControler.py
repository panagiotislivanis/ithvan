import json
import sqlite3
from tkinter import *
import tkinter
from tkinter import messagebox
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk


# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

class DeviceController(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Task Manager")
        self.geometry(f"{700}x{600}")
        self.resizable(False, False)
        
        # Create the left panel
        left_panel = customtkinter.CTkFrame(self, bg_color="grey30", width=200, height=400)
        left_panel.pack(side="left", fill="y", padx=10, pady=10)
        
        # Create the right panel
        right_panel = customtkinter.CTkFrame(self, bg_color="grey30", width=500, height=400)
        right_panel.pack(side="right", fill="both", padx=10, pady=10)
        
        #images
        off_lamp = customtkinter.CTkImage(light_image=Image.open("Images\Off-Lamp.png"), size=(120, 120))
        on_lamp = customtkinter.CTkImage(light_image=Image.open("Images\On-Lamp.png"), size=(120, 120))
        ac = customtkinter.CTkImage(light_image=Image.open("Images\AC.png"), size=(120, 120))
        fridgecat = customtkinter.CTkImage(light_image=Image.open("Images\Fridgecat.png"), size=(120, 120))
        hp = customtkinter.CTkImage(light_image=Image.open("Images\Heat_Pump.png"), size=(120, 120))
        mpajouria = customtkinter.CTkImage(light_image=Image.open("Images\Shutters.png"), size=(120, 120))
        
        
        #create a panel on top of another to make the icons dissapear
        #maintain button state = unsolved ???
                
        def open_bedroom():
            def on_lamp_handler():
                main_on_lamp = customtkinter.CTkButton(right_panel, image=on_lamp, text="", fg_color="turquoise1", cursor="hand2", height=200, width=180, command=off_lamp_handler)
                main_on_lamp.place(x=25, y=10)  
             
            def off_lamp_handler():
                main_off_lamp = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="turquoise4", cursor="hand2", height=200, width=180, command=on_lamp_handler)
                main_off_lamp.place(x=25, y=10)       
            
            def on_side_lamps_handler():
                on_side_lamps = customtkinter.CTkButton(right_panel, image=on_lamp, text="", fg_color="turquoise1", height=200, width=180, command=off_side_lamps_handler)
                on_side_lamps.place(x=255, y=10)
            
            def off_side_lamps_handler():
                off_side_lamps = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="turquoise4", height=200, width=180, command=on_side_lamps_handler)
                off_side_lamps.place(x=255, y=10)
                
            def on_AC():
                on_AC  = customtkinter.CTkButton(right_panel, image=ac, text="", fg_color="turquoise1", height=200, width=180, command=off_AC)
                on_AC.place(x=25, y=300)
            
            def off_AC():
                off_AC  = customtkinter.CTkButton(right_panel, image=ac, text="", fg_color="turquoise4", height=200, width=180, command=on_AC)
                off_AC.place(x=25, y=300)
            
            def temperature(value):
                temperature = customtkinter.CTkLabel(right_panel, text="%.1f" % value, fg_color="CadetBlue4", height=10, width=10)
                temperature.place(x=207, y=555)
            
            def closing_shutters():
                closed_shutters  = customtkinter.CTkButton(right_panel, image=mpajouria, text="", fg_color="turquoise1", height=200, width=180, command=opening_shutters)
                closed_shutters.place(x=255, y=300)
                
                
            def opening_shutters():
                opened_shutters  = customtkinter.CTkButton(right_panel, image=mpajouria, text="", fg_color="turquoise4", height=200, width=180, command=closing_shutters)
                opened_shutters.place(x=255, y=300)
            
            
            main_off_lamp = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="turquoise4", cursor="hand2", height=200, width=180, command=on_lamp_handler)
            main_off_lamp.place(x=25, y=10)
            main_lamp_label = customtkinter.CTkLabel(right_panel, text="Adjust Brightness", fg_color="CadetBlue4", height=30, width=120)
            main_lamp_label.place(x=55, y=225)
            main_lamp_slider = customtkinter.CTkSlider(right_panel, from_=0, to=100, bg_color="CadetBlue4")
            main_lamp_slider.place(x=15, y=265)
            
            side_lamps = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="turquoise4", height=200, width=180, command=on_side_lamps_handler)
            side_lamps.place(x=255, y=10)
            side_lamps_label = customtkinter.CTkLabel(right_panel, text="Adjust Brightness", fg_color="CadetBlue4", height=30, width=120)
            side_lamps_label.place(x=285, y=225)
            side_lamps_slider = customtkinter.CTkSlider(right_panel, from_=0, to=100, bg_color="CadetBlue4")
            side_lamps_slider.place(x=245, y=265)
            
            aircondition = customtkinter.CTkButton(right_panel, image=ac, text="", fg_color="turquoise4", height=200, width=180, command=on_AC)
            aircondition.place(x=25, y=300)
            aircodition_label = customtkinter.CTkLabel(right_panel, text="Temperature", fg_color="CadetBlue4", height=30, width=120)
            aircodition_label.place(x=55, y=515)
            aircodition_slider = customtkinter.CTkSlider(right_panel, from_=15, to=28, bg_color="CadetBlue4", command=temperature)
            aircodition_slider.place(x=5, y=555)
            
            shutters = customtkinter.CTkButton(right_panel, image=mpajouria, text="", fg_color="turquoise4", height=200, width=180, command=closing_shutters)
            shutters.place(x=255, y=300)
        
        def open_LR():
            def on_lamp1_handler():
                main_on_lamp = customtkinter.CTkButton(right_panel, image=on_lamp, text="", fg_color="IndianRed1", cursor="hand2", height=200, width=180, command=off_lamp1_handler)
                main_on_lamp.place(x=25, y=10)  
             
            def off_lamp1_handler():
                main_off_lamp = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="IndianRed4", cursor="hand2", height=200, width=180, command=on_lamp1_handler)
                main_off_lamp.place(x=25, y=10)       
            
            def on_lamp2_handler():
                on_side_lamps = customtkinter.CTkButton(right_panel, image=on_lamp, text="", fg_color="IndianRed1", height=200, width=180, command=off_lamp2_handler)
                on_side_lamps.place(x=255, y=10)
            
            def off_lamp2_handler():
                off_side_lamps = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="IndianRed4", height=200, width=180, command=on_lamp2_handler)
                off_side_lamps.place(x=255, y=10)
                
            def on_lamp3_handler():
                on_side_lamps = customtkinter.CTkButton(right_panel, image=on_lamp, text="", fg_color="IndianRed1", height=200, width=180, command=off_lamp3_handler)
                on_side_lamps.place(x=25, y=300)
            
            def off_lamp3_handler():
                off_side_lamps = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="IndianRed4", height=200, width=180, command=on_lamp3_handler)
                off_side_lamps.place(x=25, y=300)
                
            def on_AC():
                on_AC  = customtkinter.CTkButton(right_panel, image=ac, text="", fg_color="IndianRed1", height=200, width=180, command=off_AC)
                on_AC.place(x=255, y=300)
            
            def off_AC():
                off_AC  = customtkinter.CTkButton(right_panel, image=ac, text="", fg_color="IndianRed4", height=200, width=180, command=on_AC)
                off_AC.place(x=255, y=300)
            
            def temperature(value):
                temperature = customtkinter.CTkLabel(right_panel, text="%.1f" % value, fg_color="CadetBlue4", height=10, width=10)
                temperature.place(x=433, y=555)
            
            main_off_lamp = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="IndianRed4", cursor="hand2", height=200, width=180, command=on_lamp1_handler)
            main_off_lamp.place(x=25, y=10)
            main_lamp_label = customtkinter.CTkLabel(right_panel, text="Adjust Brightness", fg_color="RosyBrown4", height=30, width=120)
            main_lamp_label.place(x=55, y=225)
            main_lamp_slider = customtkinter.CTkSlider(right_panel, from_=0, to=100, bg_color="RosyBrown4")
            main_lamp_slider.place(x=15, y=265)
            
            side_lamp = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="IndianRed4", height=200, width=180, command=on_lamp2_handler)
            side_lamp.place(x=255, y=10)
            side_lamp_label = customtkinter.CTkLabel(right_panel, text="Adjust Brightness", fg_color="RosyBrown4", height=30, width=120)
            side_lamp_label.place(x=285, y=225)
            side_lamp_slider = customtkinter.CTkSlider(right_panel, from_=0, to=100, bg_color="RosyBrown4")
            side_lamp_slider.place(x=245, y=265)
            
            side_lamp2 = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="IndianRed4", height=200, width=180, command=on_lamp3_handler)
            side_lamp2.place(x=25, y=300)
            side_lamp2_label = customtkinter.CTkLabel(right_panel, text="Adjust Brightness", fg_color="RosyBrown4", height=30, width=120)
            side_lamp2_label.place(x=55, y=515)
            side_lamp2_slider = customtkinter.CTkSlider(right_panel, from_=0, to=100, bg_color="RosyBrown4")
            side_lamp2_slider.place(x=15, y=555)
            
            aircondition = customtkinter.CTkButton(right_panel, image=ac, text="", fg_color="IndianRed4", height=200, width=180, command=on_AC)
            aircondition.place(x=255, y=300)
            aircodition_label = customtkinter.CTkLabel(right_panel, text="Temperature", fg_color="RosyBrown4", height=30, width=120)
            aircodition_label.place(x=285, y=515)
            aircodition_slider = customtkinter.CTkSlider(right_panel, from_=15, to=28, bg_color="RosyBrown4", command=temperature)
            aircodition_slider.place(x=230, y=555)
            
        def open_kitchen():
            def on_mainlamp_handler():
                main_on_lamp = customtkinter.CTkButton(right_panel, image=on_lamp, text="", fg_color="turquoise1", cursor="hand2", height=200, width=180, command=off_mainlamp_handler)
                main_on_lamp.place(x=25, y=10)  
             
            def off_mainlamp_handler():
                main_off_lamp = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="turquoise4", cursor="hand2", height=200, width=180, command=on_mainlamp_handler)
                main_off_lamp.place(x=25, y=10)
            
            def temperature(value):
                temperature = customtkinter.CTkLabel(right_panel, text="%.1f" % value, fg_color="CadetBlue4", height=10, width=10)
                temperature.place(x=433, y=265)
            
            main_off_lamp = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="turquoise4", cursor="hand2", height=200, width=180, command=on_mainlamp_handler)
            main_off_lamp.place(x=25, y=10)
            main_lamp_label = customtkinter.CTkLabel(right_panel, text="Adjust Brightness", fg_color="CadetBlue4", height=30, width=120)
            main_lamp_label.place(x=55, y=225)
            main_lamp_slider = customtkinter.CTkSlider(right_panel, from_=0, to=100, bg_color="CadetBlue4")
            main_lamp_slider.place(x=15, y=265)    

            fridge = customtkinter.CTkButton(right_panel, image=fridgecat, text="", fg_color="turquoise1", height=200, width=180)
            fridge.place(x=255, y=10)
            fridge_label = customtkinter.CTkLabel(right_panel, text="Temperature", fg_color="CadetBlue4", height=30, width=120)
            fridge_label.place(x=285, y=225)
            fridgetmp_slider = customtkinter.CTkSlider(right_panel, from_=2, to=8, bg_color="CadetBlue4", command=temperature)
            fridgetmp_slider.place(x=230, y=265) 

            
        def open_bathroom():
            def on_lamp_handler():
                main_on_lamp = customtkinter.CTkButton(right_panel, image=on_lamp, text="", fg_color="IndianRed1", cursor="hand2", height=200, width=180, command=off_lamp_handler)
                main_on_lamp.place(x=25, y=10)  
             
            def off_lamp_handler():
                main_off_lamp = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="IndianRed4", cursor="hand2", height=200, width=180, command=on_lamp_handler)
                main_off_lamp.place(x=25, y=10)
                
            def on_heat_pump():
                on_side_lamps = customtkinter.CTkButton(right_panel, image=hp, text="", fg_color="IndianRed1", height=200, width=180, command=off_heat_pump)
                on_side_lamps.place(x=255, y=10)
            
            def off_heat_pump():
                off_side_lamps = customtkinter.CTkButton(right_panel, image=hp, text="", fg_color="IndianRed4", height=200, width=180, command=on_heat_pump)
                off_side_lamps.place(x=255, y=10)
                
            def heatpump_switch(value):
                scale = customtkinter.CTkLabel(right_panel, text="%d" % value, fg_color="RosyBrown4", height=10, width=10)
                scale.place(x=438, y=265)
            
            main_off_lamp = customtkinter.CTkButton(right_panel, image=off_lamp, text="", fg_color="IndianRed4", cursor="hand2", height=200, width=180, command=on_lamp_handler)
            main_off_lamp.place(x=25, y=10)
            main_lamp_label = customtkinter.CTkLabel(right_panel, text="Adjust Brightness", fg_color="RosyBrown4", height=30, width=120)
            main_lamp_label.place(x=55, y=225)
            main_lamp_slider = customtkinter.CTkSlider(right_panel, from_=0, to=100, bg_color="RosyBrown4")
            main_lamp_slider.place(x=15, y=265)
            
            heatpump = customtkinter.CTkButton(right_panel, image=hp, text="", fg_color="IndianRed4", cursor="hand2", height=200, width=180, command=on_heat_pump)
            heatpump.place(x=255, y=10)
            heatpump_label = customtkinter.CTkLabel(right_panel, text="Scale", fg_color="RosyBrown4", height=30, width=120)
            heatpump_label.place(x=285, y=225)
            heatpump_slider = customtkinter.CTkSlider(right_panel, from_=1, to=5, bg_color="RosyBrown4", command=heatpump_switch)
            heatpump_slider.place(x=235, y=265) 
            
            
        #def open_garage():
            
            
        #def open_garden():
            
            
        #def open_others():
            
            
        #buttons for different rooms
        bedroom = customtkinter.CTkButton(left_panel, text="Bedroom", font=('Comic Sans MS', 27, 'bold'), fg_color="turquoise4", cursor="hand2", height=60, width=180, command=open_bedroom)
        bedroom.place(x=10, y=20)
        living_room = customtkinter.CTkButton(left_panel, text="Living Room", font=('Comic Sans MS', 27, 'bold'), fg_color="IndianRed4", cursor="hand2", height=60, width=180, command=open_LR)
        living_room.place(x=10, y=100)
        kitchen = customtkinter.CTkButton(left_panel, text="Kitchen", font=('Comic Sans MS', 27, 'bold'), fg_color="turquoise4", cursor="hand2", height=60, width=180, command=open_kitchen)
        kitchen.place(x=10, y=180)
        bathroom = customtkinter.CTkButton(left_panel, text="Bathroom", font=('Comic Sans MS', 27, 'bold'), fg_color="IndianRed4", cursor="hand2", height=60, width=180, command=open_bathroom)
        bathroom.place(x=10, y=260)
        garage = customtkinter.CTkButton(left_panel, text="Garage", font=('Comic Sans MS', 27, 'bold'), fg_color="turquoise4", cursor="hand2", height=60, width=180)
        garage.place(x=10, y=340)
        garden = customtkinter.CTkButton(left_panel, text="Garden", font=('Comic Sans MS', 27, 'bold'), fg_color="IndianRed4", cursor="hand2", height=60, width=180)
        garden.place(x=10, y=420)
        other_devices = customtkinter.CTkButton(left_panel, text="Other", font=('Comic Sans MS', 27, 'bold'), fg_color="turquoise4", cursor="hand2", height=60, width=180)
        other_devices.place(x=10, y=500)
        
        
        
if __name__ == "__main__":
    app = DeviceController()
    app.mainloop()