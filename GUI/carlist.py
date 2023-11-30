import tkinter as tk
from tkinter import ttk

class CarPopup(tk.Toplevel):
    def __init__(self, *, parent, car, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.car = car

        self.title(f"{self.car.brand} {self.car.model}")
        self.resizable(width=True, height=True)
        self.geometry("400x400")

        
        self.load_protocol()
        self.create_widgets()

    def create_widgets(self):

        ttk.Label(self, text=f"Marke: {self.car.brand}").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(self, text=f"Model: {self.car.model}").grid(row=1, column=0, sticky=tk.W)
        ttk.Label(self, text=f"Preis: {self.car.price}").grid(row=2, column=0, sticky=tk.W)

        if self.car.description:    ttk.Label(self, text=f"Beschreibung:    {self.car.description}")    .grid(row=4, column=0, columnspan=3, sticky=tk.W)
        if self.car.sold:           ttk.Label(self, text=f"Verkauft:        {self.car.sold}")           .grid(row=4, column=2, sticky=tk.W)
        if self.car.fuel:           ttk.Label(self, text=f"Kraftstoff:      {self.car.fuel}")           .grid(row=4, column=2, sticky=tk.W)
        if self.car.gearbox:        ttk.Label(self, text=f"Getriebe:        {self.car.gearbox}")        .grid(row=4, column=2, sticky=tk.W)
        if self.car.age:            ttk.Label(self, text=f"Alter:           {self.car.age}")            .grid(row=4, column=2, sticky=tk.W)
        if self.car.color:          ttk.Label(self, text=f"Farbe:           {self.car.color}")          .grid(row=4, column=2, sticky=tk.W)
        if self.car.mileage:        ttk.Label(self, text=f"Kilometerstand:  {self.car.mileage}")        .grid(row=4, column=2, sticky=tk.W)
        if self.car.power:          ttk.Label(self, text=f"Leistung:        {self.car.power}")          .grid(row=4, column=2, sticky=tk.W)
        if self.car.fuel:           ttk.Label(self, text=f"Kraftstoff:      {self.car.fuel}")           .grid(row=4, column=2, sticky=tk.W)
    

        if self.car.image_path:
            self.image = tk.PhotoImage(file=self.car.image_path)
            self.image_label = ttk.Label(self, image=self.image)
            self.image_label.grid(row=0, column=1, rowspan=10, sticky=tk.NSEW)

    def load_protocol(self):
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.destroy()

class CarLabel(ttk.Frame):
    def __init__(self, *, parent, car, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.car = car
        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        ttk.Label(self, text=self.car.brand).grid(row=0, column=0, sticky=tk.W)
        ttk.Label(self, text=self.car.model).grid(row=0, column=1, sticky=tk.W)
        ttk.Label(self, text=self.car.price).grid(row=0, column=2, sticky=tk.W)

        self.view_button = ttk.Button(self, text="Einsehen", command=self.view)
        self.view_button.grid(row=0, column=3, sticky=tk.E)

    def view(self):
        CarPopup(parent=self.parent, car=self.car)

class CarList(ttk.Frame):
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

        for car in self.autohaus.get_cars():
            CarLabel(parent=self.frame, car=car).pack(fill=tk.X)

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


