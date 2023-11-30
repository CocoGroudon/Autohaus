import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font

class CarLabel(ttk.Frame):
    def __init__(self, *, parent, car, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.car = car
        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        ttk.Label(self, text=self.car.brand).grid(row=0, column=0, sticky=tk.W)
        ttk.Label(self, text=self.car.model).grid(row=0, column=1, sticky=tk.W)
        ttk.Label(self, text=self.car.price).grid(row=0, column=2, sticky=tk.W)

class CarList(ttk.Frame):
    def __init__(self, *, parent, autohaus, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.autohaus = autohaus

        self.canvas = tk.Canvas(self)
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.frame = ttk.Frame(self.canvas)

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.canvas.create_window((0,0), window=self.frame, anchor="nw", tags="self.frame")
        self.canvas.configure(yscrollcommand=self.vsb.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.vsb.pack(side="right", fill="y")

        self.create_widgets()

    def create_widgets(self):
        bbox = self.canvas.bbox("all")
        self.canvas.config(scrollregion=bbox)
        
        self.info = ttk.Label(self.frame, text="Brand\tModel\tPrice")
        self.info.pack(fill=tk.X)

        for car in self.autohaus.get_cars():
            CarLabel(parent=self.frame, car=car).pack(fill=tk.X)
        
        # self.canvas.create_window((0,0), window=self.frame, anchor="nw", tags="self.frame")
        # self.frame.bind("<Configure>", self.onFrameConfigure)

    def _bind_mouse(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mouse(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))






class StandardView(ttk.Frame):
    def __init__(self, *, parent, autohaus, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.autohaus = autohaus
        self.user = autohaus.user
        self.create_widgets()

    def create_widgets(self):
        # self.columnconfigure(0, weight=1)

        # ttk.Label(self, text=f"Wilkommen {self.user.displayname}!").grid(row=0, column=0, sticky=tk.W)

        # ttk.Button(self, text="Logout", command=self.logout).grid(row=1, column=0, columnspan=2)

        self.carlist = CarList(parent=self, autohaus=self.autohaus)
        self.carlist.pack(fill=tk.BOTH, expand=True)
        # self.carlist_scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.carlist.yview)
        # self.carlist_scrollbar.grid(row=2, column=1, sticky=tk.NS)
        # self.carlist.config(yscrollcommand=self.carlist_scrollbar.set)



    def logout(self):
        self.autohaus.logout()
        self.destroy()
        self.parent.login()


