import tkinter as tk
from tkinter import ttk

class AutocompleteEntry(ttk.Frame):
    def __init__(self, parent, autocomplete_func:callable, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.autocomplete_func = autocomplete_func

        self.entry = ttk.Entry(self)
        self.entry.bind("<KeyRelease>", self.check_key)
        self.entry.pack()

        self.listbox = tk.Listbox(self, height=0)
        self.listbox.bind("<Double-Button-1>", self.select_value)
        self.listbox.bind("<Return>", self.select_value)
        self.listbox.pack()

    def get(self):
        return self.entry.get()

    def check_key(self, event):
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)

        typed = self.entry.get()
        if typed == '':
            return

        listbox_values = self.autocomplete_func()
        listbox_values = sorted(listbox_values)
        matching = [s for s in listbox_values if typed.lower() in s.lower()]

        self.listbox.config(height=min(len(matching), 5)) # limit height to 5 items

        if not matching:
            return
        
        for i in matching:
            self.listbox.insert(tk.END, i)


    def select_value(self, event):
        if not self.listbox.curselection(): # test if something is selected
            return

        value = self.listbox.get(self.listbox.curselection())
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)



if __name__ == "__main__":
    root = tk.Tk()

    autocomplete_list = ["Apfel", "Banane", "Kirsche", "Dattel", "Erdbeere", "Feige"]
    entry = AutocompleteEntry(root, autocomplete_list)
    entry.pack()

    root.mainloop()
