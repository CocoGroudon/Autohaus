import tkinter as tk
from tkinter import ttk

class VehiclePopup(tk.Toplevel):
    def __init__(self, *, parent, vehicle, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.vehicle = vehicle

        self.title(f"{self.vehicle.brand} {self.vehicle.model}")
        self.resizable(width=False, height=False)

        
        self.load_protocol()
        self.create_widgets()

    def create_widgets(self):

        ttk.Label(self, text=f"Marke: {self.vehicle.brand}").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(self, text=f"Model: {self.vehicle.model}").grid(row=1, column=0, sticky=tk.W)
        ttk.Label(self, text=f"Preis: {self.vehicle.price}").grid(row=2, column=0, sticky=tk.W)

        ttk.Label(self, text=f"Farbe: {self.vehicle.color}").grid(row=3, column=0, sticky=tk.W)

        ttk.Label(self, text=f"Beschreibung:    {self.vehicle.description}")    .grid(row=4, column=0, rowspan=3, sticky=tk.W)

        ttk.Label(self, text=f"Verkauft: {'Nein' if not self.vehicle.sold else 'Ja'}")          .grid(row=0, column=2, sticky=tk.W)

        ttk.Label(self, text=self.vehicle.parts["engine"].infotext).grid(row=2, column=10, sticky=tk.W)

        ttk.Label(self, text=self.vehicle.parts["gearbox"].infotext).grid(row=3, column=10, sticky=tk.W)

        ttk.Label(self, text=self.vehicle.parts["tire"].infotext)   .grid(row=4, column=10, sticky=tk.W)

        ttk.Label(self, text=self.vehicle.parts["chassis"].infotext).grid(row=5, column=10, sticky=tk.W)




        
        self.image = tk.PhotoImage(file=self.vehicle.image_path)
        self.image_label = ttk.Label(self, image=self.image)
        self.image_label.grid(row=0, column=1, rowspan=30, columnspan=5, sticky=tk.NSEW)

    def load_protocol(self):
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.destroy()

class VehicleLabel(ttk.Frame):
    def __init__(self, *, parent, vehicle, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.vehicle = vehicle
        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        ttk.Label(self, text=self.vehicle.brand).grid(row=0, column=0, sticky=tk.W)
        ttk.Label(self, text=self.vehicle.model).grid(row=0, column=1, sticky=tk.W)
        ttk.Label(self, text=self.vehicle.price).grid(row=0, column=2, sticky=tk.W)

        self.view_button = ttk.Button(self, text="Einsehen", command=self.view)
        self.view_button.grid(row=0, column=3, sticky=tk.E)

    def view(self):
        VehiclePopup(parent=self.parent, vehicle=self.vehicle)

class VehicleList(ttk.Frame):
    def __init__(self, *, parent, autohaus, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.autohaus = autohaus

        self.setup()
        self.create_widgets()

    def setup(self):
        self.canvas = tk.Canvas(self)
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.frame = ttk.Frame(self.canvas)

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)

        self.canvas.create_window((0,0), window=self.frame, anchor="nw", tags="self.frame")
        self.canvas.configure(yscrollcommand=self.vsb.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.vsb.pack(side="right", fill="y")

    def refresh(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.create_widgets()


    def create_widgets(self):
        bbox = self.canvas.bbox("all")
        self.canvas.config(scrollregion=bbox)
        
        self.info = ttk.Label(self.frame, text="Marke\tModel\tPreis")
        self.info.pack(fill=tk.X)

        for vehicle in self.autohaus.get_vehicles():
            VehicleLabel(parent=self.frame, vehicle=vehicle).pack(fill=tk.X)

    def _on_mousewheel(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")
        else:
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


