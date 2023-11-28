import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font


class StandardView(ttk.Frame):
    def __init__(self, *, parent, autohaus, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.autohaus = autohaus
        self.user = autohaus.user
        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)

        ttk.Label(self, text=f"Wilkommen {self.user.displayname}!").grid(row=0, column=0, sticky=tk.W)

        ttk.Button(self, text="Logout", command=self.logout).grid(row=1, column=0, columnspan=2)

    def logout(self):
        self.autohaus.logout()
        self.destroy()
        self.parent.login()


