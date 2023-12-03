import tkinter as tk
from tkinter import messagebox, ttk, filedialog

class LabelEntryFrame(ttk.Frame):
    def __init__(self, *, parent, title, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.title = title
        self.create_widgets()
    
    def create_widgets(self):
        self.columnconfigure(0, weight=1)

        self.label = ttk.Label(self, text=self.title)
        self.label.grid(row=0, column=0, sticky=tk.W)

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=1, sticky=tk.E)
    
    def get_value(self):
        return self.entry.get()
    
    def set_value(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)


class PartFrame(ttk.Frame):
    def __init__(self, *, parent, title, part, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.title = title
        self.part = part

        self.required_parts = part.get_required_values()
        self.entries = []

        self.create_required_widgets()
        

    def create_required_widgets(self):
        part_label = ttk.Label(self, text=self.title)
        part_label.grid(row=0, column=0, sticky=tk.NW)

        row = 1
        print(self.required_parts)
        for item in self.required_parts:
            entry = LabelEntryFrame(parent=self, title=item)
            entry.grid(row=row, column=0, sticky=tk.W)
            self.entries.append(entry)
            row += 1


    def check_if_filled(self):
        for entry in self.entries:
            if not entry.get_value():
                messagebox.showerror(title="Fehler!", message=f"Bitte fülle alle Felder aus! {entry.title}")
                return False
        return True
    
    def get_values(self):
        values = {}
        for entry in self.entries:
            values[entry.title] = entry.get_value()
        return values
    
    def get_part(self):
        if not self.check_if_filled():
            return None
        return self.part(**self.get_values())