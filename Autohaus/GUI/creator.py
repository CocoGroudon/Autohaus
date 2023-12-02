import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from PIL import Image
import os
import datetime

from .autocompleteentry import AutocompleteEntry
from .constructionwindows.car import CarConstructionWindow
from .constructionwindows.motorcycle import MotorcycleConstructionWindow

from .. import vehicles



class Creator(tk.Toplevel):
    def __init__(self, *, parent, autohaus, **kwargs):
        super().__init__(parent, **kwargs)
        self.title("Auto erstellen")
        self.parent = parent
        self.autohaus = autohaus
        self.Settings = autohaus.Settings
        self.create_widgets()


    def create_widgets(self):
        self.create_image_upload()
        self.create_required_widgets()

    def create_image_upload(self):

        def select_image():
            self.image_path = filedialog.askopenfilename(title = "Bild auswählen",filetypes =[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
            # TODO: show downscaled image
            self.image_label.config(text=self.image_path)

        self.image_path = None
        self.image_button = ttk.Button(self, text="Bild Auswählen", command=select_image)
        self.image_button.grid(row=15, column=0, sticky=tk.W)
        self.image_label = ttk.Label(self)
        self.image_label.grid(row=15, column=1, sticky=tk.W)


    def create_required_widgets(self):
        # takes possible types from autohaus.known_vehicle_types and creates a selection menu
        self.type_label = ttk.Label(self, text="Typ *:")
        self.type_label.grid(row=0, column=0, sticky=tk.W)
        self.type_entry = ttk.Combobox(self, values=list(vehicles.known_types.keys()))
        self.type_entry.grid(row=0, column=1, sticky=tk.W)

        self.brand_label = ttk.Label(self, text="Marke *:")
        self.brand_label.grid(row=1, column=0, sticky=tk.W)
        self.brand_entry = AutocompleteEntry(self, autocomplete_func=self.autohaus.get_brands)
        self.brand_entry.grid(row=1, column=1, sticky=tk.W)

        self.model_label = ttk.Label(self, text="Modell *:")
        self.model_label.grid(row=2, column=0, sticky=tk.W)
        self.model_entry = AutocompleteEntry(self, autocomplete_func=lambda: self.autohaus.get_models(self.brand_entry.get()))
        self.model_entry.grid(row=2, column=1, sticky=tk.W)

        self.price_label = ttk.Label(self, text="Preis *:")
        self.price_label.grid(row=3, column=0, sticky=tk.W)
        self.price_entry = ttk.Entry(self)
        self.price_entry.grid(row=3, column=1, sticky=tk.W)


        self.color_label = ttk.Label(self, text="Farbe:")
        self.color_label.grid(row=4, column=0, sticky=tk.W)
        self.color_entry = ttk.Entry(self)
        self.color_entry.grid(row=4, column=1, sticky=tk.W)

        self.engine_label = ttk.Label(self, text="Motor Typ:")
        self.engine_label.grid(row=5, column=0, sticky=tk.W)
        self.engine_entry = ttk.Combobox(self, values=list(vehicles.parts.engine.known_types.keys()))
        self.engine_entry.grid(row=5, column=1, sticky=tk.W)

        self.gearbox_label = ttk.Label(self, text="Getriebe:")
        self.gearbox_label.grid(row=7, column=0, sticky=tk.W)
        self.gearbox_entry = ttk.Combobox(self, values=list(vehicles.parts.gearbox.known_types.keys()))
        self.gearbox_entry.grid(row=7, column=1, sticky=tk.W)

        self.tire_label = ttk.Label(self, text="Reifen:")
        self.tire_label.grid(row=8, column=0, sticky=tk.W)
        self.tire_entry = ttk.Combobox(self, values=list(vehicles.parts.tire.known_types.keys()))
        self.tire_entry.grid(row=8, column=1, sticky=tk.W)

        self.chassis_label = ttk.Label(self, text="Fahrwerk:")
        self.chassis_label.grid(row=9, column=0, sticky=tk.W)
        self.chassis_entry = ttk.Combobox(self, values=list(vehicles.parts.chassis.known_types.keys()))
        self.chassis_entry.grid(row=9, column=1, sticky=tk.W)



        self.submit_button = ttk.Button(self, text="Weiter", command=self.submit)
        self.submit_button.grid(row=20, column=0, columnspan=2, sticky=tk.NSEW)

    def process_image(self, original_path, new_path):
        new_type = "PNG"
        new_size = (300, 300)
        image = Image.open(original_path)
        # Scale image so that it fitns into the new size but keeps the aspect ratio
        image.thumbnail(new_size, )
        # Save image
        image.save(new_path, new_type)

    def submit(self):
        vehicle_type = self.type_entry.get()
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        price = self.price_entry.get()

        color = self.color_entry.get()

        engine = vehicles.parts.engine.known_types[self.engine_entry.get()]
        gearbox =vehicles.parts.gearbox.known_types[self.gearbox_entry.get()]
        tire = vehicles.parts.tire.known_types[self.tire_entry.get()]
        chassis = vehicles.parts.chassis.known_types[self.chassis_entry.get()]

        if not brand or not model or not price or not vehicle_type or not engine or not gearbox or not tire or not chassis or not color:
            messagebox.showerror(title="Fehler!", message="Bitte fülle alle Felder aus!")
            return
        
        new_path = os.path.join(self.Settings.IMAGE_DIR, f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
        self.process_image(self.image_path, new_path)

        data = {
            "brand": brand,
            "model": model,
            "price": price,
            "color": color,
            "description": None,
            "image_path": new_path,
        }



        if not vehicle_type in vehicles.known_types.keys():
            messagebox.showerror(title="Fehler!", message="Dieser Fahrzeugtyp wird noch nicht unterstützt!")
            return
        

        match vehicle_type:
            case "Car":
                self.destroy()
                window = CarConstructionWindow(parent=self.parent, autohaus=self.autohaus, data=data, engine=engine, gearbox=gearbox, tire=tire, chassis=chassis)
                self.parent.wait_window(window)
                vehicle = window.vehicle

            case "Motorcycle":
                self.destroy
                window = MotorcycleConstructionWindow(parent=self.parent, autohaus=self.autohaus, data=data, engine=engine, gearbox=gearbox, tire=tire, chassis=chassis)
                self.parent.wait_window(window)
                vehicle = window.vehicle
            case _:
                messagebox.showerror(title="Fehler!", message="Dieser Fahrzeugtyp wird noch nicht unterstützt!")
                return

        self.autohaus.add_vehicle(vehicle)    
    
        self.destroy()
        self.parent.vehiclelist.refresh()
        self.parent.vehiclelist.tkraise()


    def load_protocol(self):
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.destroy()