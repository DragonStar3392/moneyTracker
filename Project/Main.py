import tkinter as tk
from tkinter import ttk
import time as tm
import sys

from warningPage import WarningPage #user-written files
from modifyPage import * #user-written files
from displayPage import * #user-written files

width = 500
height = 550
    
class moneyTracker(tk.Tk):
    #main container
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.iconbitmap(self,default="coin2.ico")
        tk.Tk.wm_title(self,"Money Tracker (0.0.7)")
        
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        for F in (WarningPage, Home, Modify, InputFees, ModifyFees,
                  Display,DToday,DWeek,DMonth,DYear):   #pages
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame("WarningPage")

    def show_frame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        
class Home(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tname = tk.Label(self, text = "Money Usage Tracker",font=("Lucida Handwriting",40, "bold"),bg = "white")
        tname.pack(fill = "both", expand = 1)
        creator = tk.Label(self, text = "By: Shouh Yann, ID: 59090029",font=("Lucida Handwriting",20, "bold"),bg = "white")
        creator.pack(fill = "both", expand = 1)
        
        modifyBttn = tk.Button(self, text = 'Modify' , compound = "center", width = 8,
                            font=("Lucida Handwriting",15),bg = "#313AFF",
                               command=lambda: controller.show_frame("Modify"))
        modifyBttn.pack(fill = "both", expand = 1,padx = 150, pady = 10)
        
        displayBttn = tk.Button(self, text = 'Display' , compound = "center", width = 8,
                             font=("Lucida Handwriting",15),bg = "#38F35A",
                                command=lambda: controller.show_frame("Display"))
        displayBttn.pack(fill = "both", expand = 1,padx = 150, pady = 10)

        exitBttn = tk.Button(self, text = 'Exit' , compound = "center", width = 8,\
                          font=("Lucida Handwriting",15),command = self.exiting(),bg = "#F73030")
        exitBttn.pack(fill = "both", expand = 1,padx = 150, pady = 20)
        
        
    def exiting(self):
        answer = tk.messagebox.askyesno("Confirm","Exit?")
        if answer == True:
            try:
                sys.exit() # this always raises SystemExit
            except SystemExit:
                print("sys.exit() worked as expected")
            except Exception as ex:
                print("Error: ",ex) # some other exception got raised
        else:
            return
        
if __name__ == "__main__":
    app = moneyTracker()
    app.mainloop()
    
