import tkinter as tk
 
from .login import LoginFrame
from .standardView import StandardView

class GUI(tk.Tk):
    def __init__(self, *args, autohaus, **kwargs):
        super().__init__(*args, **kwargs)
        self.autohaus = autohaus
        self.title(f"Autohaus - {self.autohaus.name}")
        self.geometry("600x400")
        self.resizable(width=False, height=False)

        self.frames = []

        self.load_protocol()
        self.login()

    def change_frame(self, frame):
        self.frames.append(frame)
        self.currentFrame = frame
        self.currentFrame.pack(fill=tk.BOTH, expand=True)
        self.currentFrame.tkraise()

    def login(self):
        login_popup = LoginFrame(self, autohaus= self.autohaus)
        self.change_frame(login_popup)

    def standardView(self):
        standard_view = StandardView(parent=self, autohaus=self.autohaus)
        self.change_frame(standard_view)

    def load_protocol(self):
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.autohaus.close()
        self.destroy()

