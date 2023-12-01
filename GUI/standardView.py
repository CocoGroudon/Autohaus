import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font

from .vehiclelist import VehicleList
from .creator import Creator

class Header(ttk.Frame):
    def __init__(self, *, parent, autohaus, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.autohaus = autohaus
        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)

        self.logout = ttk.Button(self, text="Abmelden", command=self.logout)
        self.logout.grid(row=0, column=0, sticky=tk.W)

        self.user = ttk.Label(self, text=f"Wilkommen {self.autohaus.user.displayname}!")
        self.user.grid(row=0, column=1, sticky=tk.W)

    def logout(self):
        self.parent.logout()

class StandardView(ttk.Frame):
    def __init__(self, *, parent, autohaus, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.autohaus = autohaus
        self.user = autohaus.user
        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)

        self.header = Header(parent=self, autohaus=self.autohaus)
        self.header.grid(row=0, column=0, sticky=tk.NSEW)

        self.vehicleceate_button = ttk.Button(self, text="Auto hinzufügen", command=self.create_vehicle)
        self.vehicleceate_button.grid(row=1, column=0, sticky=tk.NSEW)

        self.vehiclelist = VehicleList(parent=self, autohaus=self.autohaus)
        self.vehiclelist.grid(row=2, column=0, sticky=tk.NSEW)


    def create_vehicle(self):
        Creator(parent=self, autohaus=self.autohaus)

    def logout(self):
        self.autohaus.logout()
        self.destroy()
        self.parent.login()



