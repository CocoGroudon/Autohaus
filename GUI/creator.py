import tkinter as tk
from tkinter import messagebox, ttk, filedialog

from .autocompleteentry import AutocompleteEntry

class Creator(tk.Toplevel):
    def __init__(self, *, parent, autohaus, **kwargs):
        super().__init__(parent, **kwargs)
        self.title("Auto erstellen")
        self.parent = parent
        self.autohaus = autohaus
        self.create_widgets()

    def create_widgets(self):
        self.create_required_widgets()
        self.create_optional_widgets()

    def create_optional_widgets(self):
        self.age_label = ttk.Label(self, text="Alter:")
        self.age_label.grid(row=2, column=0, sticky=tk.W)
        self.age_entry = ttk.Entry(self)
        self.age_entry.grid(row=3, column=0, sticky=tk.W)

        self.color_label = ttk.Label(self, text="Farbe:")
        self.color_label.grid(row=2, column=1, sticky=tk.W)
        self.color_entry = ttk.Entry(self)
        self.color_entry.grid(row=3, column=1, sticky=tk.W)

        self.mileage_label = ttk.Label(self, text="Kilometerstand:")
        self.mileage_label.grid(row=2, column=2, sticky=tk.W)
        self.mileage_entry = ttk.Entry(self)
        self.mileage_entry.grid(row=3, column=2, sticky=tk.W)

        self.fuel_label = ttk.Label(self, text="Kraftstoff:")
        self.fuel_label.grid(row=2, column=3, sticky=tk.W)
        self.fuel_entry = AutocompleteEntry(self, autocomplete_func=lambda: self.autohaus.get_fuels())
        self.fuel_entry.grid(row=3, column=3, sticky=tk.W)

        self.power_label = ttk.Label(self, text="Leistung:")
        self.power_label.grid(row=2, column=4, sticky=tk.W)
        self.power_entry = ttk.Entry(self)
        self.power_entry.grid(row=3, column=4, sticky=tk.W)

        self.gearbox_label = ttk.Label(self, text="Getriebe:")
        self.gearbox_label.grid(row=2, column=5, sticky=tk.W)
        self.gearbox_entry = AutocompleteEntry(self, autocomplete_func=lambda: self.autohaus.get_gearboxes())
        self.gearbox_entry.grid(row=3, column=5, sticky=tk.W)


        self.image_path = None
        self.image_button = ttk.Button(self, text="Bild Auswählen", command=self.select_image)
        self.image_button.grid(row=4, column=0, sticky=tk.W)
        self.image_label = ttk.Label(self)
        self.image_label.grid(row=4, column=1, sticky=tk.W)


    def select_image(self):
        self.image_path = filedialog.askopenfilename(title = "Bild auswählen",filetypes =[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        self.image_label.config(text=self.image_path)


    def create_required_widgets(self):
        # takes possible types from autohaus.known_types and creates a selection menu
        self.type_entry = ttk.Combobox(self, values=list(self.autohaus.known_types.keys()))
        self.type_entry.grid(row=0, column=3, sticky=tk.W)

        self.brand_label = ttk.Label(self, text="Marke *:")
        self.brand_label.grid(row=0, column=0, sticky=tk.W)

        self.model_label = ttk.Label(self, text="Modell *:")
        self.model_label.grid(row=0, column=1, sticky=tk.W)

        self.price_label = ttk.Label(self, text="Preis *:")
        self.price_label.grid(row=0, column=2, sticky=tk.W)

        self.brand_entry = AutocompleteEntry(self, autocomplete_func=self.autohaus.get_brands)
        self.brand_entry.grid(row=1, column=0, sticky=tk.W)

        self.model_entry = AutocompleteEntry(self, autocomplete_func=lambda: self.autohaus.get_models(self.brand_entry.get()))
        self.model_entry.grid(row=1, column=1, sticky=tk.W)

        self.price_entry = ttk.Entry(self)
        self.price_entry.grid(row=1, column=2, sticky=tk.W)

        self.submit_button = ttk.Button(self, text="Erstellen", command=self.submit)
        self.submit_button.grid(row=5, column=0, columnspan=3, sticky=tk.NSEW)

    def submit(self):
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        price = self.price_entry.get()

        vehicle_type = self.type_entry.get()

        if not brand or not model or not price or not vehicle_type:
            messagebox.showerror(title="Fehler!", message="Bitte fülle alle Felder aus!")
            return

        self.autohaus.add_vehicle(
            vehicle_type=vehicle_type,
            brand=brand,
            model=model, 
            price=price, 
            age=self.age_entry.get(), 
            color=self.color_entry.get(), 
            mileage=self.mileage_entry.get(), 
            fuel=self.fuel_entry.get(), 
            power=self.power_entry.get(), 
            gearbox=self.gearbox_entry.get(), 
            image_path=self.image_path
            )
        self.destroy()
        self.parent.vehiclelist.refresh()
        self.parent.vehiclelist.tkraise()

    def load_protocol(self):
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.destroy()