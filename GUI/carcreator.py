import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from .autocompleteentry import AutocompleteEntry

class CarCreator(tk.Toplevel):
    def __init__(self, *, parent, autohaus, **kwargs):
        super().__init__(parent, **kwargs)
        self.title("Auto erstellen")
        self.parent = parent
        self.autohaus = autohaus
        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)

        self.brand_label = ttk.Label(self, text="Marke:")
        self.brand_label.grid(row=0, column=0, sticky=tk.W)

        self.model_label = ttk.Label(self, text="Modell:")
        self.model_label.grid(row=0, column=1, sticky=tk.W)

        self.price_label = ttk.Label(self, text="Preis:")
        self.price_label.grid(row=0, column=2, sticky=tk.W)


        self.brand_entry = AutocompleteEntry(self, autocomplete_func=self.autohaus.get_brands)
        self.brand_entry.grid(row=1, column=0, sticky=tk.W)

        self.model_entry = AutocompleteEntry(self, autocomplete_func=lambda: self.autohaus.get_models(self.brand_entry.get()))
        self.model_entry.grid(row=1, column=1, sticky=tk.W)

        self.price_entry = ttk.Entry(self)
        self.price_entry.grid(row=1, column=3, sticky=tk.W)


        self.submit_button = ttk.Button(self, text="Erstellen", command=self.submit)
        self.submit_button.grid(row=4, column=0, columnspan=3, sticky=tk.NSEW)

    def submit(self):
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        price = self.price_entry.get()

        if not brand or not model or not price:
            messagebox.showerror(title="Fehler!", message="Bitte fülle alle Felder aus!")
            return

        self.autohaus.add_car(brand=brand, model=model, price=price)
        self.destroy()
        self.parent.carlist.refresh()
        self.parent.carlist.tkraise()

    def load_protocol(self):
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.destroy()