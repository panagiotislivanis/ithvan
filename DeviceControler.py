import itertools
import json
import sqlite3
from tkinter import *
import tkinter
from tkinter import messagebox
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk

current_camera = 0

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
        right_panel = customtkinter.CTkFrame(self, bg_color="grey30", width=500, height=600)
        right_panel.pack(side="right", fill="both", padx=10, pady=10)

        #images
        off_lamp = customtkinter.CTkImage(light_image=Image.open("Images\Off-Lamp.png"), size=(120, 120))
        on_lamp = customtkinter.CTkImage(light_image=Image.open("Images\On-Lamp.png"), size=(120, 120))
        ac = customtkinter.CTkImage(light_image=Image.open("Images\AC.png"), size=(120, 120))
        rgb = customtkinter.CTkImage(light_image=Image.open("Images\RGB.png"), size=(120, 120))
        fridgecat = customtkinter.CTkImage(light_image=Image.open("Images\Fridgecat.png"), size=(120, 120))
        hp = customtkinter.CTkImage(light_image=Image.open("Images\Heat_Pump.png"), size=(120, 120))
        mpajouria = customtkinter.CTkImage(light_image=Image.open("Images\Shutters.png"), size=(120, 120))
        opened_garagedoor = customtkinter.CTkImage(light_image=Image.open("Images\Opened_Garage.png"), size=(120, 120))
        closed_garagedoor = customtkinter.CTkImage(light_image=Image.open("Images\Closed_Garage.png"), size=(120, 120))
        water_sprinkles = customtkinter.CTkImage(light_image=Image.open("Images\Watering.png"), size=(120, 120))
        thermostat = customtkinter.CTkImage(light_image=Image.open("Images\Thermostat.png"), size=(120, 120))
        water_heater = customtkinter.CTkImage(light_image=Image.open("Images\HotTabStream.png"), size=(120, 120))
        cameraPNG = customtkinter.CTkImage(light_image=Image.open("Images\Camera.png"), size=(120, 120))
        forward_arrow = customtkinter.CTkImage(light_image=Image.open("Images\Forward.png"), size=(60, 60))
        previous_arrow = customtkinter.CTkImage(light_image=Image.open("Images\Previous.png"), size=(60, 60))
        entrance = customtkinter.CTkImage(light_image=Image.open("Images\Entrance.jpg"), size=(780, 465))
        garageCamera = customtkinter.CTkImage(light_image=Image.open("Images\GarageCamera.jpg"), size=(780, 465))
        lr1 = customtkinter.CTkImage(light_image=Image.open("Images\LR1.jpg"), size=(780, 465))
        lr2 = customtkinter.CTkImage(light_image=Image.open("Images\LR2.jpg"), size=(780, 465))
        kitchenCamera = customtkinter.CTkImage(light_image=Image.open("Images\Kitchen.jpg"), size=(780, 465))
        g1 = customtkinter.CTkImage(light_image=Image.open("Images\Garden1.jpg"), size=(780, 465))
        g2 = customtkinter.CTkImage(light_image=Image.open("Images\Garden2.jpg"), size=(780, 465))
        rabbit = customtkinter.CTkImage(light_image=Image.open("Images\Rabbit.png"), size=(80, 80))
        turtle = customtkinter.CTkImage(light_image=Image.open("Images\Turtle.png"), size=(80, 80))
        
        #maintain button state = unsolved ???
        #1st row 1st column widgets
        def on_lamp_handler_t():
            main_lamp.configure(image=on_lamp, fg_color="turquoise1", command=off_lamp_handler_t) 
        
        def off_lamp_handler_t():
            main_lamp.configure(image=off_lamp, fg_color="turquoise4", command=on_lamp_handler_t)
             
        def on_lamp_handler_r():
            main_lamp.configure(image=on_lamp, fg_color="IndianRed1", command=off_lamp_handler_r) 
            
        def off_lamp_handler_r():
            main_lamp.configure(image=off_lamp, fg_color="IndianRed4", command=on_lamp_handler_r)
            
        def on_thermo():
            main_lamp.configure(fg_color="turquoise1", command=off_thermo)
            
        def off_thermo():
            main_lamp.configure(fg_color="turquoise4", command=on_thermo)
            
        def temperature(value):
            temperatureL.configure(text="%.1f" % value)
        
        #1st row 2nd column widgets
        def on_side_lamps_handler_t():
            side_lamps.configure(image=on_lamp, fg_color="turquoise1", command=off_side_lamps_handler_t)
            
        def off_side_lamps_handler_t():
            side_lamps.configure(image=off_lamp, fg_color="turquoise4", command=on_side_lamps_handler_t)
        
        def on_side_lamps_handler_r():
            side_lamps.configure(image=on_lamp, fg_color="IndianRed1", command=off_side_lamps_handler_r)
            
            
        def off_side_lamps_handler_r():
            side_lamps.configure(image=off_lamp, fg_color="IndianRed4", command=on_side_lamps_handler_r)
        
        def on_heat_pump():
            side_lamps.configure(image=hp, fg_color="IndianRed1", command=off_heat_pump)
            
        def off_heat_pump():
            side_lamps(image=hp, fg_color="IndianRed4", command=on_heat_pump)

        def heatpump_switch(value):
            scale.configure(text="%d" % value)
            
        def open_garagedoor():
            side_lamps.configure(image=opened_garagedoor, fg_color="turquoise1", command=close_garagedoor)
                
        def close_garagedoor():
            side_lamps.configure(image=closed_garagedoor, fg_color="turquoise4", command=open_garagedoor)
            
        def on_water_sprinkles():
            side_lamps.configure(fg_color="IndianRed1", command=off_water_sprinkles)

        def off_water_sprinkles():
            side_lamps.configure(fg_color="IndianRed4", command=on_water_sprinkles)
            
        def on_water_heater():
            side_lamps.configure(fg_color="turquoise1", command=off_water_heater)
            
        def off_water_heater():
            side_lamps.configure(fg_color="turquoise4", command=on_water_heater)
            
        #2nd row 1st column widgets
        def on_AC():
            aircondition.configure(fg_color="turquoise1", command=off_AC)
            
        def off_AC():
            aircondition.configure(fg_color="turquoise4", command=on_AC)
            
        def led_handler():
            popup = CTkToplevel()
            popup.title("RGB Controler")
            popup.geometry('800x600+900+180')
            popup.resizable(False, False)
            # Create watch panel
            rgb_panel = customtkinter.CTkFrame(popup, bg_color="grey30", width=780, height=400)
            rgb_panel.pack(side="top", fill="y", padx=10, pady=10)
        
            # Create swap panel
            settings_panel = customtkinter.CTkFrame(popup, bg_color="grey30", width=780, height=180)
            settings_panel.pack(side="bottom", fill="both", padx=10, pady=10)
            
            red = customtkinter.CTkButton(rgb_panel, text="", fg_color="red", bg_color="grey30", cursor="hand2", width=170, height=170)
            red.place(x=5, y=5)
            yellow = customtkinter.CTkButton(rgb_panel, text="", fg_color="yellow", bg_color="grey30", cursor="hand2", width=170, height=170)
            yellow.place(x=205, y=5)
            green = customtkinter.CTkButton(rgb_panel, text="", fg_color="green", bg_color="grey30", cursor="hand2", width=170, height=170)
            green.place(x=405, y=5)
            cyan = customtkinter.CTkButton(rgb_panel, text="", fg_color="cyan", bg_color="grey30", cursor="hand2", width=170, height=170)
            cyan.place(x=605, y=5)
            navy = customtkinter.CTkButton(rgb_panel, text="", fg_color="navy", bg_color="grey30", cursor="hand2", width=170, height=170)
            navy.place(x=5, y=205)
            dark_violet = customtkinter.CTkButton(rgb_panel, text="", fg_color="dark violet", bg_color="grey30", cursor="hand2", width=170, height=170)
            dark_violet.place(x=205, y=205)
            deep_pink = customtkinter.CTkButton(rgb_panel, text="", fg_color="deep pink", bg_color="grey30", cursor="hand2", width=170, height=170)
            deep_pink.place(x=405, y=205)
            white = customtkinter.CTkButton(rgb_panel, text="", fg_color="white", bg_color="grey30", cursor="hand2", width=170, height=170)
            white.place(x=605, y=205)
            
            mode = customtkinter.CTkComboBox(settings_panel, values=["Rainbow", "Breath", "Flash", "Steady", "Randomize"])
            mode.place(x=50, y=20)
            speed_slider = customtkinter.CTkSlider(settings_panel, bg_color="grey40")
            speed_slider.place(x=400, y=50)
            slow = customtkinter.CTkLabel(settings_panel, text="", image=turtle, width=100, height=100)
            slow.place(x=280, y=10)
            fast = customtkinter.CTkLabel(settings_panel, text="", image=rabbit, width=100, height=100)
            fast.place(x=600, y=5)
            speed = customtkinter.CTkLabel(settings_panel, text="Select Speed", font=('Comic Sans MS', 18, 'bold'), fg_color="grey35", width=140, height=35)
            speed.place(x=435, y=90)
        
        def open_camera_controler():
                popup = CTkToplevel()
                popup.title("ITHVAN SECURITY corp.")
                popup.geometry('800x600+900+180')
                popup.resizable(False, False)
                
                # Create watch panel
                watch_panel = customtkinter.CTkFrame(popup, bg_color="grey30", width=780, height=465)
                watch_panel.pack(side="top", fill="y", padx=10, pady=10)
        
                # Create swap panel
                swap_panel = customtkinter.CTkFrame(popup, bg_color="grey30", width=780, height=115)
                swap_panel.pack(side="bottom", fill="both", padx=10, pady=10)
                
                cameraID = ["Entrance", "Garage", "Living Room 1", "Living Room 2", "Kitchen", "Garden 1", "Garden 2"]

                def next_camera():
                    global current_camera
                    current_camera = (current_camera + 1) % len(cameraID)
                    cameraLabel.configure(text=cameraID[current_camera])
                    if(cameraID[current_camera] == "Entrance"):
                        footage.configure(image=entrance)
                    elif(cameraID[current_camera] == "Garage"):
                        footage.configure(image=garageCamera)
                    elif (cameraID[current_camera] == "Living Room 1"):
                        footage.configure(image=lr1)
                    elif (cameraID[current_camera] == "Living Room 2"):
                        footage.configure(image=lr2)
                    elif (cameraID[current_camera] == "Kitchen"):
                        footage.configure(image=kitchenCamera)
                    elif (cameraID[current_camera] == "Garden 1"):
                        footage.configure(image=g1)
                    elif (cameraID[current_camera] == "Garden 2"):
                        footage.configure(image=g2)
                
                def previous_camera():
                    global current_camera
                    current_camera = (current_camera - 1) % len(cameraID)
                    cameraLabel.configure(text=cameraID[current_camera])
                    if(cameraID[current_camera] == "Entrance"):
                        footage.configure(image=entrance)
                    elif (cameraID[current_camera] == "Garage"):
                        footage.configure(image=garageCamera)
                    elif (cameraID[current_camera] == "Living Room 1"):
                        footage.configure(image=lr1)
                    elif (cameraID[current_camera] == "Living Room 2"):
                        footage.configure(image=lr2)
                    elif (cameraID[current_camera] == "Kitchen"):
                        footage.configure(image=kitchenCamera)
                    elif (cameraID[current_camera] == "Garden 1"):
                        footage.configure(image=g1)
                    elif (cameraID[current_camera] == "Garden 2"):
                        footage.configure(image=g2)
                
                footage = customtkinter.CTkLabel(watch_panel, image=entrance, text="")
                footage.place(x=0, y=0)
                forward = customtkinter.CTkButton(swap_panel, image=forward_arrow, text="", fg_color="turquoise4", cursor="hand2", height=80, width=80, command=next_camera)
                forward.place(x=678, y=5)
                previous = customtkinter.CTkButton(swap_panel, image=previous_arrow, text="", fg_color="turquoise4", cursor="hand2", height=80, width=80, command=previous_camera)
                previous.place(x=24, y=5)
                cameraLabel = customtkinter.CTkLabel(swap_panel, text=cameraID[current_camera], font=('Comic Sans MS', 27, 'bold'), text_color="black", fg_color="turquoise4", height=80, width=550)
                cameraLabel.place(x=115, y=5)
        
        #2nd row 2nd column widgets
        def closing_shutters():
            shutters.configure(fg_color="turquoise1", command=opening_shutters)
                
        def opening_shutters():
            shutters.configure(fg_color="turquoise4", command=closing_shutters)
            
        def on_AC2():
            shutters.configure(fg_color="IndianRed1", command=off_AC2)
            
        def off_AC2():
            shutters.configure(fg_color="IndianRed4", command=on_AC2)
                            
        main_lamp = customtkinter.CTkButton(right_panel, text="", cursor="hand2", height=200, width=180)
        main_lamp_label = customtkinter.CTkLabel(right_panel, height=30, width=120)
        main_lamp_slider = customtkinter.CTkSlider(right_panel, from_=0, to=100)
        temperatureL = customtkinter.CTkLabel(right_panel, height=10, width=10)
        side_lamps = customtkinter.CTkButton(right_panel, text="", cursor="hand2", height=200, width=180)
        side_lamps_label = customtkinter.CTkLabel(right_panel, height=30, width=120)
        side_lamps_slider = customtkinter.CTkSlider(right_panel, from_=0, to=100)
        scale = customtkinter.CTkLabel(right_panel, height=10, width=10)
        aircondition = customtkinter.CTkButton(right_panel, text="", cursor="hand2", height=200, width=180)
        aircondition_label = customtkinter.CTkLabel(right_panel, height=30, width=120)
        aircondition_slider = customtkinter.CTkSlider(right_panel)
        ithvan_security = customtkinter.CTkLabel(right_panel, text="Ithvan Security", font=('System', 24, 'bold'), fg_color="CadetBlue4", height=60, width=145)
        shutters = customtkinter.CTkButton(right_panel, text="", cursor="hand2", height=200, width=180, command=closing_shutters)
        shutters_label = customtkinter.CTkLabel(right_panel, height=30, width=120)
        shutters_slider = customtkinter.CTkSlider(right_panel)
                    
        def open_bedroom():
            
            temperatureL.place_forget()
            scale.place_forget()
            ithvan_security.place_forget()
            shutters_label.place_forget()
            shutters_slider.place_forget()
            main_lamp.place(x=25, y=10)
            main_lamp_label.place(x=55, y=225)
            main_lamp_slider.place(x=15, y=265)
            main_lamp.configure(image=off_lamp, fg_color="turquoise4", command=on_lamp_handler_t)
            main_lamp_label.configure(text="Adjust Brightness", fg_color="CadetBlue4")
            main_lamp_slider.configure(bg_color="CadetBlue4")

            side_lamps.place(x=255, y=10)
            side_lamps_label.place(x=285, y=225)
            side_lamps_slider.place(x=245, y=265)
            side_lamps.configure(image=off_lamp, fg_color="turquoise4", command=on_side_lamps_handler_t)
            side_lamps_label.configure(text="Adjust Brightness", fg_color="CadetBlue4")
            side_lamps_slider.configure(bg_color="CadetBlue4")

            aircondition.place(x=25, y=300)
            aircondition_label.place(x=55, y=515)
            aircondition_slider.place(x=5, y=555)
            temperatureL.place(x=207, y=555)
            aircondition.configure(image=ac, fg_color="turquoise4", command=on_AC)
            aircondition_label.configure(text="Temperature", fg_color="CadetBlue4")
            aircondition_slider.configure(from_=15, to=28, bg_color="CadetBlue4", command=temperature)
            temperatureL.configure(text="22.5", fg_color="CadetBlue4")
            
            shutters.place(x=255, y=300)
            shutters.configure(image=mpajouria, fg_color="turquoise4", command=closing_shutters)
        
        def open_LR():
            
            
       
            
                
            

            
            temperatureL.place_forget()
            scale.place_forget()
            ithvan_security.place_forget()
            main_lamp.place(x=25, y=10)
            main_lamp_label.place(x=55, y=225)
            main_lamp_slider.place(x=15, y=265)
            main_lamp.configure( image=off_lamp, fg_color="IndianRed4", command=on_lamp_handler_r)
            main_lamp_label.configure( text="Adjust Brightness", fg_color="RosyBrown4")
            main_lamp_slider.configure(bg_color="RosyBrown4")

            side_lamps.place(x=255, y=10)
            side_lamps_label.place(x=285, y=225)
            side_lamps_slider.place(x=245, y=265)
            side_lamps.configure( image=off_lamp, fg_color="IndianRed4", command=on_side_lamps_handler_r)
            side_lamps_label.configure( text="Adjust Brightness", fg_color="RosyBrown4")
            side_lamps_slider.configure(bg_color="RosyBrown4")
            
            aircondition.place(x=25, y=300)
            aircondition_label.place(x=55, y=515)
            aircondition_slider.place(x=5, y=555)
            aircondition.configure(image=rgb, fg_color="IndianRed4", command=led_handler)
            aircondition_label.configure(text="Adjust Brightness", fg_color="RosyBrown4")
            aircondition_slider.configure(bg_color="RosyBrown4")
            

            #AC
            shutters.place(x=255, y=300)
            shutters_label.place(x=285, y=515)
            shutters_slider.place(x=230, y=555)
            temperatureL.place(x=434, y=555)
            shutters.configure(image=ac, fg_color="IndianRed4", command=on_AC2)
            shutters_label.configure(text="Temperature", fg_color="RosyBrown4")
            shutters_slider.configure(from_=15, to=28,bg_color="RosyBrown4", command=temperature)
            temperatureL.configure(text="22.5", fg_color="RosyBrown4")
            
        #smart devide handler for the kitchen
        def open_kitchen():

            temperatureL.place_forget()
            scale.place_forget()
            aircondition.place_forget()
            aircondition_label.place_forget()
            aircondition_slider.place_forget()
            ithvan_security.place_forget()
            shutters.place_forget()
            shutters_label.place_forget()
            shutters_slider.place_forget()
            main_lamp.place(x=25, y=10)
            main_lamp_label.place(x=55, y=225)
            main_lamp_slider.place(x=15, y=265)
            main_lamp.configure( image=off_lamp, fg_color="turquoise4", command=on_lamp_handler_t)
            main_lamp_label.configure( text="Adjust Brightness", fg_color="CadetBlue4")
            main_lamp_slider.configure(bg_color="CadetBlue4")
            
            side_lamps.place(x=255, y=10)
            side_lamps_label.place(x=285, y=225)
            side_lamps_slider.place(x=230, y=265)
            temperatureL.place(x=433, y=265)
            side_lamps.configure( image=fridgecat, fg_color="turquoise1", cursor="", command=None)
            side_lamps_label.configure( text="Temnperature", fg_color="CadetBlue4")
            side_lamps_slider.configure(from_=2, to=8, bg_color="CadetBlue4", command=temperature) 
            temperatureL.configure(text="5", fg_color="CadetBlue4")    

        #smart device handler for the bathroom
        def open_bathroom():
            
            temperatureL.place_forget()
            scale.place_forget()
            aircondition.place_forget()
            aircondition_label.place_forget()
            aircondition_slider.place_forget()
            ithvan_security.place_forget()
            shutters.place_forget()
            shutters_label.place_forget()
            shutters_slider.place_forget()
            main_lamp.place(x=25, y=10)
            main_lamp_label.place(x=55, y=225)
            main_lamp_slider.place(x=15, y=265)
            main_lamp.configure( image=off_lamp, fg_color="IndianRed4", command=on_lamp_handler_r)
            main_lamp_label.configure( text="Adjust Brightness", fg_color="RosyBrown4")
            main_lamp_slider.configure(bg_color="RosyBrown4")
            
            side_lamps.place(x=255, y=10)
            side_lamps_label.place(x=285, y=225)
            side_lamps_slider.place(x=235, y=265)
            scale.place(x=438, y=265)
            side_lamps.configure( image=hp, fg_color="IndianRed4", command=on_heat_pump)
            side_lamps_label.configure( text="Temnperature", fg_color="RosyBrown4")
            side_lamps_slider.configure(from_=1, to=5, bg_color="RosyBrown4", command=heatpump_switch) 
            scale.configure(text="3", fg_color="RosyBrown4")
        
        #smart device handler for the garage    
        def open_garage():
            
            temperatureL.place_forget()
            scale.place_forget()
            aircondition.place_forget()
            aircondition_label.place_forget()
            aircondition_slider.place_forget()
            ithvan_security.place_forget()
            side_lamps_label.place_forget()
            side_lamps_slider.place_forget()
            shutters.place_forget()
            shutters_label.place_forget()
            shutters_slider.place_forget()
            main_lamp.place(x=25, y=10)
            main_lamp_label.place(x=55, y=225)
            main_lamp_slider.place(x=15, y=265)
            main_lamp.configure( image=off_lamp, fg_color="turquoise4", command=on_lamp_handler_t)
            main_lamp_label.configure( text="Adjust Brightness", fg_color="CadetBlue4")
            main_lamp_slider.configure(bg_color="CadetBlue4")
            
            side_lamps.place(x=255, y=10)
            side_lamps.configure( image=closed_garagedoor, fg_color="turquoise4", command=open_garagedoor)
 
        #smart device handler for the garden
        def open_garden():
            
            temperatureL.place_forget()
            scale.place_forget()    
            aircondition.place_forget()
            aircondition_label.place_forget()
            aircondition_slider.place_forget()
            ithvan_security.place_forget()
            shutters.place_forget()
            shutters_label.place_forget()
            shutters_slider.place_forget()
            main_lamp.place(x=25, y=10)
            main_lamp_label.place(x=55, y=225)
            main_lamp_slider.place(x=15, y=265)
            main_lamp.configure( image=off_lamp, fg_color="IndianRed4", command=on_lamp_handler_r)
            main_lamp_label.configure( text="Adjust Brightness", fg_color="RosyBrown4")
            main_lamp_slider.configure(bg_color="RosyBrown4")
            
            side_lamps.place(x=255, y=10)
            side_lamps_label.place(x=285, y=225)
            side_lamps_slider.place(x=235, y=265)
            scale.place(x=438, y=265)
            side_lamps.configure( image=water_sprinkles, fg_color="IndianRed4", command=on_water_sprinkles)
            side_lamps_label.configure( text="Mode", fg_color="RosyBrown4")
            side_lamps_slider.configure(from_=1, to=5, bg_color="RosyBrown4", command=heatpump_switch) 
            scale.configure(text="3", fg_color="RosyBrown4") 
        
        #smart device handler for the rest of the devices
        def open_others():
            
            temperatureL.place_forget()
            scale.place_forget()
            aircondition_label.place_forget()
            aircondition_slider.place_forget()
            shutters.place_forget()
            shutters_label.place_forget()
            shutters_slider.place_forget()
            main_lamp.place(x=25, y=10)
            main_lamp_label.place(x=55, y=225)
            main_lamp_slider.place(x=4, y=265)
            temperatureL.place(x=208, y=265)
            main_lamp.configure( image=thermostat, fg_color="turquoise4", command=on_thermo)
            main_lamp_label.configure(text="Temperature", fg_color="CadetBlue4")
            main_lamp_slider.configure(from_=18, to=30, bg_color="CadetBlue4", command=temperature)
            temperatureL.configure(text="24", fg_color="CadetBlue4")
            
            side_lamps.place(x=255, y=10)
            side_lamps_label.place(x=285, y=225)
            side_lamps_slider.place(x=235, y=265)
            scale.place(x=438, y=265)
            side_lamps.configure( image=water_heater, fg_color="turquoise4", command=on_water_heater)
            side_lamps_label.configure( text="Heating Temperature", fg_color="CadetBlue4")
            side_lamps_slider.configure(from_=45, to=85, bg_color="CadetBlue4", command=heatpump_switch) 
            scale.configure(text="65", fg_color="CadetBlue4")
            
            aircondition.place(x=25, y=300)
            ithvan_security.place(x=17, y=515)
            aircondition.configure(image=cameraPNG, fg_color="turquoise4", command=open_camera_controler)


        #buttons for different rooms
        bedroom = customtkinter.CTkButton(left_panel, text="Bedroom", font=('Comic Sans MS', 27, 'bold'), fg_color="turquoise4", cursor="hand2", height=60, width=180, command=open_bedroom)
        bedroom.place(x=10, y=20)
        living_room = customtkinter.CTkButton(left_panel, text="Living Room", font=('Comic Sans MS', 27, 'bold'), fg_color="IndianRed4", cursor="hand2", height=60, width=180, command=open_LR)
        living_room.place(x=10, y=100)
        kitchen = customtkinter.CTkButton(left_panel, text="Kitchen", font=('Comic Sans MS', 27, 'bold'), fg_color="turquoise4", cursor="hand2", height=60, width=180, command=open_kitchen)
        kitchen.place(x=10, y=180)
        bathroom = customtkinter.CTkButton(left_panel, text="Bathroom", font=('Comic Sans MS', 27, 'bold'), fg_color="IndianRed4", cursor="hand2", height=60, width=180, command=open_bathroom)
        bathroom.place(x=10, y=260)
        garage = customtkinter.CTkButton(left_panel, text="Garage", font=('Comic Sans MS', 27, 'bold'), fg_color="turquoise4", cursor="hand2", height=60, width=180, command=open_garage)
        garage.place(x=10, y=340)
        garden = customtkinter.CTkButton(left_panel, text="Garden", font=('Comic Sans MS', 27, 'bold'), fg_color="IndianRed4", cursor="hand2", height=60, width=180, command=open_garden)
        garden.place(x=10, y=420)
        other_devices = customtkinter.CTkButton(left_panel, text="Other", font=('Comic Sans MS', 27, 'bold'), fg_color="turquoise4", cursor="hand2", height=60, width=180, command=open_others)
        other_devices.place(x=10, y=500)
        
        
if __name__ == "__main__":
    app = DeviceController()
    app.mainloop()