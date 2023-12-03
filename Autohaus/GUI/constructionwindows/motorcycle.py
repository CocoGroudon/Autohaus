import tkinter as tk

from .partframe import PartFrame
from ...vehicles.motorcycle import Motorcycle

class MotorcycleConstructionWindow(tk.Toplevel):
    def __init__(self, *, parent, autohaus, data, engine, gearbox, tire, chassis, **kwargs):
        super().__init__(parent, **kwargs)
        self.title("Motorrad erstellen")
        self.parent = parent
        self.autohaus = autohaus
        self.data = data

        self.engine = engine
        self.gearbox = gearbox
        self.tire = tire
        self.chassis = chassis

        self.vehicle = None

        self.create_widgets()

    def create_widgets(self):
        self.create_required_widgets()

    def create_required_widgets(self):
        self.engine_frame = PartFrame(parent=self, title="Motor", part=self.engine)
        self.engine_frame.grid(row=0, column=0, sticky=tk.W)

        self.gearbox_frame = PartFrame(parent=self, title="Getriebe", part=self.gearbox)
        self.gearbox_frame.grid(row=0, column=2, sticky=tk.W)

        self.tire_frame = PartFrame(parent=self, title="Reifen", part=self.tire)
        self.tire_frame.grid(row=0, column=3, sticky=tk.W)

        self.chassis_frame = PartFrame(parent=self, title="Chassis", part=self.chassis)
        self.chassis_frame.grid(row=0, column=4, sticky=tk.W)


        self.submit_button = ttk.Button(self, text="Erstellen", command=self.submit)
        self.submit_button.grid(row=5, column=0, columnspan=3, sticky=tk.NSEW)

    def submit(self):
        engine = self.engine_frame.get_part()
        gearbox = self.gearbox_frame.get_part()
        tire = self.tire_frame.get_part()
        chassis = self.chassis_frame.get_part()

        if not engine or not gearbox or not tire or not chassis:
            messagebox.showerror(title="Fehler!", message="Bitte fülle alle Felder mit * aus!")
            return

        self.vehicle = Motorcycle(engine=engine, gearbox=gearbox, tire=tire, chassis=chassis, **self.data)
        self.destroy()

    def load_protocol(self):
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.destroy()