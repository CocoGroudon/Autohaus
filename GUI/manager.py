import tkinter as tk
 
from .login import LoginPopup
from .standardView import StandardView

class GUI(tk.Tk):
    def __init__(self, *args, autohaus, **kwargs):
        super().__init__(*args, **kwargs)
        self.autohaus = autohaus
        self.title("My GUI")
        self.geometry("600x400")
        self.resizable(width=False, height=False)

        self.frames = []

        self.login()

    def changeFrame(self, frame):
        self.frames.append(frame)
        self.currentFrame = frame
        self.currentFrame.pack(fill=tk.BOTH, expand=True)
        self.currentFrame.tkraise()

    def login(self):
        login_popup = LoginPopup(self, autohaus= self.autohaus)
        self.changeFrame(login_popup)

    def standardView(self):
        standard_view = StandardView(parent=self, autohaus=self.autohaus)
        self.changeFrame(standard_view)

