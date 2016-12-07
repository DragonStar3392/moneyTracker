import tkinter as tk
from tkinter import ttk

class WarningPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text = "This is an alpha version, use at your own discretion.",
                         font = ("Times New Roman", 30, "bold"))
        label.pack(pady=10,padx=10)

        firstStyle = ttk.Style()
        firstStyle.configure("First.TButton",font = ('Sans','20','bold'))
                         
        agreeButton = ttk.Button(self, text="Agree",
                           command=lambda: controller.show_frame("Home"), style ="First.TButton")
        agreeButton.pack()

        disagreeButton = ttk.Button(self, text="Disagree",command=quit, style ="First.TButton")
        disagreeButton.pack()
