import tkinter as tk
from tkinter import ttk
import time as tm
import os

class Display(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Display", font=("Lucida Handwriting",30, "bold"))
        label.pack(side="top", fill="x", pady=10)

        newStyle = ttk.Style()
        newStyle.configure("Newstyle.TButton",font = ('Sans','15','bold'))

        homeStyle = ttk.Style()
        homeStyle.configure("Home.TButton",font = ('Arial','15','italic'))
        
        dtodayBttn = ttk.Button(self, text="Display today's?", compound = "center", width = 8,
                           command=lambda: controller.show_frame("DToday"), style ="Newstyle.TButton")
        dtodayBttn.pack(fill = "both",expand = True, padx = 200,pady = 10)

        dweekBttn = ttk.Button(self, text="Display this week's?", compound = "center", width = 8,
                           command=lambda: controller.show_frame("DWeek"), style ="Newstyle.TButton")
        dweekBttn.pack(fill = "both",expand = True, padx = 200,pady = 10)

        dmonthBttn = ttk.Button(self, text="Display this month's?", compound = "center", width = 8,
                           command=lambda: controller.show_frame("DMonth"), style ="Newstyle.TButton")
        dmonthBttn.pack(fill = "both",expand = True, padx = 200,pady = 10)

        dyearBttn = ttk.Button(self, text="Display this year's?", compound = "center", width = 8,
                           command=lambda: controller.show_frame("DYear"), style ="Newstyle.TButton")
        dyearBttn.pack(fill = "both",expand = True, padx = 200,pady = 10)
        
        home = ttk.Button(self, text="Go back to the home page",
                           command=lambda: controller.show_frame("Home"), style ="Home.TButton")
        home.pack(fill= "both",expand = True, padx = 300, pady = 5)
        
class DToday(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        homeStyle = ttk.Style()
        homeStyle.configure("Home.TButton",font = ('Arial','15','italic'))

        showStyle = ttk.Style()
        showStyle.configure("display.TButton",font = ('SimSun','15','bold'))

        show = ttk.Button(self, text="Display!",
                          command=lambda:self.shows(), style = "display.TButton")
        show.pack(fill="x",expand = True, padx = 300, pady = 5)
        
        home = ttk.Button(self, text="帰れ！！！",
                           command=lambda: controller.show_frame("Display"), style ="Home.TButton")
        home.pack(fill= "x",expand = True, padx = 300, pady = 5)
    def shows(self):
        try:
            if os.stat('Payment.txt').st_size > 0: #if not empty and check by size of bytes
                toRead = open('Payment.txt','r')
                currentTime = tm.strftime("%A %b %d, %Y %H:%M:%S +0700", tm.localtime())
                    
                currTime = currentTime.replace(',',' ')
                currTime = currTime.replace(':',' ')
                currTime = currTime.replace('+',' ') #get info on today's date
                currTime = currTime.replace(',',' ')
                currTime = currTime.split()

                data = toRead.readlines()
                for line in data:
                        
                    line = line.replace(',',' ')
                    line = line.replace(':',' ')
                    line = line.replace('+',' ')
                    line = line.replace(',',' ')
                    line = line.split()
                        
                    if(currTime[1] == line[2] and currTime[2] == line[3] and currTime[3] and line[4]): #today
                        tk.messagebox.showinfo("Today","Today's input: "+str(line[0])+" Baht.")
                        toRead.close() #curr(1 is month, 2 is date, 3 is year),line(2 is month, 3 is date, 4 is year)
                        return
        
                toRead.close()
                tk.messagebox.showerror("Error!","Today's one doesn't exist yet!")
                    
            else: #empty file
                tk.messagebox.showerror("Error!","Empty file!")
        except OSError: #file doesn't exist
            tk.messagebox.showerror("Error!","Unable to open file cause it doesn't exist!")
        
class DWeek(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        showStyle = ttk.Style()
        showStyle.configure("display.TButton",font = ('SimSun','15','bold'))

        show = ttk.Button(self, text="Display!",
                          command=lambda:self.shows(), style = "display.TButton")
        show.pack(fill="x",expand = True, padx = 300, pady = 5)
        
        homeStyle = ttk.Style()
        homeStyle.configure("Home.TButton",font = ('Arial','15','italic'))

        home = ttk.Button(self, text="帰れ！！！",
                           command=lambda: controller.show_frame("Display"), style ="Home.TButton")
        home.pack(fill= "x",expand = True, padx = 300, pady = 5)
        
    def shows(self):
        try:
            if os.stat('Payment.txt').st_size > 0: #if not empty and check by size of bytes
                toRead = open('Payment.txt','r')
                currentTime = tm.strftime("%A %b %d, %Y %H:%M:%S +0700", tm.localtime())
                    
                currTime = currentTime.replace(',',' ')
                currTime = currTime.replace(':',' ')
                currTime = currTime.replace('+',' ') #get info on today's date
                currTime = currTime.replace(',',' ')
                currTime = currTime.split()

                data = toRead.readlines()
                for line in data:
                        
                    line = line.replace(',',' ')
                    line = line.replace(':',' ')
                    line = line.replace('+',' ')
                    line = line.replace(',',' ')
                    line = line.split()
                        
                    if(currTime[1] == line[2] and currTime[2] == line[3] and currTime[3] and line[4]):
                        tk.messagebox.showinfo("This week","Input: "+str(line[0])+" Baht.")
                        toRead.close() #curr(1 is month, 2 is date, 3 is year),line(2 is month, 3 is date, 4 is year)
                        return
        
                toRead.close()
                tk.messagebox.showerror("Error!","Today's one doesn't exist yet!")
                    
            else: #empty file
                tk.messagebox.showerror("Error!","Empty file!")
        except OSError: #file doesn't exist
            tk.messagebox.showerror("Error!","Unable to open file cause it doesn't exist!")
                
class DMonth(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        showStyle = ttk.Style()
        showStyle.configure("display.TButton",font = ('SimSun','15','bold'))

        show = ttk.Button(self, text="Display!",
                          command=lambda:self.shows(), style = "display.TButton")
        show.pack(fill="x",expand = True, padx = 300, pady = 5)
        
        homeStyle = ttk.Style()
        homeStyle.configure("Home.TButton",font = ('Arial','15','italic'))

        home = ttk.Button(self, text="帰れ！！！",
                           command=lambda: controller.show_frame("Display"), style ="Home.TButton")
        home.pack(fill= "x",expand = True, padx = 300, pady = 5)
    def shows(self):
        try:
            if os.stat('Payment.txt').st_size > 0: #if not empty and check by size of bytes
                toRead = open('Payment.txt','r')
                currentTime = tm.strftime("%A %b %d, %Y %H:%M:%S +0700", tm.localtime())
                    
                currTime = currentTime.replace(',',' ')
                currTime = currTime.replace(':',' ')
                currTime = currTime.replace('+',' ') #get info on today's date
                currTime = currTime.replace(',',' ')
                currTime = currTime.split()

                data = toRead.readlines()
                for line in data:
                        
                    line = line.replace(',',' ')
                    line = line.replace(':',' ')
                    line = line.replace('+',' ')
                    line = line.replace(',',' ')
                    line = line.split()
                        
                    if(currTime[1] == line[2] and currTime[2] == line[3] and currTime[3] and line[4]):
                        tk.messagebox.showinfo("This month","Input: "+str(line[0])+" Baht.")
                        toRead.close() #curr(1 is month, 2 is date, 3 is year),line(2 is month, 3 is date, 4 is year)
                        return
        
                toRead.close()
                tk.messagebox.showerror("Error!","Today's one doesn't exist yet!")
                    
            else: #empty file
                tk.messagebox.showerror("Error!","Empty file!")
        except OSError: #file doesn't exist
            tk.messagebox.showerror("Error!","Unable to open file cause it doesn't exist!")
                
class DYear(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        showStyle = ttk.Style()
        showStyle.configure("display.TButton",font = ('SimSun','15','bold'))

        show = ttk.Button(self, text="Display!",
                          command=lambda:self.shows(), style = "display.TButton")
        show.pack(fill="x",expand = True, padx = 300, pady = 5)
        
        homeStyle = ttk.Style()
        homeStyle.configure("Home.TButton",font = ('Arial','15','italic'))

        home = ttk.Button(self, text="帰れ！！！",
                           command=lambda: controller.show_frame("Display"), style ="Home.TButton")
        home.pack(fill= "x",expand = True, padx = 300, pady = 5)
    def shows(self):
        try:
            if os.stat('Payment.txt').st_size > 0: #if not empty and check by size of bytes
                toRead = open('Payment.txt','r')
                currentTime = tm.strftime("%A %b %d, %Y %H:%M:%S +0700", tm.localtime())
                    
                currTime = currentTime.replace(',',' ')
                currTime = currTime.replace(':',' ')
                currTime = currTime.replace('+',' ') #get info on today's date
                currTime = currTime.replace(',',' ')
                currTime = currTime.split()

                data = toRead.readlines()
                for line in data:
                        
                    line = line.replace(',',' ')
                    line = line.replace(':',' ')
                    line = line.replace('+',' ')
                    line = line.replace(',',' ')
                    line = line.split()
                        
                    if(currTime[1] == line[2] and currTime[2] == line[3] and currTime[3] and line[4]):
                        tk.messagebox.showinfo("This year","Input: "+str(line[0])+" Baht.")
                        toRead.close() #curr(1 is month, 2 is date, 3 is year),line(2 is month, 3 is date, 4 is year)
                        return
        
                toRead.close()
                tk.messagebox.showerror("Error!","Today's one doesn't exist yet!")
                    
            else: #empty file
                tk.messagebox.showerror("Error!","Empty file!")
        except OSError: #file doesn't exist
            tk.messagebox.showerror("Error!","Unable to open file cause it doesn't exist!")
