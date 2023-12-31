import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Login popup window from main window
# smmall child window asking for username and password

class LoginFrame(ttk.Frame):
    def __init__(self, parent, autohaus, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.autohaus = autohaus
        self.credentialManager = autohaus.credentialManager
        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)

        ttk.Label(self, text="Nutzername:").grid(row=0, column=0, sticky=tk.W)
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=0, column=1, sticky=tk.E)
        self.username_entry.focus()

        ttk.Label(self, text="Passwort:").grid(row=1, column=0, sticky=tk.W)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, sticky=tk.E)

        ttk.Button(self, text="Eingabe", command=self.submit).grid(row=2, column=0, columnspan=2)

    def submit(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror(title="Fehler!", message="Bitte gebe sowohl den Nutzername, als auch das Passwort ein!")
            return
        
        is_valid = self.credentialManager.validate_login(username=username, password=password)

        if is_valid:
            self.autohaus.set_user(self.credentialManager.get_user(username=username))
            self.destroy()
            self.parent.standardView()
        else:
            messagebox.showerror(title="Fehler!", message="Falscher Nutzername oder Passwort!")