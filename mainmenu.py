from tkinter import *
from tkinter import ttk
from typing import Callable

class MainMenu:
    def __init__(self, tk, local2p: Callable):
        self.tk = tk

        self.style = ttk.Style(tk)
        # https://docs.microsoft.com/en-us/typography/fonts/windows_10_font_list
        self.style.configure("title.TLabel", font=("Sitka Text Bold", 50), foreground="purple")
        
        self.frame = ttk.Frame(self.tk)
        self.frame.pack(expand=True)

        self.title = ttk.Label(self.frame, text="WIZARD WEATHER WARS", style="title.TLabel")
        self.title.pack()

        self.localmultiplayer_btn = ttk.Button(self.frame, text="Local Multiplayer", command=lambda local2p=local2p: self.localmultiplayerPage(local2p))
        self.localmultiplayer_btn.pack()
    
    def localmultiplayerPage(self, local2p):
        self.frame.destroy()

        self.frame = ttk.Frame(self.tk)
        self.frame.pack(expand=True)

        self.local2p_btn = ttk.Button(self.frame, text="2 Player", command=lambda: self.runfunc(local2p))
        self.local2p_btn.pack()

    def runfunc(self, func):
        self.frame.destroy()
        func()